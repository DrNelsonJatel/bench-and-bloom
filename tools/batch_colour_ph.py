#!/usr/bin/env python3
"""
Bench & Bloom — batch colour / pH proxy tool.

The butterfly pea in the syrup is a polyacylated anthocyanin (ternatin), which is a
genuine pH indicator, so the product reports its own pH. This samples the liquid
column in a batch photograph and returns:

  1. a pH BRACKET from the ternatin colour series, and
  2. a hue drift check against the batch-1 reference.

WHAT THIS IS FOR
  Colour is a poor pH meter and an excellent THRESHOLD indicator. It cannot separate
  pH 2.3 from 2.6. It can state emphatically that the product is nowhere near pH 4,
  because ternatins are purple (hue 280-320) at pH 4-6. The threshold is the part that
  carries the safety claim, so that is the useful output.

WHAT THIS IS NOT
  Not a food-safety record. A meter reading is still required before printing an
  ambient best-before. Only the UPPER bound of the bracket carries information:
  anthocyanin concentration and path length both deepen colour toward red
  independently of pH, so the lower bound is an artifact of the colour series.

PHOTO PROTOCOL (follow it or the drift check is meaningless)
  White background, INDIRECT light (never direct sun, it clips the red channel),
  a white-balance reference in frame, same bottle, same fill level, no flash.

USAGE
  python3 tools/batch_colour_ph.py <image> [--batch LOT] [--log batch_colour_log.csv]
  python3 tools/batch_colour_ph.py --self-test
"""
from __future__ import annotations
import argparse, colorsys, csv, math, os, statistics as st, sys
from datetime import datetime, timezone

try:
    from PIL import Image
except ImportError:
    sys.exit("ERROR: Pillow is required.  pip3 install Pillow")

# ---------------------------------------------------------------- reference
# Batch 1, 2026-09-06, Photos/BnB_Lavender Syrop.JPG. Direct sun, so this
# reference is itself off-protocol; re-baseline on the first protocol photo.
REF = {"batch": "2026-001", "hue": 351.0, "hex": "#34020C", "drift_warn_deg": 8.0}

# Ternatin colour series: (label, hue arc, pH range). Arcs are in degrees and may
# wrap past 360; they are unwrapped to negatives before comparison.
SERIES = [("red / crimson",      (350, 375), (0.5, 2.0)),
          ("deep ruby / garnet", (340, 365), (1.5, 3.0)),
          ("magenta / pink",     (315, 345), (2.5, 4.0)),
          ("purple",             (280, 320), (4.0, 6.0)),
          ("blue-violet",        (250, 285), (5.5, 6.5)),
          ("blue",               (210, 255), (6.0, 7.5)),
          ("teal / green",       (150, 210), (8.0, 10.0))]

SAFETY_PH, HURDLE_PH = 4.6, 4.0          # acidified-food threshold; spec's own hurdle
# Colour brackets the product at <= 3.0. STATED_PH adds margin for proxy error and is
# the figure to quote in any document or claim until a meter reading exists.
STATED_PH = 3.5
DEFAULT_WINDOW = (0.34, 0.52, 0.60, 0.86)  # x0,x1,y0,y1 as fractions of W,H
MIN_SAT, MIN_VAL, MAX_VAL = 0.45, 0.10, 0.95

def _unwrap(a: float) -> float:
    return a - 360 if a > 300 else a

def circular_mean(degs: list[float]) -> tuple[float, float]:
    """Returns (mean angle in [0,360), resultant length R in [0,1])."""
    s = sum(math.sin(math.radians(d)) for d in degs) / len(degs)
    c = sum(math.cos(math.radians(d)) for d in degs) / len(degs)
    return math.degrees(math.atan2(s, c)) % 360, math.hypot(s, c)

