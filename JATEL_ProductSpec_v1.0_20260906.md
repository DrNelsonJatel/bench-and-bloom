# Bench & Bloom Lavender Syrup: Product & Label Specification

**Document:** JATEL_ProductSpec_v1.0_20260906
**Status:** Authoritative product definition as of 2026-09-06. Supersedes the formulation, nutrition, storage and colour content in `build/BATCH_RECIPE_2026.md`, `build/LABEL_SPEC.md`, `build/LABEL_HANDOFF.md`, `brand/labels/Label_PrinterSpec_uline2026.md` and `singlelabel/Label_PrinterSpec_Wrap_uline2026.md`. Those five files describe the abandoned 1:5 refrigerated formulation and must not be used to generate label copy.
**Purpose:** Single input file for generating the first draft of a Canadian-compliant wrap label.
**Market:** Canada only (Amazon.ca and direct). A US variant is out of scope for this version.

## 1. What changed, and why this document exists

The product was reformulated from a 1:5 low-sugar refrigerated cordial to an 11:5 acidified, sugar-preserved syrup. Sugar concentration rose 5.9x. Every recipe-derived field on the July 2026 artwork is now wrong, and one new mandatory element (the front-of-package nutrition symbol) is now triggered. The label must be redrawn, not patched.

| Attribute | July 2026 label | Current product |
|---|---|---|
| Sugar : water (by volume) | 1 : 5 | **11 : 5** |
| Sucrose by mass | ~14.5 °Brix | **64 °Brix** |
| Acidulant | none | **citric acid, 0.53% w/v** |
| pH | ~7 | **~2.5** |
| Water activity | ~0.98 | **~0.85** |
| Shelf stability | refrigerated only | **ambient shelf-stable** |
| Colour in bottle | blue | **deep ruby / garnet red** |
| Colour hook | blue turns pink with citrus | **already red; hook is dead** |
| Front-of-package symbol | not required | **"High in sugars" REQUIRED** |

## 2. Product definition

- **Brand:** Bench & Bloom
- **Descriptor / house line:** NARAMATA BENCH BOTANICALS
- **Common name (bilingual, mandatory, PDP):** Lavender Syrup / Sirop à la lavande
- **Net quantity:** 250 mL (8.45 fl oz)
- **Container:** Uline S-23397, 8 oz clear Boston round glass, 28-400 neck finish
- **Appearance:** clear, deep ruby to garnet red syrup, viscous, no sediment
- **Flavour:** floral lavender forward, bright citric lift, sweet, not bitter and not soapy
- **Use:** flavouring syrup for cocktails, sparkling wine, lemonade, soda and coffee
- **Origin:** lavender grown and product made on the Naramata Bench, Naramata, BC

## 3. Formulation (1x batch)

| Ingredient | Amount | Approx. mass | Notes |
|---|---|---|---|
| Pure cane granulated sugar | 11 cups | 2,200 g | imported cane |
| Distilled water (Canadian) | 5 cups | 1,183 g | |
| Fresh Naramata farm lavender | 1 cup | ~50 g | *Lavandula* ×*intermedia* 'Grosso', estate grown, strained out |
| Citric acid | 1 tbsp | ~13.5 g | acidulant, remains in product |
| Butterfly pea flower, dried | 1 tbsp | ~2 g | *Clitoria ternatea*, sourced, strained out |

**Steep time: 3 minutes (LOCKED).** Confirmed by taste 2026-09-06: delicious, not bitter. This replaces the 5 / 8 / 12 minute taste-pull range in the old batch sheet. Do not lengthen it: the bud dose here is roughly 4x the previous recipe and Grosso is the camphorous end of the genus.

**Process order matters.** Dissolve sugar in water with heat, steep lavender 3 minutes off heat, strain, cool to ~75 to 80 °C, steep butterfly pea, strain, add citric acid, return to >= 85 °C, hot-fill into heat-sanitized bottles, cap and invert.

### 48-bottle pilot (12 L, scale factor 4.67x)

| Ingredient | Pilot quantity |
|---|---|
| Sugar | 51 cups (~10.3 kg) |
| Distilled water | 23 cups (~5.5 L) |
| Fresh lavender | 4.7 cups |
| Citric acid | 4.7 tbsp (~63 g) |
| Butterfly pea flower | 4.7 tbsp |

