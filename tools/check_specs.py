#!/usr/bin/env python3
"""
Bench & Bloom — spec consistency checker.

These specs have been revised many times, by more than one author, and at least once
a corrected block reverted underneath us. This asserts that the facts of record agree
across every document, so a stale figure cannot quietly survive in one file.

  python3 tools/check_specs.py
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS = ["JATEL_ProductSpec_v1.0_20260906.md",
         "singlelabel/Label_PrinterSpec_Wrap_uline2026.md",
         "JATEL_BoxPackagingSpec_v1.0_20260906.md",
         "JATEL_SealStickerSpec_v1.0_20260906.md"]

# Text that must NOT appear outside a superseded/before-after context.
FORBIDDEN = [
    ("stale-brix-precision",   r"64\.8",            "Brix is stated as 64; no decimal"),
    ("wrong-postal-code",      r"V0H\s*1N0",        "farm postal code is V0H 1N1"),
    ("home-address",           r"Bernard\s*Ave|V1Y\s*6P7", "home address must never appear"),
    ("printed-date-in-art",    r"Packaged\s*/\s*Emball[ée]:\s*YYYY", "no date prints; coding panel is blank"),
    ("old-lot-only-format",    r"LOT:\s*2026-001",  "lot format is YYYYMMDD-nn"),
    ("stale-serving-15ml",     r"per\s*15\s*mL",    "prescribed serving is 30 mL"),
    # only flag "not required" when REQUIRED does not also appear on the line,
    # so the July-vs-current comparison rows do not trip it
    ("stale-fop-not-required", r"(?!.*REQUIRED).*symbol[^.]{0,40}not\s+required",
                               "the sugars symbol IS required"),
    ("wrong-fop-trigger",      r"above\s*3\s*g\s*sugars", "FOP trigger is 10 g sugars / 30 mL (10% DV)"),
    ("civic-number-removed",   r"Civic house number\s*\*{0,2}\s*$|number\s+removed\*{0,2}\s+from the address",
                               "3820 is mandatory and stays"),
    ("old-coding-panel-size",  r"42\s*×\s*13\s*mm", "coding panel is 51 × 12.5 mm"),
    ("old-art-send-to-printer", r"(?!.*(SUPERSEDED|DO NOT)).*(SEND THIS TO THE PRINTER|Send the printer:\*\*\s*`Label_)",
                               "the July artwork must never be sent to a printer"),
    ("stale-pds-straddle",     r"78 to 105 cm", "PDS pinned at 60.2–94 cm², one band"),
]
# Context words that legitimise a forbidden match (before/after tables, supersession notes).
EXCUSE = re.compile(r"supersed|July artwork|previously|was wrong|~~|abandoned|prior version|"
                    r"old two-label|corrected|WRONG|historical|\| ~14\.5 \||"
                    r"existing artwork|artwork prints|artwork currently|must not print|"
                    r"is confirmed wrong|fix in the redraw|STALE|do not use", re.I)

# Facts that MUST appear somewhere in the named file.
REQUIRED = [
    ("JATEL_ProductSpec_v1.0_20260906.md", r"3820 Partridge Rd",           "farm address"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"V0H\s*1N1",                   "farm postal code"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"STATE AS ≤ 3\.5",              "pH of record (reverted once by an outside edit — keep asserting it)"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"351",                          "batch 2026-001 hue of record"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"coding panel",                 "coding panel, not printed dates"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"YYYYMMDD-nn",                 "lot format"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"NOT printed on the label",    "pH/Brix off-label decision"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"30 mL",                       "prescribed serving"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"rounding boundary",           "NFt sensitivity warning"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"3820 Partridge Rd", "farm address"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"51 × 12\.5 mm",  "coding panel size"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"coating knockout", "the ink-on-BOPP fix"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"REQUIRED",       "sugars symbol required"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"\*\*`benchandbloom\.com/recipes`\*\*", "QR to the general recipes page (2026-10-03)"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"Made in Canada", "origin claim"),
    # the front panel carries the origin claim; the qualifier is part of the claim, never optional
    ("singlelabel/redesign/BenchAndBloom_FrontPanel_v2.html",
     r"Made in Canada from domestic and imported ingredients", "qualified origin claim on the front (EN)"),
    ("singlelabel/redesign/BenchAndBloom_FrontPanel_v2.html",
     r"Fait au Canada avec des ingrédients canadiens et importés", "qualified origin claim on the front (FR)"),
    ("singlelabel/redesign/BenchAndBloom_FrontPanel_v2.html",
     r"Lavender grown on our Naramata estate", "lavender-origin claim on the front (EN)"),
    ("singlelabel/redesign/BenchAndBloom_FrontPanel_v2.html",
     r"Lavande cultivée sur notre domaine de Naramata", "lavender-origin claim on the front (FR)"),
]

fails = 0
def flag(msg):
    global fails; fails += 1; print(f"  [FLAG] {msg}")

print("="*76); print("SPEC CONSISTENCY"); print("="*76)
for rel in SPECS:
    p = ROOT / rel
    if not p.exists():
        flag(f"missing spec: {rel}"); continue
    lines = p.read_text().splitlines()
    for name, pat, why in FORBIDDEN:
        for i, line in enumerate(lines, 1):
            if re.search(pat, line, re.I) and not EXCUSE.search(line):
                flag(f"{rel}:{i}  {name} — {why}\n         {line.strip()[:100]}")
print("  forbidden-text scan complete")

for rel, pat, why in REQUIRED:
    p = ROOT / rel
    if not (p.exists() and re.search(pat, p.read_text(), re.I)):
        flag(f"{rel}  MISSING required fact: {why}  ({pat})")
print("  required-fact scan complete")

# ---- Front panel geometry, read straight from the source the PDF is printed from ----
print("="*76); print("FRONT PANEL GEOMETRY  (singlelabel/redesign/BenchAndBloom_FrontPanel_v2*.html)"); print("="*76)
INTER_CAP = 0.727          # Inter cap/numeral height as a fraction of font size (font metrics)
NET_MIN_MM = 3.2           # CPLR numeral height for a PDS > 32 to <= 258 cm²
PANEL_H = 63.5
for fn in ["BenchAndBloom_FrontPanel_v2.html", "BenchAndBloom_FrontPanel_v2_measured.html", "BenchAndBloom_FrontPanel_v3.html"]:
    p = ROOT / "singlelabel/redesign" / fn
    if not p.exists():
        flag(f"missing front panel source: {fn}"); continue
    css = p.read_text()
    def rule(sel):
        m = re.search(r"\." + re.escape(sel) + r"\{([^}]*)\}", css)
        return m.group(1) if m else ""
    def mm(sel, prop):
        m = re.search(prop + r":\s*([\d.]+)mm", rule(sel))
        return float(m.group(1)) if m else None
    net = mm("net", "font-size")
    if net is None:
        flag(f"{fn}: .net font-size not found")
    else:
        h = net * INTER_CAP
        ok = h >= NET_MIN_MM
        print(f"  [{'PASS' if ok else 'FLAG'}] {fn}: net quantity numerals {h:.2f} mm (font {net} mm) vs min {NET_MIN_MM} mm")
        if not ok: flag(f"{fn}: net quantity numerals below {NET_MIN_MM} mm")
    zones = ["z-fop", "z-lock", "z-name", "z-tast", "z-orig", "z-net"]
    hs = [mm(z, "height") for z in zones]
    if None in hs:
        flag(f"{fn}: zone heights missing: {[z for z,h in zip(zones,hs) if h is None]}")
    else:
        tot = sum(hs); ok = tot <= PANEL_H
        print(f"  [{'PASS' if ok else 'FLAG'}] {fn}: zones sum {tot:.1f} of {PANEL_H} mm")
        if not ok: flag(f"{fn}: zones overflow the panel")
        ok = hs[0] >= 18 and hs[0] <= PANEL_H / 2
        print(f"  [{'PASS' if ok else 'FLAG'}] {fn}: FOP zone {hs[0]} mm (>= 18 mm, within the upper half)")
        if not ok: flag(f"{fn}: FOP zone too small or outside the upper half")
    # Sugars symbol side inset: the clear buffer's outer edge must be >= 10% of the PDS width from the
    # left and right edges of the panel (LabelGenSpec v1.2 §5.2). Symbol 28.0 mm wide, buffer ~2.0 mm.
    PANEL_W, SYM_W, BUF = 63.2, 28.0, 2.0
    z = rule("z-fop")
    pad = re.search(r"padding:\s*([\d.]+)mm\s+([\d.]+)mm\s+([\d.]+)\s*(?:mm)?\s+([\d.]+)\s*(?:mm)?", z)
    pr = float(pad.group(2)) if pad else 0.0
    pl = float(pad.group(4)) if pad else 0.0
    if "justify-content:flex-end" in z:
        right_gap, left_gap = pr, PANEL_W - pr - SYM_W
    elif "justify-content:flex-start" in z:
        left_gap, right_gap = pl, PANEL_W - pl - SYM_W
    else:  # centred (the .zone default)
        left_gap = right_gap = (PANEL_W - pl - pr - SYM_W) / 2 + pl
    inset = min(left_gap, right_gap) - BUF
    ok = inset >= 0.10 * PANEL_W
    print(f"  [{'PASS' if ok else 'FLAG'}] {fn}: sugars symbol buffer {inset:.2f} mm from the nearer side edge (>= {0.10*PANEL_W:.2f} mm)")
    if not ok: flag(f"{fn}: sugars symbol buffer inside the 10% side margin")
    order = [css.find(f'class="zone {z}') for z in zones]
    ok = -1 not in order and order == sorted(order)
    print(f"  [{'PASS' if ok else 'FLAG'}] {fn}: zone order symbol > lockup > name > tasting > origin > net")
    if not ok: flag(f"{fn}: zone order changed or a zone is missing")
    bare = re.findall(r"Made in Canada(?! from)", css)
    ok = not bare
    print(f"  [{'PASS' if ok else 'FLAG'}] {fn}: no bare 'Made in Canada' ({len(bare)} found)")
    if not ok: flag(f"{fn}: bare Made in Canada claim")
    for bad in ["Product of Canada", "Produit du Canada", "Keep refrigerated", "per 15 mL", "Made in Canada from Canadian"]:
        if bad.lower() in css.lower():
            flag(f"{fn}: forbidden text on the front panel: {bad}")

# The printed QR encodes https://benchandbloom.com/recipes (static, no redirect service). Every printed
# label breaks if that page is renamed or removed, so its source must exist.
print("="*76); print("QR TARGET"); print("="*76)
qr_page = ROOT / "src/pages/recipes/index.astro"
ok = qr_page.exists()
print(f"  [{'PASS' if ok else 'FLAG'}] printed QR target page exists: {qr_page.relative_to(ROOT)} (serves /recipes)")
if not ok: flag("the page the printed QR points to (/recipes) is missing")

# ---- Print build vs specs: the QR target and the symbol placement must agree everywhere ----
print("="*76); print("PRINT BUILD CONSISTENCY  (spec v1.2, printer spec, singlelabel/v3 build)"); print("="*76)
gen = (ROOT / "JATEL_LabelGenSpec_v1.2_20261003.md").read_text()
build = (ROOT / "singlelabel/v3/build_wrap_v3.py").read_text()
prn = (ROOT / "singlelabel/Label_PrinterSpec_Wrap_uline2026.md").read_text()
m_spec = re.search(r"Encodes exactly \*\*`([^`]+)`\*\*", gen)
m_file = re.search(r'b64\(ART / "(JATEL_QR-[^"]+\.svg)"', build)
url_spec = m_spec.group(1) if m_spec else None
url_file = None
if m_file:
    t = re.search(r"<title>QR: ([^<]+)</title>", (ROOT / "singlelabel/artwork" / m_file.group(1)).read_text())
    url_file = t.group(1).strip() if t else None
m_prn = re.search(r"QR code\*\* \(left wing, beside the UPC\) → \*\*`([^`]+)`\*\*", prn)
url_prn = ("https://" + m_prn.group(1)) if m_prn else None
ok = url_spec is not None and url_spec == url_file == url_prn
print(f"  [{'PASS' if ok else 'FLAG'}] QR URL agrees: spec v1.2 {url_spec} | build file {m_file.group(1) if m_file else None} -> {url_file} | printer spec {url_prn}")
if not ok: flag("QR URL differs between the generation spec, the QR file used by the build, and the printer spec")
gap_build = re.search(r"FOP_RIGHT_GAP, FOP_BUF_SPEC = ([\d.]+), ([\d.]+)", build)
v3 = (ROOT / "singlelabel/redesign/BenchAndBloom_FrontPanel_v3.html").read_text()
gap_panel = re.search(r"\.z-fop\{[^}]*padding:\s*[\d.]+mm\s+([\d.]+)mm", v3)
ok = bool(gap_build and gap_panel) and float(gap_build.group(1)) == float(gap_panel.group(1))
print(f"  [{'PASS' if ok else 'FLAG'}] sugars symbol right gap: print build {gap_build.group(1) if gap_build else None} mm = panel of record {gap_panel.group(1) if gap_panel else None} mm")
if not ok: flag("sugars symbol position in the print build differs from FrontPanel_v3")
nm = re.search(r"^N=(\S+)", (ROOT / "singlelabel/v3/render_v3.sh").read_text(), re.M)
missing = [suf for suf in ["_print.pdf", "_600dpi.png", "_600dpi.jpg", "_CMYK_600dpi.tif", "_dieline.pdf", "_PROOF-guides.png"]
           if not nm or not (ROOT / "singlelabel/v3" / f"{nm.group(1)}{suf}").exists()]
ok = bool(nm) and not missing
print(f"  [{'PASS' if ok else 'FLAG'}] current print files present for {nm.group(1) if nm else None}" + (f" (missing {missing})" if missing else ""))
if not ok: flag("current print files missing")

print(f"\n{fails} FLAG(s).")
sys.exit(1 if fails else 0)
