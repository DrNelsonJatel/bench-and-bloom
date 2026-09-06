# PRINT FILES STATUS

> ## ⛔ SUPERSEDED 2026-09-06 — NOTHING IN THIS FOLDER IS PRINT-READY
>
> Every file below renders the **abandoned 1:5 refrigerated product**. The product was reformulated
> to an 11:5 acidified syrup and the artwork must be **redrawn, not reprinted**: new 30 mL nutrition
> table, mandatory front-of-pack sugars symbol, reordered ingredient list with citric acid, ruby not
> blue, "Refrigerate after opening", "Made in Canada from domestic and imported ingredients", and
> real dates.
>
> **Do not send any file in this folder to a printer.**
> Read `Label_PrinterSpec_Wrap_uline2026.md` (v2.0) and `JATEL_ProductSpec_v1.0_20260906.md` first.
>
> The **physical** spec below (trim, bleed, stock, fonts) is still correct and still applies.

---

## Historical status (as of 2026-07-02, retained for reference)

All label art regenerated for the reformulated **1:5 (~14.5 °Brix), refrigerated** product.
Rendered from the editable master via headless Chrome with the real **Inter + Fraunces**
fonts embedded, print guides removed. Visually verified.

## ❌ ~~Send these to the printer~~ — SUPERSEDED, DO NOT SEND
- **`Label_benchandbloom_Wrap_PRINTREADY_uline2026.pdf`** — **primary print deliverable.**
  7.5" × 3.0" (trim 7.25 × 2.75 + 0.125 bleed), fonts embedded (Inter + Fraunces subsets),
  guides removed. RGB (digital label printers handle RGB→CMYK; CMYK values are in the spec if
  a printer wants them).
- `Label_benchandbloom_PRINTREADY_uline2026_600dpi.png` — 4500 × 1800 (600 dpi) raster, for
  printers/editors that take PNG (e.g. StickerYou's online editor).
- `Label_benchandbloom_PRINTREADY_uline2026.svg` — self-contained SVG (Inter + Fraunces embedded
  as base64 @font-face, guides removed) — font-independent, editable fallback.

## ✅ Current (source + previews)
- `Label_benchandbloom_Final_uline2026_Wrap.svg` — editable master (source of truth).
- `Label_benchandbloom_Final_uline2026_Wrap.png` / `.jpg` — refreshed preview renders.
- `Label_PrinterSpec_Wrap_uline2026.md` — the spec (authoritative, current).

## ✅ Spec document
- `Label_PrinterSpec_Wrap_uline2026.md` — authoritative source.
- `Label_PrinterSpec_Wrap_uline2026.pdf` — regenerated 2026-07-02 from the `.md`
  (pandoc gfm → HTML → Chrome print-to-PDF, US Letter, 8pp). Now current.

## Verified label content (per 15 mL)
Calories 10 · Carbohydrate 2 g · Sugars 2 g (2% DV) · Fat/Protein/Sodium 0 ·
Ingredients water-first (Water, sugar, lavender, butterfly pea) · **Keep refrigerated /
Garder au froid** · Best before 2026 10 01 · GS1 627146286305 · QR intact.

## To regenerate (if the master changes again)
Builder script + steps are in the session scratchpad (`build_label.py`): embeds the woff2 fonts
from `node_modules/@fontsource/{inter,fraunces}`, strips `<g id="guides">`, wraps in HTML;
`Google Chrome --headless … --print-to-pdf` for the PDF; `qlmanage -t -s 4500 -o . <pdf>` to raster.