Dose scales with batch volume. **Steep time does not scale: hold it at 3 minutes.**

## 4. Derived physical and chemical properties

Calculated from the formulation and cross-checked against ICUMSA sucrose density tables.

| Property | Value | Basis |
|---|---|---|
| Sucrose by mass | 64 °Brix | 2,200 g sugar / 3,396 g total |
| Total soluble solids (refractometer) | ~65 °Brix | includes citric acid |
| Density | 1.316 g/mL | ICUMSA, 65 °Brix at 20 °C |
| Yield, 1x batch | 2.57 L (~10 x 250 mL bottles) | |
| Sugar concentration | 0.856 g/mL | |
| Citric acid concentration | 0.53% w/v | 13.5 g / 2,570 mL |
| pH | **STATE AS ≤ 3.5.** Colour proxy brackets **≤ 3.0**; stoichiometric estimate 2.34 | Two independent methods + margin, §4.1 |
| Water activity | ~0.85 (estimated) | 65 °Brix sucrose |
| Mass of a 250 mL fill | ~329 g syrup | up ~25% from the 1:5 version |

**Preservation:** sugar-preserved (>= 65 °Brix, a_w ~0.85) and acid-preserved (pH ~2.5), plus hot-fill into sanitized glass. This is an ambient shelf-stable product. It is not a refrigerated product and the label must not say "Keep refrigerated".

**Colour chemistry:** butterfly pea ternatins are blue near neutral pH and shift through purple to red below pH 3. At pH ~2.5 the syrup is permanently ruby red in the bottle. The blue-to-pink-with-citrus reveal is no longer possible and all copy describing it must be removed.

### 4.1 pH by colour — butterfly pea as its own indicator

The butterfly pea is a polyacylated anthocyanin (ternatin), a genuine pH indicator, so the syrup
reports its own pH. Working value until a meter reading exists.

**Batch 2026-001** (`Photos/BnB_Lavender Syrop.JPG`), measured with `tools/batch_colour_ph.py`:
35,503 qualifying pixels, median `#34020C`, **hue of record 351°** (spread 5.7°, R = 0.999),
saturation 0.96, clipping 0.00%.

Hue 351° sits in the **red / deep ruby** arc, bracketing **pH ≤ 3.0**. The stoichiometric estimate is
**2.34**, inside that bracket. **Two independent methods agree.**

> **Value of record: state pH as `≤ 3.5`**, carrying 0.5 of margin for proxy error.

Colour is a **poor pH meter and an excellent threshold indicator**. At pH 4–6 ternatins are purple,
hue 280–320°, and this reads 351°, so the product is emphatically not near pH 4. Limits: a backlit
sRGB JPEG is not colorimetry, and concentration deepens colour toward red independently of pH, so
**only the upper bound carries information**. Re-baseline on a protocol photo: white background,
**indirect** light, white-balance card, same fill.

---

## 5. Regulatory determinations (Canada)

### 5.1 Reference amount and serving size

The product is item **U.15** of the Health Canada Table of Reference Amounts for Food: *"Syrups used as ingredients, such as corn syrup, agave syrup and flavoured syrups for milk."*

- **Reference amount: 30 mL**
- **Serving of stated size, prescribed by column 3A: 2 tbsp (30 mL)**

The 15 mL serving on the July artwork is not the prescribed serving and must be changed. (Alternative reading: item U.14, "syrups used as toppings", reference amount 60 mL. U.15 is the correct fit for a cocktail and coffee syrup. Confirm in the CFIA Industry Labelling Tool.)

### 5.2 Nutrition Facts table (recipe-calculated, per 30 mL)

| Line | Value | %DV |
|---|---|---|
| Serving | Per 30 mL (2 tbsp) / pour 30 mL (2 c. à soupe) | |
| Calories / Calories | 100 | |
| Fat / Lipides | 0 g | 0 % |
| Carbohydrate / Glucides | 26 g | (no %DV) |
| Sugars / Sucres | 26 g | **26 %** |
| Protein / Protéines | 0 g | |
| Sodium | 0 mg | 0 % |

Unrounded basis: **25.69 g sugars per 30 mL**, computed **from the recipe**, not from the rounded
64 °Brix display value.

