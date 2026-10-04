#!/usr/bin/env python3
"""Bench & Bloom 250 mL wrap label, v3 (2026-10-03).

Base: the ChatGPT render the owner chose for its front-panel imagery
(source/JATEL_ChatGPTBase_v1.0_20261003.png). The watercolour lockup, the title, the tasting
lines and the net quantity are lifted from it; everything else is rebuilt to
JATEL_LabelGenSpec_v1.1_20261003 with the committed artwork in singlelabel/artwork/.

Writes Label_BenchAndBloom_Wrap_v3.html (the master) and runs a layout QAQC inside Chrome.
Render the outputs with render_v3.sh.
"""
import base64, json, pathlib
from PIL import Image, ImageFilter

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SRC = HERE / "source" / "JATEL_ChatGPTBase_v1.0_20261003.png"
ART = ROOT / "singlelabel" / "artwork"
FONTS = ROOT / "node_modules" / "@fontsource"
OUT = HERE / "build"
OUT.mkdir(exist_ok=True)

BLEED = 3.175
TRIM_W, TRIM_H = 184.15, 69.85
DOC_W, DOC_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED
SAFE = 3.175
DPI = 600
GROUND = "#F7F3EE"
ONYX = "#2D2933"
GOLD = "#C2A05E"

base = Image.open(SRC).convert("RGB")
BW, BH = base.size
MM_PER_PX = ((TRIM_W / BW) + (TRIM_H / BH)) / 2      # base is drawn at trim size, no bleed

