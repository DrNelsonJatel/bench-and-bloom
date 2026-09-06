# Bench & Bloom — Single Wrap Label Printer Spec (uline2026) — **v2.0, 2026-09-06**

> ## ⛔ THE JULY ARTWORK CANNOT BE REPRINTED. IT MUST BE REDRAWN.
>
> The product was reformulated on 2026-09-06 from a **1:5 refrigerated cordial** to an
> **11:5 acidified, sugar-preserved syrup**. Authoritative definition:
> **`JATEL_ProductSpec_v1.0_20260906.md`** (repo root). Read that first.
>
> | | July artwork | Current product |
> |---|---|---|
> | Sugar : water | 1 : 5 | **11 : 5** |
> | Brix | ~14.5 | **64.8** |
> | pH | ~7 | **~2.5** (citric acid, 0.53% w/v) |
> | Colour in bottle | blue | **deep ruby / garnet** |
> | Serving | 15 mL | **30 mL** (Table of Reference Amounts item U.15) |
> | Nutrition | 10 cal / 2 g sugars | **100 cal / 26 g sugars / 26% DV** |
> | FOP symbol | not required | **REQUIRED**, and it needs upper-half PDP space |
> | Storage | Keep refrigerated | **Refrigerate after opening** |
> | Origin claim | Product of Canada | **Made in Canada from domestic and imported ingredients** |
>
> **A prior version of this file stated a 60 mL reference amount and a 15% DV trigger.
> Both were wrong.** The correct figures are **30 mL** and **10% DV**. Corrected throughout below.
>
> **What is still valid in this file:** every physical and print specification. Trim, bleed, wrap
> math, stock, adhesive, finish, fonts, palette, barcode handling. Sections marked *(physical)* are
> unchanged and can be used as-is.

Hand this file **plus `Label_benchandbloom_Final_uline2026_Wrap.svg`** to the label printer
(StickerYou / Jukebox / Avery WePrint / a local trade printer). The `.png` / `.jpg` in this folder
are **previews only** — print from the **SVG** (vector, infinite resolution).

This replaces the old two-label set. **Why one wrap:** without a benchtop labeller, getting two
separate labels square and aligned on opposite faces by hand is fiddly. A single wrap is applied in
one motion — line up the top edge, roll the bottle once — so it's the right call for a hand-applied
pilot run.

---

## The bottle
- **Uline S-23397** — 8 oz Clear Boston Round glass, neck finish **28-400**.
- Height 5.437″ · body diameter **2.375″** · **circumference 7.46″** · straight **label panel 3.125″ tall**.
- Tamper band: **Uline S-17668** black shrink band (55 × 28 mm) over the cap/neck, **above** the label.