> ⚠️ **THE DECLARED SUGARS VALUE IS 0.7% FROM A ROUNDING BOUNDARY.** 25.69 g rounds to **26 g**; the
> boundary is 25.50 g, **0.19 g away**. At a measured 64 °Brix it is 25.38 g and declares as **25 g**.
> A refractometer reading one point low flips the label. Calories hold at 100 across 61–66 °Brix, so
> only sugars and carbohydrate move. **Measure the Brix before the labels print, not after.** Rounded per CFIA rules (calories >= 50 to the nearest 10; carbohydrate and sugars to the nearest 1 g; %DV to the nearest 1%, calculated on the unrounded amount against a 100 g Daily Value for sugars).

Footnote, verbatim:
```
*5% or less is a little, 15% or more is a lot
*5% ou moins c'est peu, 15% ou plus c'est beaucoup
```

### 5.3 Front-of-package nutrition symbol: REQUIRED

Sugars are 26% DV per 30 mL. The reference amount is <= 30 mL, so the trigger is **10% DV**, not the default 15%. The product exceeds it by a factor of 2.6.

The Division 18 "sweetening agents sold as such" full exemption (sugar, honey, maple syrup, table syrup, agave, corn syrup, molasses) does **not** apply: this is a compounded botanical flavouring syrup, not a sweetening agent sold as such.

Presentation requirements:
- **Symbol:** "High in sugars / Élevé en sucres", one nutrient bar, magnifying-glass format, Schedule K.1 FDR
- **Location:** on the principal display panel. The front panel is approximately square (2.75 in tall), so where PDP height >= PDP width the symbol must sit in the **upper half** of the PDP
- **Cylindrical rule:** the outer edge of the symbol's buffer must be at least 10% of the principal display surface width from the left or right edge of that surface
- **Buffer:** a clear zone equal to the x-height of the symbol text, no other text or graphics inside it
- **Language:** bilingual symbol, or two unilingual symbols
- **Size:** proportional to the principal display surface (PDS). For this bottle the PDS under CPLR paragraph (c) is 40% of the total side surface excluding top and bottom, which computes to roughly **78 to 105 cm²**, straddling the boundary between the "> 30 cm² to <= 100 cm²" and "> 100 cm² to <= 250 cm²" bands. **[VERIFY]** Pin the PDS before choosing the size row. Per the Directory, the bilingual **horizontal** symbol is **2.80 x 1.42 cm with a 1.1 mm buffer** in the 30 to 100 cm² band and **3.60 x 1.89 cm with a 1.5 mm buffer** in the 100 to 250 cm² band. Bilingual **vertical** is 1.37 x 2.60 cm and 1.75 x 3.31 cm respectively. Reserve the larger footprint and the layout is safe either way.
- **Artwork:** do not redraw the symbol. The exact specifications and the 94-page Compendium of Nutrition Symbol Formats are **free public downloads**, so layout can proceed immediately. Only the editable `.eps` files require a request to smiu-ugdi@hc-sc.gc.ca with subject line "HPFB BNS Compendium of Nutrition Symbol Formats"; the label printer may already hold them.

**Consequence for front-panel copy:** when the PDP carries a "high in sugars" symbol, all sugars-related nutrient content claims are prohibited on the PDP except "reduced in sugar". No "lightly sweetened", no "less sugar", no "unsweetened". Size limits also apply to health-related representations on the PDP, though not to the brand or product name. Descriptors like "small batch", "no essential oils" and "no artificial colour" are not nutrient content claims and remain permitted.

### 5.4 Origin claim: "Product of Canada" must be removed

CFIA requires that all or virtually all major ingredients, processing and labour be Canadian, with non-Canadian material under 2% of the product. Cane sugar is named by CFIA as an ingredient not grown in Canada, and here it is ~65% of the product by mass. Citric acid and butterfly pea flower are also imported.

- **Remove:** "Product of Canada / Produit du Canada"
- **Replace with:** "Made in Canada from domestic and imported ingredients / Fait au Canada avec des ingrédients canadiens et importés"

The lavender and water are Canadian, so an ingredient-origin claim remains available and truthful, for example "Lavender grown on the Naramata Bench".

### 5.5 Other mandatory elements