def crop(name, box, scale, blank=None):
    """Crop a base region, optionally blanking a sub-box to ground, upscale to 600 dpi at its
    placed size. Returns (path, width_mm, height_mm)."""
    im = base.crop(box)
    if blank:
        bx0, by0, bx1, by1 = blank
        im.paste((247, 243, 238), (bx0 - box[0], by0 - box[1], bx1 - box[0], by1 - box[1]))
    w_mm = (box[2] - box[0]) * MM_PER_PX * scale
    h_mm = (box[3] - box[1]) * MM_PER_PX * scale
    px_w = round(w_mm / 25.4 * DPI); px_h = round(h_mm / 25.4 * DPI)
    im = im.resize((px_w, px_h), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    p = OUT / f"{name}.png"; im.save(p, dpi=(DPI, DPI))
    return p, w_mm, h_mm

# Front-panel pieces (base pixel boxes measured 2026-10-03). Scales keep the mandatory French
# common name at >= 1.6 mm "o" (base 'o' ~2.08 mm -> 0.8 gives 1.66 mm) and the net quantity
# numerals at >= 3.2 mm (base ~3.6 mm -> 0.95 gives ~3.4 mm).
S_LOCK, S_TITLE, S_TAST, S_NET = 0.72, 0.80, 0.80, 0.95
lock = crop("lockup", (664, 108, 1346, 330), S_LOCK, blank=(818, 0, 1200, 152))
title = crop("title", (742, 346, 1326, 488), S_TITLE)
tast = crop("tasting", (703, 504, 1343, 573), S_TAST)
net = crop("netqty", (788, 688, 1249, 749), S_NET)

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font(face, weight, file):
    return f"@font-face{{font-family:{face};font-weight:{weight};src:url({b64(file,'font/woff2')}) format('woff2')}}"

fonts = "\n".join([
    font("In", 400, FONTS / "inter/files/inter-latin-400-normal.woff2"),
    font("In", 500, FONTS / "inter/files/inter-latin-500-normal.woff2"),
    font("In", 600, FONTS / "inter/files/inter-latin-600-normal.woff2"),
    font("In", 700, FONTS / "inter/files/inter-latin-700-normal.woff2"),
])

T = lambda v: v + BLEED   # trim coordinate -> document coordinate

# ---------------- FRONT PANEL (trim x 60.5..123.7) ----------------
FX0, FX1 = 60.5, 123.7
FCX = (FX0 + FX1) / 2
FOP_W, FOP_H, FOP_BUF = 28.0, 14.2, 1.1         # 5.6(BH), PDS band >30 to <=100 cm2
y = SAFE + FOP_BUF
front = []
front.append(("fop", FCX - FOP_W / 2, y, FOP_W, FOP_H, b64(ART / "JATEL_FOPSymbol-Sugars-5.6BH_v1.0_20261003.svg", "image/svg+xml")))
y += FOP_H + FOP_BUF
GAP = 0.5
y += GAP
for name, (p, w, h) in [("lockup", lock), ("title", title), ("tasting", tast)]:
    front.append((name, FCX - w / 2, y, w, h, b64(p, "image/png")))
    y += h + GAP
y += 0.3
ORIG_TOP = y
ORIG_LINES = ["Made in Canada from domestic and imported ingredients",
              "Fait au Canada avec des ingrédients canadiens et importés",
              "Lavender grown on our Naramata estate",
              "Lavande cultivée sur notre domaine de Naramata"]
ORIG_SIZE, ORIG_LH = 1.8, 1.2
y += len(ORIG_LINES) * ORIG_SIZE * ORIG_LH + 0.9
p, w, h = net
front.append(("netqty", FCX - w / 2, y, w, h, b64(p, "image/png")))
FRONT_BOTTOM = y + h

# ---------------- RIGHT WING (trim x 125.2..180.975) ----------------
RX0, RX1 = 125.2, TRIM_W - SAFE
NFT_W, NFT_H = 46.0, 52.09
nft_x = RX0 + ((RX1 - RX0) - NFT_W) / 2
STOR_TOP = SAFE + NFT_H + 1.6

# ---------------- LEFT WING (trim x 3.175..59.0) ----------------
LX0, LX1 = SAFE, 59.0
UPC_W, UPC_H = 42.735 * 0.8, 24.956 * 0.8      # 80% magnification
QR = 13.0
ROW_TOP = TRIM_H - SAFE - UPC_H

css = f"""
{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
@page{{size:{DOC_W}mm {DOC_H}mm;margin:0}}
html,body{{width:{DOC_W}mm;height:{DOC_H}mm;background:{GROUND}}}
.doc{{position:relative;width:{DOC_W}mm;height:{DOC_H}mm;background:{GROUND};overflow:hidden;font-family:In,sans-serif;color:{ONYX}}}
.a{{position:absolute}}
.rule{{position:absolute;width:0.3mm;background:{GOLD}}}
.mand{{font-size:2.95mm;line-height:3.5mm;font-weight:500}}          /* x-height 1.61 mm (Inter 0.546) */
.code{{background:#FFFFFF}}
.cap{{font-size:2.2mm;font-weight:600;letter-spacing:.02em}}           /* caps height 1.60 mm (Inter 0.727) */
.ing{{border:0.25mm solid #000;padding:0.8mm 1.0mm;color:#000;font-weight:400;font-size:2.05mm;line-height:2.5mm}} /* x-height 1.12 mm */
.ing b{{font-weight:700}}
.ing p+p{{margin-top:0}}
.orig{{font-size:{ORIG_SIZE}mm;line-height:{ORIG_SIZE*ORIG_LH}mm;font-weight:500;text-align:center;color:{ONYX}}}
.small{{font-size:1.8mm;line-height:2.2mm;font-weight:500;color:#5A5266}}
.guides .g{{position:absolute;border:0.15mm dashed}}
"""

def img(cls, x, y, w, h, src, extra=""):
    return f'<img class="a {cls}" id="{cls}" src="{src}" style="left:{T(x):.3f}mm;top:{T(y):.3f}mm;width:{w:.3f}mm;height:{h:.3f}mm" {extra}>'

body = []
# panel rules
body.append(f'<div class="rule" style="left:{T(FX0)-0.15:.3f}mm;top:{T(SAFE):.3f}mm;height:{TRIM_H-2*SAFE:.3f}mm"></div>')
body.append(f'<div class="rule" style="left:{T(FX1)-0.15:.3f}mm;top:{T(SAFE):.3f}mm;height:{TRIM_H-2*SAFE:.3f}mm"></div>')
for (cls, x, yy, w, h, src) in front:
    body.append(img(cls, x, yy, w, h, src))
body.append(f'<div class="a orig" id="origin" style="left:{T(FX0):.3f}mm;top:{T(ORIG_TOP):.3f}mm;width:{FX1-FX0:.3f}mm">' + "<br>".join(ORIG_LINES) + "</div>")

# right wing
body.append(img("nft", nft_x, SAFE, NFT_W, NFT_H, b64(ART / "JATEL_NutritionFacts-Fig6.2B_v1.0_20261003.svg", "image/svg+xml")))
body.append(f'<div class="a mand" id="storage" style="left:{T(nft_x):.3f}mm;top:{T(STOR_TOP):.3f}mm;width:{RX1-nft_x:.3f}mm">Refrigerate after opening /<br>Réfrigérer après ouverture</div>')

# left wing: coding panel, dealer, ingredients, codes
body.append(f'<div class="a code" id="coding" style="left:{T(LX0):.3f}mm;top:{T(SAFE):.3f}mm;width:51mm;height:12.5mm">'
            f'<div class="a cap" style="left:1mm;top:1mm">BEST BEFORE / MEILLEUR AVANT</div>'
            f'<div class="a cap" style="left:1mm;top:8.6mm">LOT</div></div>')
DEALER_TOP = SAFE + 12.5 + 1.4
body.append(f'<div class="a mand" id="dealer" style="left:{T(LX0):.3f}mm;top:{T(DEALER_TOP):.3f}mm;width:{LX1-LX0:.3f}mm">'
            '<span style="font-weight:600">Prepared by / Préparé par:</span><br>Bench &amp; Bloom, 3820 Partridge Rd,<br>'
            'Naramata, BC, Canada V0H 1N1<br>BenchandBloom.com</div>')
body.append(f'<div class="a ing" id="ingredients" style="left:{T(LX0):.3f}mm;width:{LX1-LX0:.3f}mm;top:0mm">'
            '<p><b>Ingredients:</b> Sugar, water, lavender (Lavandula), citric acid, butterfly pea flower (Clitoria ternatea).</p>'
            '<p><b>Ingrédients :</b> Sucre, eau, lavande (Lavandula), acide citrique, fleur de pois bleu (Clitoria ternatea).</p></div>')
body.append(img("upc", LX0, ROW_TOP, UPC_W, UPC_H, b64(ART / "JATEL_UPC-627146286305_100pct_v1.0_20261003.svg", "image/svg+xml")))
qr_x = LX1 - QR
body.append(img("qr", qr_x, ROW_TOP, QR, QR, b64(ART / "JATEL_QR-LavenderMilk_v1.0_20261003.svg", "image/svg+xml")))
body.append(f'<div class="a small" id="qrcap" style="left:{T(qr_x):.3f}mm;top:{T(ROW_TOP+QR+0.6):.3f}mm;width:{QR:.3f}mm;text-align:center">Recipes<br>Recettes</div>')

# guides (only shown with ?guides)
g = []
g.append(f'<div class="g" style="border-color:#c08;left:0;top:0;width:{DOC_W}mm;height:{DOC_H}mm"></div>')
g.append(f'<div class="g" style="border-color:#000;left:{BLEED}mm;top:{BLEED}mm;width:{TRIM_W}mm;height:{TRIM_H}mm"></div>')
g.append(f'<div class="g" style="border-color:#0aa;left:{T(SAFE)}mm;top:{T(SAFE)}mm;width:{TRIM_W-2*SAFE}mm;height:{TRIM_H-2*SAFE}mm"></div>')
g.append(f'<div class="g" style="border-color:#2a2;left:{T(LX0)}mm;top:{T(SAFE)}mm;width:51mm;height:12.5mm"></div>')

qa = f"""
const MM = 96/25.4, T = v => v + {BLEED};
const r = id => {{ const e = document.getElementById(id).getBoundingClientRect();
  return {{x0: e.left/MM - {BLEED}, y0: e.top/MM - {BLEED}, x1: e.right/MM - {BLEED}, y1: e.bottom/MM - {BLEED}}}; }};
// place the ingredient box between the dealer block and the code row, centred in the gap
const d = r('dealer'), ing = document.getElementById('ingredients');
const ih = ing.getBoundingClientRect().height/MM, gapTop = d.y1, gapBot = {ROW_TOP};
ing.style.top = (T(gapTop + ((gapBot - gapTop) - ih)/2)) + 'mm';
const ids = ['fop','lockup','title','tasting','origin','netqty','nft','storage','coding','dealer','ingredients','upc','qr','qrcap'];
const R = Object.fromEntries(ids.map(i => [i, r(i)]));
const out = {{boxes: R, checks: []}};
const safe = {{x0:{SAFE}, y0:{SAFE}, x1:{TRIM_W-SAFE}, y1:{TRIM_H-SAFE}}};
for (const i of ids) {{ const b = R[i];
  out.checks.push([`${{i}} inside safe area`, b.x0 >= safe.x0-0.01 && b.y0 >= safe.y0-0.01 && b.x1 <= safe.x1+0.01 && b.y1 <= safe.y1+0.01]); }}
const panel = {{front:[{FX0},{FX1}], left:[{LX0},{LX1}], right:[{RX0},{RX1}]}};
const where = {{fop:'front',lockup:'front',title:'front',tasting:'front',origin:'front',netqty:'front',nft:'right',storage:'right',coding:'left',dealer:'left',ingredients:'left',upc:'left',qr:'left',qrcap:'left'}};
for (const i of ids) {{ const [a,b] = panel[where[i]];
  out.checks.push([`${{i}} within its panel`, R[i].x0 >= a-0.01 && R[i].x1 <= b+0.01]); }}
const ov = (a,b) => a.x0 < b.x1 && b.x0 < a.x1 && a.y0 < b.y1 && b.y0 < a.y1;
for (let i=0;i<ids.length;i++) for (let j=i+1;j<ids.length;j++)
  if (ov(R[ids[i]], R[ids[j]])) out.checks.push([`overlap ${{ids[i]}} / ${{ids[j]}}`, false]);
// FOP buffer (1.1 mm) must be clear of every other element
const f = R.fop, fb = {{x0:f.x0-{FOP_BUF}, y0:f.y0-{FOP_BUF}, x1:f.x1+{FOP_BUF}, y1:f.y1+{FOP_BUF}}};
for (const i of ids) if (i!=='fop' && ov(fb, R[i])) out.checks.push([`FOP buffer intruded by ${{i}}`, false]);
out.checks.push(['FOP in upper half of the front panel', f.y1 <= {SAFE} + {TRIM_H-2*SAFE}/2]);
out.checks.push(['FOP >=10% inset from front-panel edges', f.x0-{FOP_BUF} >= {FX0}+0.1*{FX1-FX0} && f.x1+{FOP_BUF} <= {FX1}-0.1*{FX1-FX0}]);
const gaps = [['ingredients above code row', R.upc.y0 - R.ingredients.y1], ['dealer above ingredients', R.ingredients.y0 - R.dealer.y1],
  ['coding above dealer', R.dealer.y0 - R.coding.y1], ['origin above net qty', R.netqty.y0 - R.origin.y1], ['tasting above origin', R.origin.y0 - R.tasting.y1],
  ['nft above storage', R.storage.y0 - R.nft.y1], ['upc beside qr', R.qr.x0 - R.upc.x1]];
for (const [n,v] of gaps) out.checks.push([`${{n}}: ${{v.toFixed(2)}} mm clear (>= 0.8)`, v >= 0.8]);
out.ingredient_box_mm = [R.ingredients.x1-R.ingredients.x0, R.ingredients.y1-R.ingredients.y0];
document.getElementById('qa').textContent = JSON.stringify(out);
if (location.search.includes('guides')) document.getElementById('guides').style.display='block';
"""

html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Bench &amp; Bloom wrap v3</title><style>{css}</style></head>
<body><div class="doc">{''.join(body)}<div id="guides" class="guides" style="display:none">{''.join(g)}</div></div>
<pre id="qa" style="display:none"></pre><script>{qa}</script></body></html>"""
(HERE / "Label_BenchAndBloom_Wrap_v3.html").write_text(html, encoding="utf-8")
print(json.dumps({"doc_mm": [DOC_W, DOC_H], "front_bottom_mm": round(FRONT_BOTTOM, 2),
                  "front_safe_bottom_mm": TRIM_H - SAFE,
                  "pieces_mm": {n: [round(w, 2), round(h, 2)] for n, (_, w, h) in
                                [("lockup", lock), ("title", title), ("tasting", tast), ("netqty", net)]}}))