## Label size & geometry
- **Trim: 7.25″ W × 2.75″ H** (single piece, wraps the bottle).
- **Bleed: 0.125″** all sides → **artwork / cut sheet 7.5″ × 3.0″**.
- **Safe margin: 0.125″** inside trim — all text/logo/barcode are kept inside it.
- **Wrap math:** 7.25″ label on a **7.46″** circumference leaves a **~0.21″ vertical window of bare
  glass** where the two ends approach each other. This is **intentional and good**:
  1. the ruby syrup still peeks through (the colour is the product's signature), and
  2. the ends **never need to butt or overlap precisely** — so hand application is forgiving (no
     labeller, no registration headache, no wrinkled seam).
- **Height:** 2.75″ centres in the 3.125″ straight panel with ≈ 0.19″ clearance top and bottom.
- The file is built at final size. **Magenta dashed = trim, cyan dashed = safe.** Two faint green
  dashed verticals mark where the wrap curves front↔back (front panel framed by the gold rules).
  **Delete the `#guides` layer before printing** (or tell the printer they're non-printing).

## Dating, logo & extras (2026 pilot)
- **Front logo** = the official outlined **Bench & Bloom** lockup (sprig + wordmark + descriptor),
  embedded as vector — fully font-independent. The descriptor reads the brand-canonical
  **"NARAMATA BENCH BOTANICALS"** (regenerated as outlined Inter; the old logo art said
  "Lavender · Naramata Bench" — now corrected here and in `public/brand/logo-*.svg`).
- **Best-before convention = ~12 months, AMBIENT.** ⛔ **NO DATE IS PRINTED IN THE ARTWORK.**
  The label carries a blank **coding panel** that is stamped per batch — see
  **"Coding panel (date + lot)"** below. The old approach baked
  `Packaged 2026 07 01 / Best before 2026 10 01 / LOT 2026-001` into the vector art, which meant every
  batch needed a new print run and left 48 labels that expired with one batch. That is now fixed. Format `YYYY MM DD`, bilingual, plus **LOT**. This is a
  **high-sugar (64.8 °Brix, 11:5 sugar:water), acidified (pH ~2.5) product** and it **IS
  shelf-stable** (a_w ≈ 0.85). Preservation is carried by **two hurdles, sugar and acid**, plus
  hot-fill into sanitized glass, so the label carries **"Refrigerate after opening / Réfrigérer après
  ouverture"** and a ~12-month dated life. **Colour, not safety, is the limit on shelf life:**
  anthocyanins are at their most stable below pH 3.5, so the ruby holds far better than the old blue
  did. Stamp the real packaged/best-before dates + lot per batch.
- **Ingredients (5, current product — ORDER HAS CHANGED, sugar now leads by weight):** sugar, water, lavender (*Lavandula* ×*intermedia* 'Grosso'), citric acid,
  butterfly pea flower (*Clitoria ternatea*) — bilingual, descending by weight, binomials italicised.
  (At 11:5 **sugar is the largest component at ~65% by mass**, so it leads the list. Citric acid
  remains in the product and must be declared; the lavender and butterfly pea are strained out but
  are still declared by their as-added weight.)
  Clean-label trio stated: **no essential oils, no artificial colour, no synthetic flavour.**
- **QR code** (left wing, beside the UPC) → **`benchandbloom.com/recipes/lavender-milk`**.
  ⚠️ **Repointed.** It previously pointed at `/recipes/naramata-sunset`, which described a
  blue-to-pink serve the product can no longer perform. The colour change now happens in milk, and
  `/recipes/lavender-milk` is the serve that demonstrates it. **Both pages are live; verify the new
  target loads before generating the symbol.** 33-module symbol with a 4-module quiet zone; keep it
  ≥ 11 mm square in print and do **not** recolour or crop the quiet zone, or it may not scan.

## Coding panel (date + lot) — **variable data, stamped at fill**

The artwork prints the **field names** and leaves the **values blank**. Only the operator's stamp
changes between batches, so one print run serves every batch until the recipe or the law changes.

### Geometry
- **Panel: 42 × 13 mm**, on the **left wing**, above the "Prepared for" block.
- **Pure ground, no artwork behind it.** Chalk White `#F7F3EE` or pure white. Nothing screened, no
  rules crossing it, no drop shadow. Ink needs maximum contrast and a clean key.
- Two lines, each with a pre-printed bilingual field name and a blank value zone:

```
  BEST BEFORE / MEILLEUR AVANT   [ ______________ ]     ← ~30 mm blank
  LOT                            [ ______________ ]     ← ~30 mm blank
```

- Field names in **Inter, 6 pt, Onyx `#2D2933`**. Value zones sized for **8 pt** stamped characters:
  a full date reads ~15.5 mm wide, so 30 mm gives comfortable room and tolerates a crooked stamp.
- Line height 3.8 mm at 8 pt; two lines plus leading needs 9.6 mm, inside the 13 mm panel.

**Space check:** the left wing is 60.5 × 63.5 mm. With the UPC, QR, address, origin claim, story and
this panel it runs to **81% committed.** It fits, but there is little slack — **if anything has to
give in layout, shorten the provenance story, not the coding panel.**

### ⚠️ The trap: ink will not dry on laminated BOPP

This is the single thing that ruins hand-coded film labels. **BOPP is non-porous, and a matte
laminate over it is more so.** Ordinary rubber-stamp ink will bead, smear, transfer to the next
bottle, and thumb off a week later. A best-before date that rubs off is a compliance failure, not
just an annoyance.

**Tell the printer, in these words:** *"Leave a coating knockout in the coding panel — no laminate and
no varnish in that window — for on-line date coding."* Printers do this routinely and it usually costs
nothing.

**Then still use the right ink:** a **solvent-based, fast-dry ink rated for non-porous surfaces**
(the pad or cartridge will say "for glass, metal, plastic, foil"). Water-based office stamp ink will
not work even on a knockout.

### Coding method at pilot scale
- **48 bottles: a self-inking date stamp with changeable bands, plus a solvent ink pad.** Roughly
  $30 to $60. Add a separate small stamp or a fine permanent marker for the lot code.
- **If you scale past a few hundred:** a handheld thermal inkjet (TIJ) coder. Faster, cleaner,
  prints date and lot in one pass. Not worth it for a pilot.
- **Do not** hand-write the best-before in pen. It reads amateur and it smudges on film.

### Best practice: stamp flat, before application
**Stamp the labels while they are still on the liner, laid flat, before any of them touch a bottle.**
You can run a whole strip in a minute. Stamping a curved bottle after application gives you a smeared,
skewed code and one ruined label at a time. Let the ink flash off for a minute before handling.

### Date format
Use the **bilingual month symbols** prescribed in the regulations rather than a numeric month:

`JA  FE  MR  AL  MA  JN  JL  AU  SE  OC  NO  DE`

So a best-before reads **`2027 SE 06`**. One stamp then serves both languages, and it removes any
ambiguity about whether the middle number is a month or a day, which a numeric format would force you
to declare explicitly. **[VERIFY** the exact permitted formats and whether an order declaration is
still needed, in the CFIA Industry Labelling Tool, along with everything else in this file.**]**

Lot format: keep it simple and traceable, e.g. **`2026-001`**, incrementing per batch. Record every
lot against its production sheet, Brix and pH reading in the batch log. That link is your traceability
under SFCR and it is the whole point of the lot code.

### Verification before you commit the run
1. Stamp a printed sample in the coding panel.
2. **Thumb it after 60 seconds.** It must not smear.
3. **Thumb it again after 24 hours, hard.** It must not lift.
4. Leave one sample in a fridge overnight and repeat, because the bottle goes cold after opening.

If any of those fail, the coating knockout is missing or the ink is wrong. Fix it before printing
quantity, not after.

### The commercial upside
Because the labels no longer expire with a batch, **order them in quantity.** The old baked-in dates
capped a sensible order at one batch. A blank coding panel means 500 labels are as usable in a year
as they are today, and label pricing steps hard between 100 and 500. Get both quoted.

---

## Layout (how it reads on the bottle)
- **Centre = FRONT / Principal Display Panel:** sprig mark, "Bench & Bloom", descriptor, common name
  (EN + FR), tasting line, net quantity. Framed by two thin gold rules.
- **Right wing → curves to the back:** Nutrition Facts, ingredients (EN/FR), how to use.
- **Left wing → curves to the back:** provenance story, **blank coding panel (date + lot)**, "Prepared for" address,
  website, **"Made in Canada from domestic and imported ingredients"**, **UPC barcode + QR code**
  (QR → repoint to `/recipes/lavender-milk`, the serve that now carries the colour change).
- The two wings meet at the **rear seam/window**. Orient the bottle PDP-forward when applying.

---

## Material, stock & colour  (what to actually order)

**Face stock — order this:**
- **Soft-matte / cream BOPP film** (bi-axially-oriented polypropylene). **Waterproof and oil/
  moisture-resistant.** The product is now ambient rather than refrigerated, so condensation is no
  longer the daily case, but it still goes in a fridge after opening, gets handled with wet hands and
  meets sticky syrup at the pour. Paper stock will cockle, wick, and tear; **do not use paper.**
- **Slight cream/natural tint preferred** over bright optic-white — it flatters the `#F7F3EE` chalk
  ground and reads premium/editorial, not crafty. If the printer only offers white BOPP, that's
  fine because the artwork carries its own chalk ground edge-to-edge (full-bleed `#F7F3EE`).
- **Avoid glossy white film** — it cheapens the wine-country positioning and fights the matte brand.

**Adhesive:**
- **Permanent, clear, glass-rated, cold/wet-resistant** permanent acrylic. Tell the printer it's
  **for glass, ambient storage but refrigerated after opening, with condensation.** The cold-rated
  adhesive is still the right call and costs nothing extra.

**Finish / lamination:**
- **Matte laminate or matte varnish over-coat** — adds scuff/water durability and the tactile
  premium feel. Avoid gloss laminate.
- Optional upgrade if budget allows: **spot-gloss or soft-touch** on the wordmark/sprig only — nice,
  not necessary for the pilot.

**Colour / printing:**
- **Print CMYK** using the brand values in the palette table below. For the lavender, a **spot
  Pantone** (≈ **PANTONE 5275 C / 668 C** family — ask the printer to match `#5A4A78`) gives a more
  consistent, richer violet across runs if they offer spot; CMYK is acceptable for a short pilot run.
- **Resolution:** vector (infinite); any embedded raster ≥ **300 dpi**.
- **Black:** legal/body text prints as the brand **Onyx `#2D2933`** (a rich near-black), not 100% K
  flat black — keeps the warm, editorial tone. Barcode bars must be **true black on white** (below).

**Barcode:**
- Keep the barcode panel **solid black bars on a plain white block** (already built that way). Do
  **not** tint it, reverse it, or shrink it below ~80% — scanners need the quiet zones and contrast.
- The art carries the **real GS1 barcode (GTIN 627146286305, GS1 Canada)** — the official GS1 output,
  embedded verbatim. **Scan a printed sample** to confirm it reads at final size (don't shrink the
  barcode below ~80% or crop its quiet zones).

**Fonts:**
- **Fraunces** (wordmark + "Lavender Syrup") and **Inter** (everything else). Both free
  (Google Fonts / SIL OFL). **Outline / vectorise all fonts before sending to print**, or supply the
  font files. The mark, rules, and colour fields are already vector.

---

## Full brand palette (CMYK for print)

| Role | Name | HEX | CMYK | Pantone (approx.) |
|---|---|---|---|---|
| **Ground** (label paper) | Chalk White | `#F7F3EE` | 0 / 2 / 4 / 3 | Warm Gray 1 C |
| **Wordmark / headings** | Lavender Deep ("Dark Denim") | `#5A4A78` | 25 / 38 / 0 / 53 | 5275 C |
| Primary accent (sprig buds) | Lavender | `#7C6A9C` | 21 / 32 / 0 / 39 | 666 C |
| Sprig bud highlight | Sprig Violet | `#7E6FA0` | 21 / 30 / 0 / 37 | 666 C |
| **Legal / body text** | Onyx | `#2D2933` | 12 / 20 / 0 / 80 | Black 7 C |
| Secondary text | Ink Soft | `#5A5266` | 12 / 19 / 0 / 60 | Cool Gray 11 C |
| **Rules / eyebrow / accents** | Bench Gold | `#C2A05E` | 22 / 31 / 70 / 4 | 4515 C |
| Gold text (contrast) | Gold Deep | `#7A5E28` | 22 / 41 / 90 / 36 | 4505 C |
| Foliage (sprig stem) | Sage | `#8A9A78` | 26 / 9 / 40 / 16 | 5783 C |
| Cool accent (sparingly) | Lake | `#4F7286` | 65 / 32 / 22 / 8 | 5415 C |

Usage rules carried from the brand guide: **lavender is an accent, never body text**; body text =
Onyx on Chalk; **gold is for thin rules and small accents only** (it cheapens in large fills); lake +
sage are quiet supporting tints.

---

## Regulatory — Canada ✓ built in,  US ⚠ one divergence

The label is built to **Canadian** prepackaged-food rules (SFCR / FDR / CFIA) and is **bilingual
(EN/FR)** throughout. Items below marked **[VERIFY]** must be confirmed before printing via CFIA's
free **Industry Labelling Tool** (inspection.canada.ca) or a food-labelling consultant. **The French
copy is a solid draft — have it professionally verified.**

> **French is MANDATORY — do not remove.** Bilingual (EN + FR) labelling of all mandatory
> information (common name, net quantity, ingredients, Nutrition Facts, storage) is required under the
> Consumer Packaging and Labelling Act + SFCR for prepackaged consumer food sold **nationally** —
> which Amazon.ca is. The narrow exemptions (local foods sold only in the producing area, specialty/
> test-market foods) do **not** apply, and Quebec adds its own French requirements. Removing French
> would risk CFIA non-compliance and Amazon delisting. (The dealer name/address itself need not be
> translated beyond "Prepared for / Préparé pour".)
>
> **Common name dropped "Simple"** → now **"Lavender Syrup / Sirop à la lavande"** (cleaner/more
> premium per label-expert feedback), aligned across the label and the website. The Amazon listing
> **title** aligns to **"Lavender Syrup"** too; keep **"lavender simple syrup"** only in the Amazon
> **backend search keywords** (invisible to shoppers) to retain search intent. **Civic house number
> removed** from the address (privacy) — postal code + town + website/email keep it contactable.

**Canada — present on the label:**
- ✓ Common name, **bilingual**, on the PDP — "Lavender Syrup / Sirop à la lavande"
- ✓ **Net quantity** on the PDP in metric — **250 mL** — **[VERIFY type height** for the PDP area]
- ✓ Ingredient list, **bilingual, descending by weight** — **[VERIFY order against your recipe]**
- ✓ Nutrition Facts table, **bilingual** — **recipe-calculated (per 30 mL / 2 tbsp: 100 cal, 26 g carb, 26 g sugars / 26% DV, 0 fat/protein/sodium)**
- ✓ Dealer name + principal place of business — **"Prepared for / Préparé pour: Bench & Bloom,
      3820 Partridge Rd, Naramata, BC, Canada V0H 1N1"**. This is the **farm** address. The civic
      number **3820 is required and must stay**: an earlier revision removed it for privacy, which
      made the address undeliverable and the field non-compliant. **Never substitute a home address
      here.** ✅ **Postal code confirmed `V0H 1N1`.** ⛔ **The existing artwork prints `V0H 1N0`,
      which is WRONG.** Correct it in the redraw — a wrong postal code in a mandatory field is a
      compliance failure, not a typo.
- ✓ Best-before + lot code fields (`YYYY MM DD` / `LOT 2026-001`) — **fill in real values per batch**
- ✓ Allergens: sugar/water/lavender/butterfly-pea carry **no priority allergens** → no "Contains"
      line. **[VERIFY]** add "may contain" **only if** shared-equipment cross-contact is real.
- ⛔ **Front-of-pack "High in sugars / Élevé en sucres" symbol — REQUIRED. This is the single
      biggest change and it is a PDP relayout, not a patch.** The product is item **U.15** of the
      Health Canada *Table of Reference Amounts for Food* ("syrups used as ingredients"), reference
      amount **30 mL**, prescribed serving **2 tbsp (30 mL)**. Because the reference amount is
      **≤ 30 mL, the trigger is 10% DV, not the default 15%.** At **26% DV** the product exceeds it
      by 2.6x. The Division 18 "sweetening agents sold as such" exemption (sugar, honey, maple, table
      syrup) does **not** reach a compounded botanical flavouring syrup.
      **Placement:** principal display panel, **upper half** (PDP height ≥ width), with a clear
      buffer equal to the symbol's x-height, and the buffer's outer edge at least 10% of the
      principal display surface width in from the left or right edge.
      **Do NOT redraw the symbol.** Obtain the official EPS and the size directory from Health
      Canada: email **smiu-ugdi@hc-sc.gc.ca**, subject *"HPFB BNS Compendium of Nutrition Symbol
      Formats"*.
      **Consequence:** with the symbol on the PDP, all sugars-related nutrient content claims are
      prohibited there except "reduced in sugar". "Small batch", "no essential oils", "no artificial
      colour" and the tasting descriptors are not nutrient content claims and remain permitted.
      **PDS PINNED (2026-09-06): use the `> 30 cm² to ≤ 100 cm²` size row.** The bottle is a
      **Boston round — cylindrical through the full label panel** (confirmed against the physical
      bottle from Uline order 53425173). Computing CPLR s.2(c) at 40% of the side area:
      **straight body only → 60.2 cm²; full true geometry including shoulder and neck → 91–94 cm²
      across every plausible segment split.** Both defensible readings land in the **same band**, so
      the size row is settled and no longer blocks the designer. Only a crude "treat the whole bottle
      as a full-diameter cylinder" reading reaches 104.7 cm², and that reading is wrong because it
      counts the tapered shoulder and the 28 mm neck as if they were 60 mm across.
      *Headroom to the 100 cm² boundary is ~6%, so if you want it airtight, measure the straight body
      height and the shoulder height with calipers and I will recompute exactly.*

**United States (FDA) — if you also sell on Amazon.com:**
- ✓ **Net quantity is dual-declared** on the PDP — **"250 mL (8.45 fl oz)"** — satisfies FDA's
      requirement for both metric and US customary, and Canada's metric requirement. (8.45 fl oz is
      the accurate US conversion of a 250 mL fill — not "8 fl oz".)
- ✓ Statement of identity in **English**, ingredient list in English, and name/place of business —
      all present and FDA-acceptable (foreign address with city + country is allowed).
- ⚠ **Nutrition panel is the one genuine conflict.** A **US FDA Nutrition Facts panel** has a
      **different format** from the Canadian one (different reference values, mandatory nutrients,
      "Amount Per Serving", larger "Calories", US daily-value footnote). **One panel cannot be
      simultaneously compliant in both countries.** Two clean options:
  1. **Print the Canadian bilingual table** (as built) and sell on **Amazon.ca**. For **Amazon.com**,
     run a **separate US label variant** with an FDA-format panel. *(I can generate that US variant
     SVG from this file in ~one pass — just say the word.)*
  2. **Carry both panels** (Canadian *Valeur nutritive* + US *Nutrition Facts*) side-by-side on the
     back — fully dual-compliant, but it's tight on a 7.25″ wrap and would mean trimming other back
     copy. Feasible if cross-border from day one matters more than breathing room.
- For the pilot (Amazon.ca first), **option 1 is recommended**: ship the Canadian label now, add the
  US variant when/if you list on Amazon.com.

**Nutrition Facts are RECIPE-CALCULATED** for the **11:5 sugar:water (by volume), 64.8 °Brix,
acidified, ambient-stable product, per 30 mL (2 tbsp) serving:** Calories 100, Carbohydrate 26 g,
Sugars 26 g (26% DV), Fat/Protein 0 g, Sodium 0 mg. Unrounded basis 25.67 g sugars and 102.7 kcal per
30 mL; rounded per CFIA rules (calories >50 to the nearest 10, carbohydrate and sugars to the nearest
1 g, %DV to the nearest 1% computed on the unrounded amount against a 100 g DV for sugars).
**The serving is prescribed, not chosen** — 2 tbsp follows from the 30 mL reference amount.
**If the recipe changes, recompute, and note the FOP symbol is already required and stays required
anywhere above 3 g sugars / 30 mL.**

> ⚠️ **FOOD SAFETY — this is now an AMBIENT, SHELF-STABLE product, and the reasons have changed.**
> At 64.8 °Brix water activity is ~0.85 and pH is ~2.5, so preservation is carried by **two hurdles,
> sugar and acid**, plus hot-fill into sanitized glass. The label must say
> **"Refrigerate after opening / Réfrigérer après ouverture"** and must **NOT** say "Keep
> refrigerated", which is now false and would misdescribe the product.
>
> **pH is now corroborated by two independent methods.** The butterfly pea is its own indicator: the
> batch-1 photograph reads a hue of **351°** (deep ruby), bracketing **pH ≤ 3.0**, and the
> stoichiometric estimate is **2.34**. **State the pH as `≤ 3.5`**, carrying 0.5 of deliberate margin
> for proxy error. At pH 4 to 6 ternatins are purple, so the product is
> emphatically not near the 4.6 safety threshold. See §4.1 of the product spec.
>
> ⚠️ **Brix is still CALCULATED, not measured, and pH still needs a meter reading for the record.** Confirm
> with a refractometer (expect 64–66 °Brix) and a pH meter (expect ≤ 4.0) on batch 1 **before**
> printing an ambient best-before. If the measured Brix is more than 1 °Brix off, recompute the
> Nutrition Facts table.

## Pre-print checklist
- [ ] **[VERIFY]** all items above in the CFIA Industry Labelling Tool (worth the hour for a real run)
- [ ] Nutrition Facts **rebuilt** for 11:5 / 64.8 °Brix on the 30 mL serving — recompute if measured Brix differs by >1
- [ ] **"Refrigerate after opening"** present; **"Keep refrigerated" REMOVED**; best-before ~12 months
- [ ] **Coding panel present and BLANK** (42 × 13 mm, left wing); no date or lot baked into the artwork
- [ ] **Coating knockout** specified in the coding panel — no laminate, no varnish in that window
- [ ] **Solvent, non-porous-rated ink** sourced; smear-tested at 60 s and at 24 h, cold and ambient
- [ ] **FOP "High in sugars" symbol placed** in the upper half of the PDP, from the official Health Canada EPS
- [ ] **Nutrition Facts rebuilt on the 30 mL serving** (100 cal / 26 g / 26% DV)
- [ ] **Ingredient list reordered**, sugar first, **citric acid added**, EN + FR
- [ ] **"Product of Canada" REMOVED**, replaced with "Made in Canada from domestic and imported ingredients"
- [ ] **All blue-to-pink colour copy removed**; the syrup is ruby
- [ ] **Measure Brix and pH** on batch 1 before committing to an ambient best-before
- [ ] **QR repointed** to `/recipes/lavender-milk`
- [ ] ⛔ **Print derivatives are STALE.** The 2026-07-02 exports (`...PRINTREADY....pdf` / `.png` /
      `.svg`) all render the 1:5 refrigerated product: blue-era copy, 15 mL nutrition table, no FOP
      symbol, "Keep refrigerated", "Product of Canada", July dates. **Do not send any of them to a
      printer.** The editable master must be redrawn against this v2 spec and re-exported.
- [ ] **Address set to `Bench & Bloom, 3820 Partridge Rd, Naramata, BC, Canada V0H 1N1`** (farm address, civic number included)
- [x] **Postal code confirmed `V0H 1N1`** (2026-09-06). ⛔ Artwork's `V0H 1N0` is wrong — fix in the redraw
- [x] **Real GS1 barcode** embedded (627146286305) — scan a printed sample to confirm
- [ ] Have the **French** professionally verified
- [ ] Decide CMYK vs. spot Pantone for the lavender (ask printer)
- [ ] **Outline the fonts** (Fraunces + Inter) or supply font files
- [ ] **Delete the `#guides` layer** (trim/safe/fold lines) before output
- [ ] Order **soft-matte cream BOPP, permanent glass/fridge adhesive, matte laminate**
- [ ] Print one, **wrap a real bottle**, check the 0.21″ window sits where you want it and the panel
      clears the shrink band

## Ordering (read before you upload)
- **Send the printer:** `Label_benchandbloom_PRINTREADY_uline2026.svg` — **guides removed, all fonts
  outlined** (Fraunces + Inter → vector), so nothing prints wrong and no font needs supplying.
- **Set the FINISHED / die-cut size to `7.25in × 2.75in`.** The file is `7.5in × 3.0in` because that
  **includes the 0.125in bleed** — it is **not** the finished size. If you enter 7.5×3.0 as the
  finished size the label comes out too big (over-wraps the 7.46in bottle, too tall for the 3.125in
  panel). Tell the printer: *finished 7.25×2.75, artwork 7.5×3.0 with 0.125in bleed, cut centred.*
- **Do NOT order off the `.png`** — the preview PNGs still show the guide lines and are raster.
- Quantity: order ~2× your bottle count (hand-application wastes a few).

## Files in this folder
- `Label_benchandbloom_PRINTREADY_uline2026.svg` — **SEND THIS TO THE PRINTER** (guides removed, fonts outlined, vector)
- `Label_benchandbloom_PRINTREADY_uline2026_600dpi.png` — 600-dpi raster backup (correct fonts, no guides)
- `Label_benchandbloom_Final_uline2026_Wrap.svg` — **editable master** (keeps text + guides; edit here, then re-export press-ready)
- `Label_benchandbloom_Final_uline2026_Wrap.png` / `.jpg` — previews only (show guides — not for print)
- `Label_PrinterSpec_Wrap_uline2026.md` / `.pdf` — this spec