- Bilingual (EN and FR) for all mandatory information. Not optional: this is a prepackaged consumer food sold nationally.
- Net quantity in metric on the PDP. **[VERIFY]** type height against PDS area.
- Ingredient list, bilingual, descending by weight.
- Allergens: no priority allergens present. No "Contains" statement. **[VERIFY]** shared-equipment cross-contact before omitting "may contain".
- Dealer name and principal place of business, sufficient for postal delivery. **RESOLVED 2026-09-06:** use the farm address, **3820 Partridge Rd, Naramata, BC, Canada V0H 1N1**. Postal code confirmed by the owner. Note the July artwork printed **V0H 1N0**, which is wrong and must be corrected. Do not use the owner's Kelowna home address anywhere on the label or in public materials.
- Best before date and lot code.

## 6. Label copy blocks (paste verbatim)

French is a working draft and must be professionally verified before print.

### FRONT (principal display panel)

Brand lockup (use the existing outlined vector logo):
```
Bench & Bloom
NARAMATA BENCH BOTANICALS
```

Common name, bilingual, mandatory:
```
Lavender Syrup
Sirop à la lavande
```

Descriptor lines (revised: "estate-grown" as a bare descriptor is not defensible now that imported sugar is the lead ingredient):
```
Small batch · estate lavender · Naramata Bench
Grosso lavender + butterfly pea · ruby red, no artificial colour
```

Net quantity:
```
250 mL (8.45 fl oz)
```

Front-of-package symbol: "High in sugars / Élevé en sucres", upper half of the PDP.

### BACK, right wing

Nutrition Facts table per section 5.2.

Ingredients (order verified by weight: sugar 2,200 g > water 1,183 g > lavender ~50 g > citric acid ~13.5 g > butterfly pea ~2 g):
```
Ingredients: Sugar, water, lavender (Lavandula ×intermedia 'Grosso'),
citric acid, butterfly pea flower (Clitoria ternatea).

Ingrédients : Sucre, eau, lavande (Lavandula ×intermedia 'Grosso'),
acide citrique, fleur de pois bleu (Clitoria ternatea).
```

Clean-label line (all three claims remain true):
```
No essential oils, no artificial colour, no synthetic flavour.
Sans huiles essentielles, sans colorant artificiel, sans arôme synthétique.
```

How to use:
```
Stir into gin cocktails, sparkling wine, lemonade or coffee.
Mélanger à des cocktails au gin, vin mousseux, limonade ou café.
```

Storage (changed: this is no longer a refrigerated product):
```
Refrigerate after opening / Réfrigérer après ouverture
```

### BACK, left wing

Story:
```
Half an acre of Grosso lavender on the Naramata Bench, above Okanagan Lake.
Real buds, steeped three minutes and strained by hand. The butterfly pea flower
goes in blue and comes out ruby.
```

Dating — **printed as blank field names only, never as values.** The artwork carries a
**51 × 12.5 mm coding panel** on the left wing with a **coating knockout** (no laminate, no varnish)
so solvent ink will key and dry. Values are stamped per batch, flat, while the labels are still on
the liner. ~12 month convention; colour rather than safety is the limit. Bilingual month symbols
(JA FE MR AL MA JN JL AU SE OC NO DE). **Lot format `YYYYMMDD-nn`**, so the lot carries the bottling
date and no separate bottled-date line is needed. **DECIDED 2026-09-06: pH and °Brix are NOT printed on the label** — they live in the batch record, keyed by the lot.
```
BEST BEFORE / MEILLEUR AVANT   [ blank, stamped at fill ]    e.g. 2027 SE 15
LOT                            [ blank, stamped at fill ]    e.g. 20260915-01
```

Responsible party:
```
Prepared for / Préparé pour:
Bench & Bloom, 3820 Partridge Rd, Naramata, BC, Canada V0H 1N1
benchandbloom.com · hello@benchandbloom.com
```

Origin:
```
Made in Canada from domestic and imported ingredients
Fait au Canada avec des ingrédients canadiens et importés
```

Codes (carry forward unchanged from the July artwork):
- GS1 UPC, GTIN **627146286305**, true black bars on plain white, quiet zones intact, do not scale below 80%
- QR code to `benchandbloom.com/recipes/naramata-sunset`, minimum 11 mm square, 4-module quiet zone, do not recolour. **[VERIFY]** the target recipe page still describes a blue-to-pink drink; rewrite it or repoint the QR.

