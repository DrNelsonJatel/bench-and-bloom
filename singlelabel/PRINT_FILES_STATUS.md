# ⚠️ PRINT FILES STATUS — read before sending anything to a printer

**Updated 2026-07-02** for the reformulated **1:5 (~14.5 °Brix), refrigerated** product.

## Current (authoritative, edited)
- ✅ `Label_benchandbloom_Final_uline2026_Wrap.svg` — the editable master. **Source of truth.**
- ✅ `Label_PrinterSpec_Wrap_uline2026.md` — the spec.
- ✅ `../brand/labels/Label_benchandbloom_Final_uline2026_Back.svg` — legacy 2-panel back, kept in sync.

## STALE — must be re-exported from the master before printing
These are rasters/outlined derivatives that still show the **OLD** values
(50 cal / 12 g sugars, "Refrigerate after opening", sugar-first ingredients):
- ❌ `Label_benchandbloom_PRINTREADY_uline2026.svg` (outlined)
- ❌ `Label_benchandbloom_PRINTREADY_uline2026_600dpi.png`
- ❌ `Label_benchandbloom_Final_uline2026_Wrap.png`
- ❌ `Label_benchandbloom_Final_uline2026_Wrap.jpg`

## What changed in the master
| Field | Old | New |
|---|---|---|
| Calories / 15 mL | 50 | **10** |
| Carbohydrate | 12 g | **2 g** |
| Sugars | 12 g (12% DV) | **2 g (2% DV)** |
| Ingredients order | Sugar, water, … | **Water, sugar, …** (water leads at 1:5) |
| Storage | Refrigerate after opening | **Keep refrigerated / Garder au froid** |
| Best before | 2027 07 01 (12 mo) | **2026 10 01 (~3 mo, refrigerated)** |
| FOP "High in sugars" | required-but-omitted | **not required** (~8% DV < 15% trigger) |

## Re-export steps (needs Inkscape or Illustrator — not available in this environment)
1. Open `Label_benchandbloom_Final_uline2026_Wrap.svg`.
2. **Outline fonts:** Select All → `Path > Object to Path` → Save As `…_PRINTREADY_…svg`.
3. Export raster: `…_600dpi.png` (600 dpi), plus the preview `.png` / `.jpg`.
4. Delete this file's ❌ entries once regenerated, or update the dates here.
