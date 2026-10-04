"""Bench & Bloom Nutrition Facts table, Health Canada Bilingual Simplified Standard Format,
Figure 6.1(B), built on the Figure 1.1(E) base specifications.

Spec sources (Directory of Nutrition Facts Table Formats, canada.ca, read 2026-10-03):
  box 0.5 pt rule within 3 pt of text; heading 13 pt bold (FR line 14 pt leading);
  serving 9 pt / 11 pt leading (FR line 10 pt); Calories 10 pt bold / 14.5 pt leading;
  %DV subheading 6 pt bold, FR line 6.5 pt leading; nutrients 8 pt, non-indented bold name +
  regular amount, indented regular; thin rule 0.5 pt, thick 2.5 pt; footnotes 6 pt condensed,
  7 pt leading (no rule) / 10 pt (thin rule above) / 13 pt (thick rule above);
  " / " between English and French terms.
ASSUMED (not stated in the text read): 11 pt nutrient leading under a thin rule, 13.5 pt under
a thick rule, 1 pt rule under the serving size, 6 pt sub-nutrient indent. Verify against the
Figure 6.1(B) drawing before print.
"""
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = "/System/Library/Fonts/Supplemental/"
for n, f in [("A", "Arial.ttf"), ("AB", "Arial Bold.ttf"),
             ("AN", "Arial Narrow.ttf"), ("ANB", "Arial Narrow Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(n, F + f))

# ---- values of record (JATEL_ProductSpec §5.2; Health Canada U.15 confirmation 2026-09-17) ----
NFT = dict(calories=100, fat_g=0, fat_dv=0, carb_g=26, sugars_g=26, sugars_dv=26, protein_g=0)
NS_EN = ("Not a significant source of saturated fat, trans fat, fibre, cholesterol, "
         "sodium, potassium, calcium or iron.")
NS_FR = ("Source négligeable de lipides saturés, lipides trans, fibres, cholestérol, "
         "sodium, potassium, calcium et fer.")

import os
FIG = os.environ.get("FIG", "6.1")
S = dict(h=13, hl=14.0, sv=9, svl=10.0, cal=10, calL=14.5, nut=8, nl=11.0, nlk=13.5, ind=6.0, width=52.0) if FIG == "6.1" else \
    dict(h=9, hl=10.0, sv=8, svl=9.0, cal=9, calL=14.5, nut=7, nl=9.5, nlk=12.0, ind=5.0, width=46.0)
MM = 72 / 25.4
W = S["width"] * MM          # outer box width
INSET = 3.0            # text within 3 pt of the box rule
BOX = 0.5
X0, X1 = INSET, W - INSET
w = lambda t, f, s: pdfmetrics.stringWidth(t, f, s)

def wrap(text, font, size, width):
    out, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if w(trial, font, size) <= width: line = trial
        else: out.append(line); line = word
    return out + [line]

# ---- build a display list top-down; y = distance below the top text edge ----
ops, y = [], 0.0
def text(t, font, size, lead, x=None, right=False):
    global y
    y += lead
    ops.append(("t", t, font, size, y, x, right))
def text_same(t, font, size, x=None, right=False):
    ops.append(("t", t, font, size, y, x, right))
def rule(weight, below):
    ops.append(("r", weight, y + below))

text("Nutrition Facts", "AB", S["h"], S["h"] * 0.85)
text("Valeur nutritive", "AB", S["h"], S["hl"])
text("Per 30 mL (2 tbsp)", "A", S["sv"], S["sv"] + 2)
text("pour 30 mL (2 c. à soupe)", "A", S["sv"], S["svl"])
rule(1.0, S["sv"] * 0.212 + 0.6)
serv_rule = y + S["sv"] * 0.212 + 0.6
# Calories line with the two-line %DV subheading right-aligned, bottom line on the Calories baseline
y += S["calL"]
cal_y = y
ops.append(("t", f"Calories {NFT['calories']}", "AB", S["cal"], cal_y, None, False))
ops.append(("t", "% Daily Value*", "AB", 6, cal_y - 6.5, None, True))
ops.append(("t", "% valeur quotidienne*", "AB", 6, cal_y, None, True))
rule(2.5, 3.6)

def nutrient(name, amount, dv=None, indent=False, lead=None, thin_after=True):
    global y
    y += S["nl"] if lead is None else lead
    nx = X0 + (S["ind"] if indent else 0)
    ops.append(("n", name, amount, dv, indent, y, nx))
    if thin_after: rule(0.5, 2.6)

nutrient("Fat / Lipides", f"{NFT['fat_g']} g", f"{NFT['fat_dv']} %", lead=S["nlk"])
nutrient("Carbohydrate / Glucides", f"{NFT['carb_g']} g")
nutrient("Sugars / Sucres", f"{NFT['sugars_g']} g", f"{NFT['sugars_dv']} %", indent=True)
nutrient("Protein / Protéines", f"{NFT['protein_g']} g", thin_after=False)
rule(2.5, 3.6)

ns = wrap(NS_EN + " / " + NS_FR, "AN", 6, X1 - X0)
for i, ln in enumerate(ns):
    text(ln, "AN", 6, 13.0 if i == 0 else 7.0)
rule(0.5, 2.4)
# %DV footnote: 'a little', 'a lot', 'peu', 'beaucoup' in bold
FOOT = [[("*5% or less is ", "AN"), ("a little", "ANB"), (", 15% or more is ", "AN"), ("a lot", "ANB")],
        [("*5% ou moins c'est ", "AN"), ("peu", "ANB"), (", 15% ou plus c'est ", "AN"), ("beaucoup", "ANB")]]
for i, runs in enumerate(FOOT):
    y += 10.0 if i == 0 else 7.0
    ops.append(("runs", runs, 6, y))

H = y + 2.0 + INSET   # descender clearance + inset to the box
OUT_H = H

def render(path):
    c = canvas.Canvas(path, pagesize=(W, OUT_H), initialFontName="A", initialFontSize=8)
    c.setTitle(f"Bench & Bloom Nutrition Facts, Figure {FIG}(B) bilingual simplified")
    c.setFillColorRGB(1, 1, 1); c.rect(0, 0, W, OUT_H, stroke=0, fill=1)
    c.setFillColorRGB(0, 0, 0); c.setStrokeColorRGB(0, 0, 0)
    top = OUT_H - INSET
    for op in ops:
        if op[0] == "t":
            _, t, f, s, yy, x, right = op
            c.setFont(f, s)
            if right: c.drawRightString(X1, top - yy, t)
            else: c.drawString(X0 if x is None else x, top - yy, t)
        elif op[0] == "r":
            _, wt, yy = op
            c.setLineWidth(wt); c.line(BOX, top - yy, W - BOX, top - yy)
        elif op[0] == "n":
            _, name, amount, dv, indent, yy, nx = op
            nf = "A" if indent else "AB"
            n = S["nut"]
            c.setFont(nf, n); c.drawString(nx, top - yy, name)
            c.setFont("A", n); c.drawString(nx + w(name, nf, n) + w(" ", "A", n), top - yy, amount)
            if dv: c.drawRightString(X1, top - yy, dv)
        elif op[0] == "runs":
            _, runs, s, yy = op
            x = X0
            for t, f in runs:
                c.setFont(f, s); c.drawString(x, top - yy, t); x += w(t, f, s)
    c.setLineWidth(BOX); c.rect(BOX / 2, BOX / 2, W - BOX, OUT_H - BOX, stroke=1, fill=0)
    c.showPage(); c.save()

if __name__ == "__main__":
    import sys
    render(sys.argv[1])
    # QAQC: the %DV subheading cap tops must clear the rule under the serving size (+0.5 pt)
    dv_top = cal_y - 6.5 - 6 * 0.72
    print(f"QAQC %DV subheading clears serving rule by {dv_top - (serv_rule + 0.5):.2f} pt:", "PASS" if dv_top > serv_rule + 0.5 else "FLAG")
    print(f"NFt size: {W/MM:.2f} x {OUT_H/MM:.2f} mm = {W/MM*OUT_H/MM:.0f} mm2; NS lines {len(ns)}")
    # QAQC: every text line fits inside the 3 pt inset
    worst = max(w(ln, "AN", 6) for ln in ns)
    print("QAQC NS statement within inset:", "PASS" if worst <= X1 - X0 + 1e-6 else "FLAG")
    for runs in FOOT:
        fw = sum(w(t, f, 6) for t, f in runs)
        print(f"QAQC footnote width {fw:.1f} of {X1-X0:.1f} pt:", "PASS" if fw <= X1 - X0 else "FLAG")
    widest = max(w("Carbohydrate / Glucides", "AB", 8) + w(" 26 g", "A", 8),
                 6 + w("Sugars / Sucres", "A", 8) + w(" 26 g", "A", 8) + w("26 %", "A", 8) + 6)
    print(f"QAQC widest nutrient line {widest:.1f} of {X1-X0:.1f} pt:", "PASS" if widest <= X1 - X0 else "FLAG")