def sample(path: str, window=DEFAULT_WINDOW):
    im = Image.open(path).convert("RGB")
    W, H = im.size
    fx0, fx1, fy0, fy1 = window
    x0, x1, y0, y1 = int(W*fx0), int(W*fx1), int(H*fy0), int(H*fy1)
    px = im.load()
    hues, rgbs, clipped, seen = [], [], 0, 0
    step = max(1, min(x1-x0, y1-y0)//180)          # ~180 samples per axis, any image size
    for y in range(y0, y1, step):
        for x in range(x0, x1, step):
            r, g, b = px[x, y]
            seen += 1
            if r >= 254 or g >= 254 or b >= 254:
                clipped += 1
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            if s > MIN_SAT and MIN_VAL < v < MAX_VAL:
                hues.append(h*360); rgbs.append((r, g, b, s, v))
    return dict(size=(W, H), box=(x0, x1, y0, y1), step=step, seen=seen,
                clipped=clipped, hues=hues, rgbs=rgbs)

def analyse(path: str, window=DEFAULT_WINDOW):
    d = sample(path, window)
    if len(d["hues"]) < 300:
        raise SystemExit(f"ERROR: only {len(d['hues'])} qualifying pixels in the sample window. "
                         f"Adjust --window; the default assumes the bottle is centre-frame.")
    hue, R = circular_mean(d["hues"])
    unw = sorted(_unwrap(h) for h in d["hues"])
    p10, p90 = unw[int(.10*len(unw))], unw[int(.90*len(unw))]
    r = st.median([x[0] for x in d["rgbs"]]); g = st.median([x[1] for x in d["rgbs"]])
    b = st.median([x[2] for x in d["rgbs"]])
    sat = st.median([x[3] for x in d["rgbs"]]); val = st.median([x[4] for x in d["rgbs"]])
    hits = [(n, a, z) for n, (h1, h2), (a, z) in SERIES
            if _unwrap(h1) <= _unwrap(hue) <= _unwrap(h2)]
    lo = min((h[1] for h in hits), default=None)
    hi = max((h[2] for h in hits), default=None)
    return dict(**d, hue=hue, R=R, spread=p90-p10, rgb=(r, g, b), sat=sat, val=val,
                hex=f"#{int(r):02X}{int(g):02X}{int(b):02X}",
                hits=[h[0] for h in hits], ph_lo=lo, ph_hi=hi,
                drift=abs((hue - REF["hue"] + 180) % 360 - 180),
                clip_pct=100*d["clipped"]/max(d["seen"], 1))

def report(a, batch, path):
    print("="*76); print(f"BENCH & BLOOM — batch colour / pH proxy"); print("="*76)
    print(f"  image      {os.path.basename(path)}  ({a['size'][0]} x {a['size'][1]})")
    print(f"  batch      {batch or '(unspecified)'}")
    print(f"  window     x[{a['box'][0]}:{a['box'][1]}] y[{a['box'][2]}:{a['box'][3]}] step {a['step']}")
    print(f"  pixels     {len(a['hues']):,} qualifying of {a['seen']:,} sampled")
    print(f"\n  median RGB {a['rgb'][0]:.0f}, {a['rgb'][1]:.0f}, {a['rgb'][2]:.0f}   {a['hex']}")
    print(f"  hue        {a['hue']:.1f} deg   (10th-90th spread {a['spread']:.1f} deg, R={a['R']:.3f})")
    print(f"  sat / val  {a['sat']:.2f} / {a['val']:.2f}      clipped {a['clip_pct']:.2f}%")
    print(f"\n  appearance {', '.join(a['hits']) or 'no match in the ternatin series'}")
    if a['ph_hi'] is not None:
        print(f"  >>> pH BRACKET  <= {a['ph_hi']}    (lower bound {a['ph_lo']} carries NO information)")
        print(f"      clears {SAFETY_PH} safety threshold : {'YES' if a['ph_hi'] < SAFETY_PH else 'NO'}")
        print(f"      clears {HURDLE_PH} acid hurdle      : {'YES' if a['ph_hi'] < HURDLE_PH else 'NO'}")
        print(f"      STATED value for documents/claims  : pH <= {STATED_PH} (proxy bracket + margin)")
    print(f"\n  drift vs batch {REF['batch']} (hue {REF['hue']}): {a['drift']:.1f} deg")

def qaqc(a) -> int:
    print("\n"+"="*76); print("QAQC"); print("="*76)
    fails = 0
    def ck(desc, ok, det=""):
        nonlocal fails
        if not ok: fails += 1
        print(f"  [{'PASS' if ok else 'FLAG'}] {desc}" + (f"  ({det})" if det else ""))
    ck("enough qualifying pixels", len(a['hues']) >= 300, f"{len(a['hues']):,}")
    ck("single tight hue population", a['spread'] < 45, f"{a['spread']:.1f} deg")
    ck("hue vector is coherent (R > 0.95)", a['R'] > 0.95, f"R={a['R']:.3f}")
    ck("saturation high enough to trust hue", a['sat'] > 0.50, f"{a['sat']:.2f}")
    ck("channel clipping under 1% (else re-shoot indirect)", a['clip_pct'] < 1.0,
       f"{a['clip_pct']:.2f}%")
    ck("red-dominant", a['rgb'][0] > a['rgb'][1] and a['rgb'][0] > a['rgb'][2])
    ck(f"NOT in the purple/blue arc (would mean pH > {HURDLE_PH})",
       not (250 <= a['hue'] <= 320), f"hue {a['hue']:.0f}")
    ck(f"pH bracket clears the {SAFETY_PH} safety threshold",
       a['ph_hi'] is not None and a['ph_hi'] < SAFETY_PH)
    ck(f"hue drift vs batch {REF['batch']} within {REF['drift_warn_deg']} deg",
       a['drift'] <= REF['drift_warn_deg'], f"{a['drift']:.1f} deg")
    print(f"\n  {fails} FLAG(s).")
    if fails:
        print("  A FLAG is not necessarily a bad batch. Check the photo protocol first:\n"
              "  white background, INDIRECT light, white-balance card, same fill.")
    return fails

def log_row(path_csv, batch, img, a):
    new = not os.path.exists(path_csv)
    with open(path_csv, "a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["utc", "batch", "image", "hue_deg", "hex", "sat", "val",
                        "spread_deg", "clip_pct", "ph_bracket_max", "drift_deg", "n_px"])
        w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), batch or "",
                    os.path.basename(img), f"{a['hue']:.1f}", a['hex'], f"{a['sat']:.2f}",
                    f"{a['val']:.2f}", f"{a['spread']:.1f}", f"{a['clip_pct']:.2f}",
                    a['ph_hi'], f"{a['drift']:.1f}", len(a['hues'])])
    print(f"\n  logged to {path_csv}")