## 7. Physical and print specification (unchanged from the July wrap)

- **Trim:** 7.25 in W x 2.75 in H, single wrap
- **Bleed:** 0.125 in all sides, artwork 7.5 in x 3.0 in
- **Safe margin:** 0.125 in inside trim
- **Wrap math:** 7.25 in label on a 7.46 in circumference leaves a ~0.21 in bare-glass window at the rear seam. Intentional: forgiving for hand application, and the ruby colour shows through.
- **Panel:** 2.75 in centres in the 3.125 in straight body panel, ~0.19 in clearance top and bottom
- **Stock:** soft-matte cream BOPP film, waterproof, permanent glass-rated adhesive, matte laminate. No paper, no gloss.
- **Colour:** CMYK per the brand palette below, or spot Pantone 5275 C for the lavender
- **Fonts:** Fraunces (wordmark and common name), Inter (everything else). Outline before print.
- **Guides:** delete the `#guides` layer before output.

### Brand palette

| Role | Name | HEX | CMYK |
|---|---|---|---|
| Ground | Chalk White | `#F7F3EE` | 0 / 2 / 4 / 3 |
| Wordmark, headings | Lavender Deep | `#5A4A78` | 25 / 38 / 0 / 53 |
| Sprig accent | Lavender | `#7C6A9C` | 21 / 32 / 0 / 39 |
| Legal, body text | Onyx | `#2D2933` | 12 / 20 / 0 / 80 |
| Rules, eyebrow | Bench Gold | `#C2A05E` | 22 / 31 / 70 / 4 |
| Gold text | Gold Deep | `#7A5E28` | 22 / 41 / 90 / 36 |
| Sprig stem | Sage | `#8A9A78` | 26 / 9 / 40 / 16 |

Lavender is an accent, never body text. Gold is for thin rules only. Barcode block stays true black on white.

Design consideration: the syrup is now ruby red behind a lavender-violet brand palette. Check the front panel against a filled bottle before committing, since the rear window and the shoulder will show red against violet.

## 8. Hard rules (do not break)

- Brand is **Bench & Bloom**. Never "Provence", "France" or "French lavender". Provenance is Naramata Bench, Okanagan, BC.
- No "organic", no "100% natural", no "Product of Canada".
- No blue-to-pink, colour-change or "add citrus to turn it pink" copy anywhere. The product is already red.
- No "shelf-stable" claim is needed on-label, and no "Keep refrigerated" statement either.
- No sugars-related nutrient content claim on the PDP.
- All mandatory copy in English and French.
- Do not redraw the front-of-package symbol by hand. Use the official Health Canada EPS.

## 9. Open items before print

