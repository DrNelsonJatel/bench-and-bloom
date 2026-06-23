# Bench & Bloom — Label Printer Spec (uline2026)

Hand this, plus the two SVGs, to the label printer (StickerYou / Jukebox / Avery WePrint, etc.).

## The bottle
- **Uline S-23397** — 8 oz Clear Boston Round glass, neck finish 28-400.
- Height 5.437″ · body diameter 2.375″ · circumference 7.46″ · **label panel 3.125″ tall.**
- Tamper band: Uline S-17668 black shrink band (55 × 28 mm) over the cap/neck (above the label).

## Label size  (front + back, two labels — leaves side windows so the blue syrup shows)
- **Trim: 2.5″ W × 2.75″ H** each.
- **Bleed: 0.125″** all sides → **artwork/cut sheet 2.75″ × 3.0″.**
- **Safe margin: 0.125″** inside trim (keep all text/logo inside).
- Files are built at this size. The **magenta dashed line = trim, cyan dashed = safe.**
  **Delete the `#guides` layer before printing** (or tell the printer they are non-printing guides).
- Two labels sit on opposite faces; ~1.2″ of glass shows on each side (intentional — the colour-change
  syrup is the feature). If you prefer a single wrap instead, it would be ~7.25″ × 2.75″ (hides syrup).

## Files
- `Label_benchandbloom_Final_uline2026_Front.svg`
- `Label_benchandbloom_Final_uline2026_Back.svg`
- Vector SVG, fonts referenced by name (see below) — **outline the fonts** before sending to print,
  or supply the fonts. The mark + colour fields are already vector.

## Print specs
- **Colour: CMYK.** Values:
  - Lavender (Dark Denim) `#5A4A78` → C25 M38 Y0 K53
  - Chalk White ground `#F7F3EE` → C0 M2 Y4 K3
  - Onyx text `#2D2933` → C12 M20 Y0 K80
  - Gold rule `#C2A05E` → C22 M31 Y70 K4 · Sprig accent `#7E6FA0` · Sage stem `#8A9A78`
- **Resolution:** vector (infinite); any raster ≥ 300 dpi.
- **Stock:** premium **cream / soft-matte BOPP film** (waterproof — fridge + wet). Permanent,
  glass-rated adhesive. No glossy white.
- **Finish:** matte laminate recommended (durability + premium feel).
- **Fonts:** Fraunces (wordmark + "Lavender Simple Syrup") and Inter (everything else). Both free
  (Google Fonts / SIL OFL). Outline before print.

## Application
- Front and back centred on opposite faces, sitting within the 3.125″ straight panel
  (≈ 0.19″ clearance top and bottom at 2.75″ tall).
- Apply the shrink band over the cap + neck and heat to set (tamper evidence for Amazon).

## Before you print — [VERIFY] with CFIA Industry Labelling Tool (free)
- Nutrition Facts table (placeholder box on back) — likely required; may qualify for the small-supplier
  exemption. If required, insert the calculated table (per 15 mL serving).
- Front-of-pack "High in sugars / Élevé en sucres" symbol — confirm whether it applies.
- French copy professionally verified (it is draft here).
- Real civic address filled into "Prepared for / Préparé pour".
- UPC barcode placed in the box (needed for Amazon FBA).
- Net-quantity type height confirmed for the panel area.