def self_test() -> int:
    """Reproduce the published batch-1 figures. Fails loudly if the method drifts."""
    img = os.path.join(os.path.dirname(__file__), "..", "Photos", "BnB_Lavender Syrop.JPG")
    if not os.path.exists(img):
        print("SELF-TEST SKIPPED: batch-1 photo not present."); return 0
    a = analyse(img)
    print("="*76); print("SELF-TEST vs published batch-1 figures"); print("="*76)
    fails = 0
    for desc, got, want, tol in [("median hue ~351.0 deg", a['hue'], 351.0, 1.0),
                                 ("hue spread ~5.7 deg", a['spread'], 5.7, 2.0),
                                 ("saturation ~0.96", a['sat'], 0.96, 0.05),
                                 ("pH bracket max = 3.0", a['ph_hi'], 3.0, 0.001)]:
        ok = abs(got - want) <= tol
        if not ok: fails += 1
        print(f"  [{'PASS' if ok else 'FLAG'}] {desc}  (got {got:.2f}, want {want})")
    print(f"\n  {fails} FLAG(s).")
    return fails

def main():
    ap = argparse.ArgumentParser(description="Bench & Bloom batch colour / pH proxy")
    ap.add_argument("image", nargs="?", help="batch photograph")
    ap.add_argument("--batch", help="lot code, e.g. 2026-002")
    ap.add_argument("--log", help="append a row to this CSV batch log")
    ap.add_argument("--window", help="x0,x1,y0,y1 as fractions of width/height")
    ap.add_argument("--self-test", action="store_true", help="reproduce the batch-1 figures")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(1 if self_test() else 0)
    if not args.image:
        ap.error("give an image, or --self-test")
    win = DEFAULT_WINDOW
    if args.window:
        win = tuple(float(v) for v in args.window.split(","))
        if len(win) != 4: ap.error("--window needs four comma-separated fractions")
    a = analyse(args.image, win)
    report(a, args.batch, args.image)
    fails = qaqc(a)
    if args.log: log_row(args.log, args.batch, args.image, a)
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
