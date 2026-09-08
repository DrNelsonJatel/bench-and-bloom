# Bench & Bloom — Label redesign (front panel v2)

**Document:** JATEL_LabelRedesign_v1.0_20260908
**Why:** the mandatory front-of-package sugars symbol does not fit the July layout. This records what
changed, why, and what is still open.
**Artwork:** `singlelabel/redesign/` · **Symbol:** `singlelabel/fop-symbol/5.6(BH).eps`

---

## 1. What forced the redesign

The product was reformulated to 11:5 acidified syrup, which triggers Health Canada's
**"High in sugars / Élevé en sucres"** symbol at 26% DV against a 10% threshold. That symbol is:

- **mandatory**, and cannot be redrawn — it must be the official EPS;
- **fixed in size** at **2.80 × 1.42 cm** for our PDS band (> 30 to ≤ 100 cm²); and
- **fixed in placement** — the upper half of the principal display panel, because PDP height ≥ width.

The upper half of the front panel is exactly where the brand lockup sat. **The symbol's placement is
prescribed; the lockup's is not.** So the lockup moves. This is not a style decision.

## 2. The one design move: the lockup goes horizontal

**Before:** a *stacked* lockup — sprig above the wordmark above the descriptor. Roughly 1:1, and
tall.
**After:** a *horizontal* lockup — sprig at the left, wordmark and descriptor stacked to its right.
Roughly 4:1, and short.

**The reasoning is purely dimensional.** The panel is short on height and long on width: after the
symbol takes 18 mm of vertical space, the remaining budget is tight vertically and has **18.6 mm to
spare horizontally**. A horizontal lockup spends the surplus and protects the scarcity. Nothing about
the mark, the wordmark, the typefaces or the palette changes — only the arrangement.

| | Stacked (v1) | Horizontal (v2) |
|---|---|---|
| Envelope | ~24 × 24 mm | **54 × 15 mm** |
| Vertical cost | ~24 mm | **15 mm** |
| Sprig | 40 × 52 units, above | same, at left, 8.4 × 10.9 mm |
| Wordmark | Fraunces 700 | Fraunces 700, 5.7 mm |
| Descriptor | Inter tracked caps | Inter 600, 1.58 mm, tracked 0.15 em |

The stacked lockup is **not retired** — it stays correct for the website, the seal sticker and
anywhere with vertical room. This is a label-specific variant.

## 3. The new front panel, zone by zone

Panel **63.2 × 63.5 mm** (front third of the 7.25 in wrap), ground Chalk White `#F7F3EE`.

| From | To | Zone | Status |
|---|---|---|---|
| 0.0 | 18.0 | **FOP sugars symbol + buffer** | **mandatory, prescribed position** |
| 18.0 | 33.0 | **Brand lockup (horizontal)** | redesigned |
| 33.0 | 47.0 | Common name, EN then FR | mandatory |
| 47.0 | 54.0 | Tasting line | optional |
| 54.0 | 62.0 | Net quantity, 250 mL (8.45 fl oz) | mandatory, min 3.2 mm type |

**62.0 of 63.5 mm used, 1.5 mm spare.** There is no slack. Anything added to the front panel has to
displace something already there.

The symbol clears the CPLR edge rule comfortably: its buffer sits **32 mm** wide inside a **50.6 mm**
window (10% of PDS inset each side), leaving 18.6 mm spare. **The constraint is vertical, not
horizontal** — which is why the lockup change works.

## 4. Copy on the panel

```
Lavender Syrup                    ← Fraunces, EN common name
Sirop à la lavande                ← Inter, FR common name
Small batch · estate lavender · Naramata Bench
Grosso lavender + butterfly pea · earthy and warm
250 mL (8.45 fl oz)               ← dual declaration, metric first
```

"earthy and warm" replaces the retired blue-to-pink colour hook and matches the site. No sugars-related
nutrient content claim appears, which is **required**: with the symbol on the PDP, all such claims are
prohibited there except "reduced in sugar".

## 5. Files

| File | Use |
|---|---|
| `redesign/BenchAndBloom_FrontPanel_v2.pdf` | Front panel at exact size, 63.2 × 63.5 mm |
| `redesign/BenchAndBloom_FrontPanel_v2_measured.pdf` | Same with zone rules and mm marks, for the designer |
| `redesign/BenchAndBloom_Lockup_Horizontal_v2.pdf` | The lockup alone |
| `redesign/*.png` | Screen previews |
| `redesign/*.html` | Editable sources, fonts embedded base64 |
| `fop-symbol/5.6(BH).eps` | **The real symbol. Swap it in for the preview raster before print.** |

## 6. ⚠️ What this is not

**This is the front panel only, and the symbol in it is a raster proxy.** The mockup uses a PNG
cropped from the Compendium so the layout could be measured. **The production file must place the
official `5.6(BH).eps` vector at exactly 2.80 × 1.42 cm.** Do not print from these previews.

**The two wings are not redrawn.** The right wing (Nutrition Facts, ingredients, storage) and the
left wing (story, coding panel, address, origin, UPC, QR) still need rebuilding against
`Label_PrinterSpec_Wrap_uline2026.md` v2.0. The right wing is the tighter of the two at 94% committed,
because the Nutrition Facts table alone is 1,596 mm².

## 7. Open before this can go to print

1. **The reference amount.** U.15 vs U.14, with Health Canada since 2026-09-06, ~2 weeks. It sets the
   serving size and therefore the whole Nutrition Facts table. **Nothing final can be drawn first.**
2. **Measure the Brix.** The declared sugars sits 0.19 g from a rounding boundary; 64 °Brix declares
   25 g, not 26 g.
3. **Confirm the PDS basis** with AskCFIA. Not blocking — both readings land in the same size band.
4. **Measure the symbol's x-height** to fix the buffer. I estimated 2 mm; it sets the 18 mm zone.
5. **Professional French verification**, still outstanding.