| # | Item | Owner |
|---|---|---|
| 1 | **U.15 vs U.14 SENT 2026-09-06** to `food-aliment@hc-sc.gc.ca`. Acknowledged; stated target **~2 weeks**, so expect a reply about **2026-09-20**. **This is now the critical path for the Nutrition Facts table**, ahead of the symbol EPS. **Route PDS and labelling-requirement questions to AskCFIA** (`inspection.canada.ca/en/about-cfia/contact-us/ask-cfia`); Health Canada declined them on 2026-09-08 and does not review labels for compliance. Remaining for the CFIA Industry Labelling Tool session: **how to determine the PDS**, net-quantity type height, whether a best-before is required at all (durable life >90 days), allergen/cross-contact wording, and the seal sticker's brand-only status | Nelson |
| 2 | ~~Resolve the dealer address~~ **CLOSED 2026-09-06:** 3820 Partridge Rd, Naramata, BC V0H 1N1. Correct the postal code from the July art's V0H 1N0 | done |
| 3 | Professional French verification | external |
| 4 | Measure actual Brix with a refractometer on batch 1 and confirm 64 to 66; recompute the NFt if it deviates by more than 1 °Brix | Nelson |
| 5 | Measure actual pH with a meter **for the record**. **Risk downgraded:** two independent methods (stoichiometric 2.34, and the batch photo's hue of **351°** read through the butterfly pea, §4.1) agree the product is **≤ 3.0**, clearing both the 4.6 safety threshold and the 4.0 hurdle with margin | Nelson |
| 6 | ~~Pin the principal display surface~~ **CLOSED 2026-09-06.** 60.2 cm² (body only) to 91–94 cm² (true geometry); both readings sit in the **> 30 to ≤ 100 cm²** band, so use that size row | done |
| 7 | ~~Obtain the official FOP symbol `.eps`~~ **RESOLVED 2026-09-08.** Health Canada (Laurène Bakouche, SMIU) supplied a zip of **280 .eps files** covering every acceptable variation of the nutrition symbol: `https://drive.google.com/file/d/1nWlOmu77euniS4QOWsWqOBwGSNEVa-fb/view`. The **Compendium of Nutrition Symbol Formats** is public: `canada.ca/en/health-canada/services/technical-documents-labelling-requirements/nutrition-symbol-formats-label-designers/compendium-nutrition-symbol-formats.html`. **Download the zip and store it in the repo before the share link ages out.** | done |
| 8 | Net-quantity type height — **provisionally 3.2 mm minimum**; both PDS readings fall in the same `> 32 to ≤ 258 cm²` band. **[VERIFY** the band table with item 1**]** | verify |
| 9 | ~~Rewrite or repoint `naramata-sunset`~~ **CLOSED — both done.** Page rewritten (arrives ruby; the lemon is for brightness) **and** the printed QR repointed to `/recipes/lavender-milk`. Live and verified | done |
| 10 | ~~Set real dates at fill~~ **SUPERSEDED.** No date prints in the artwork; the label carries a blank coding panel stamped per batch. Remaining task is operational: source a changeable-band date stamp and **solvent ink rated for non-porous surfaces**, and run the smear test | Nelson |

## 10. Confidence and provenance

- **[High confidence, retrieved]** Reference amount 30 mL (item U.15), serving 2 tbsp; FOP thresholds 10% DV for reference amounts <= 30 g/mL; FOP full exemption list; FOP placement, buffer, size hierarchy and PDP claim restrictions; "Product of Canada" 2% rule and the "Made in Canada from domestic and imported ingredients" qualifier; CPLR definition of principal display surface.
- **[High confidence, calculated]** Brix, density, yield, sugar concentration, per-serving sugars and calories, CFIA rounding. Density cross-check independently confirms the Brix figure.
- **[Moderate confidence, calculated]** pH ~2.5 and water activity ~0.85. Both are estimates from concentration, not measurements. Items 4 and 5 above exist to close this.
- **[Moderate confidence, training]** Butterfly pea anthocyanin colour response to pH. The 2026-09-06 photograph of the finished batch confirms the direction and magnitude empirically.
- **[Low to moderate confidence, calculated]** Principal display surface of 78 to 105 cm². The bottle is not a true cylinder, so the 40% rule gives a range rather than a number. This straddles a size band boundary and must be pinned.
- **Not verified:** ingredient masses for lavender and butterfly pea are estimated from volume. Neither changes the declared ingredient order, and both are strained out.

## 11. References

Health Canada. *Nutrition labelling: Table of reference amounts for food.* Items U.14, U.15. https://www.canada.ca/en/health-canada/services/technical-documents-labelling-requirements/nutrition-labelling-table-reference-amounts-food.html

Health Canada. *Front-of-package nutrition symbol labelling guide for industry.* Sections 4.2, 4.3, 5.2, 6.1 to 6.8, 8.1, 8.2. Food and Drug Regulations ss. B.01.350 to B.01.358, Schedule K.1. https://www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/guidance-documents/front-package-nutrition-symbol-labelling-industry.html

Canadian Food Inspection Agency. *Origin claims on food labels: Guidelines for "Product of Canada" and "Made in Canada" claims.* https://inspection.canada.ca/en/food-labels/labelling/industry/origin-claims

Government of Canada. *Consumer Packaging and Labelling Regulations*, C.R.C. c. 417, s. 2, definition of "principal display surface", paragraph (c). https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._417/page-1.html

Internal: `pricing/Pricing_benchandbloom_2026.md` (superseded, built on FBA assumptions for the refrigerated product), `singlelabel/Label_PrinterSpec_Wrap_uline2026.md` (physical and print specification carried forward, regulatory content superseded).
