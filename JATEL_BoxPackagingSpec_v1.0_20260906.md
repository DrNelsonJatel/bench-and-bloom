# Bench & Bloom — Bottle Box & Shipper Specification

**Document:** JATEL_BoxPackagingSpec_v1.0_20260906
**Status:** First issue. Geometry computed from the bottle and cross-checked against
`singlelabel/Label_PrinterSpec_Wrap_uline2026.md`.
**Scope:** A single-bottle retail carton and a three-bottle shipping box. **Plain white, no print.**
All branding is carried by the seal sticker (`JATEL_SealStickerSpec_v1.0_20260906.md`).
**Companion:** `JATEL_ProductSpec_v1.0_20260906.md` (authoritative product definition).

---

## 1. The bottle these are built around

| Property | Value |
|---|---|
| Bottle | Uline **S-23397**, 8 oz clear Boston round glass. **Verified in hand**, order 53425173, 48 EA received 2026-06-23. **Caps included.** |
| Neck finish | 28-400 |
| Body diameter | **2.375 in** (60.3 mm) |
| Overall height | **5.437 in** (138.1 mm) |
| Circumference | 7.461 in (189.5 mm) |
| Straight label panel | 3.125 in |
| Tamper band | Uline S-17668 black shrink band over cap/neck |

**Filled weight ≈ 540 g. VERIFIED 2026-09-06.** Bottle **209 g** with the cap (Uline lists S-23397
at a unit weight of 0.46 lb / 0.21 kg, **cap included and shipped attached**) + syrup 329 g
(250 mL × 1.316 g/mL at 64 °Brix) + label ~2 g.

> This closes the open estimate. Note it lands close to this spec's 200 g guess and **well above the
> 175 g used in the channel costing model**, which understated the filled bottle by 30 g, or 6%.
> A confirmatory kitchen-scale check on a real bottle is still worth thirty seconds, since Uline's
> unit weight may be a shipping figure rather than a measured one.

**The body is a true cylinder** through the whole label panel, tapering only at the shoulder. That is
what makes the 7.25 in wrap label work, and it is also why the square carton in section 2 carries a
29% corner void. Do not treat the void as waste: it is exactly where cushioning goes, for free, and a
round tube costs more, does not stack, and does not ship flat.

> Note the syrup is ~25% heavier than the abandoned 1:5 formulation (329 g vs 264 g). Any shipping
> cost carried over from the July pricing sheet is understated.

---

## 2. Single-bottle retail carton

A round bottle in a square tube. The corners are void by design; that is normal for a tuck carton
and is what makes the box cheap and stackable.

| Dimension | Value |
|---|---|
| **Internal** | **2.500 × 2.500 × 5.625 in**  (63.5 × 63.5 × 142.9 mm) |
| External (24 pt SBS) | 2.548 × 2.548 × 5.673 in |
| Clearance | 0.125 in diametral, 0.188 in height |
| Footprint void | 29% (round bottle, square tube) |

**Specify to the supplier as internal dimensions.** Carton suppliers quote internal by default, but
say it explicitly, because ordering 2.5 in *external* gives a box the bottle will not enter.

**Construction**
- **Style:** reverse tuck end (RTE), or straight tuck end if the supplier prefers. Both close without
  glue and both present a clean flap for the seal sticker.
- **Stock:** **18 to 24 pt SBS (solid bleached sulphate), white both sides, uncoated or matte.**
  24 pt if you want it to feel substantial; 18 pt is adequate and cheaper.
> ### ⚠️ "No print" holds for the BOX. It does not survive contact with FBA.
> An FBA-bound unit must additionally carry a hand-applied **FNSKU barcode label** (you are not in
> Brand Registry, so stickerless is unavailable), an **expiry sticker in `MM-DD-YYYY`**, the expiry
> again on the **outside of the bubble wrap**, and the expiry on the **outer box at 36 pt or larger**.
> A three-pack sold as its own ASIN also needs **its own GTIN**, which is a barcode.
>
> None of that changes the box order — it is all applied afterwards — but it means the finished FBA
> unit is not a clean unprinted box, and the labour is real: roughly **240 discrete sticker and wrap
> applications** across 48 singles and 16 three-packs, about **80 minutes**, which the channel
> costing explicitly does not model.

- **Print:** **none.** Plain white. This is a deliberate cost and lead-time decision: unprinted stock
  cartons ship from inventory, custom-printed cartons carry a plate charge and a 1,000-unit minimum
  that a 48-bottle pilot cannot absorb.
- **Finish:** avoid gloss. It fights the matte label and the brand.

**This carton is not a shipper.** 24 pt paperboard will not protect glass in a parcel network on its
own. A single bottle sold by mail needs the carton *inside* a corrugated mailer with void fill. The
carton is for shelf presentation, gifting, and as the unit that goes into the three-pack.

---

## 3. Three-bottle shipping box

Two viable builds. **Option A is recommended.**

### Option A (recommended): three single cartons in a row

| Dimension | Value |
|---|---|
| **Internal** | **7.769 × 2.673 × 5.798 in**  (197.3 × 67.9 × 147.3 mm) |
| External (B-flute) | 8.019 × 2.923 × 6.048 in  (20.4 × 7.4 × 15.4 cm) |
| Volume | 2,323 cm³ |
| Gross weight | **≈ 1.86 kg** |

Round up the internal to **7.75 × 2.75 × 5.75 in** when ordering; that is closer to a stock size and
the 0.125 in slack is welcome, not harmful.

**Why A.** Each bottle already sits in its own rigid tube, so the cartons act as the divider. Nothing
extra to buy, nothing extra to assemble, and the three-pack can be broken down into three sellable
retail units if a boutique wants singles instead.

### Option B: three bare bottles plus a corrugated divider

| Dimension | Value |
|---|---|
| Internal | 7.375 × 2.625 × 5.687 in |
| External | 7.625 × 2.875 × 5.937 in  (19.4 × 7.3 × 15.1 cm) |
| Volume | 2,133 cm³ (8% smaller than A) |
| Gross weight | ≈ 1.86 kg |

Marginally smaller, and it saves the cost of three cartons. It requires a **die-cut two-piece
corrugated divider** (glass touching glass in transit will chip or break), and it gives up the
retail-unit flexibility. **The 8% volume saving buys nothing**, because both options bill on actual
weight (section 5), so A wins on every axis that matters.

### Construction, both options
- **Board:** **B-flute (≈ 3 mm) single wall**, 200 lb test / 32 ECT minimum. C-flute is also fine and
  slightly more cushioning if the supplier stocks it in this size.
- **Style:** **RSC** (regular slotted container), the standard shipping box.
- **Colour:** **white exterior** (bleached white kraft or white-top liner). Interior kraft is fine
  and normal; specify **"white outside"**, not "white two sides", which costs more for no benefit.
- **Print:** **none.**
- **Void fill:** the 0.125 in slack plus the carton corners is not cushioning. Add a **kraft paper
  pad or crinkle fill at the top** so nothing moves vertically. Shake the packed box beside your ear:
  if you hear glass, add fill.
- **Closure:** 2 in kraft or clear tape, centre seam, then the seal sticker over the closure.

---

## 4. Sourcing note

Both boxes are **stock commodity items** at Uline, ULINE Canada, PakTech, or any local corrugated
converter. Quote the **internal dimensions and the board spec**, not a part number.

> **I have not verified any supplier SKU for these cartons.** The bottle SKU (S-23397) and shrink
> band (S-17668) come from your existing printer spec and are trusted. Do not let a substituted
> carton SKU past you without checking its **internal** dimensions against section 2.

Ask any converter for the **cost break at 100, 250 and 500 units.** Corrugated pricing steps hard at
volume, and the 48-bottle pilot will be buying at the worst point on the curve. Budget for that
rather than being surprised by it.

---

## 5. Shipping consequences

| | 3-pack, option A |
|---|---|
| External | 20.4 × 7.4 × 15.4 cm |
| Girth, L + 2(W+H) | 65.9 cm |
| Actual weight | **1.86 kg** |
| Dimensional weight (/6000) | 0.39 kg |
| Dimensional weight (/5000) | 0.46 kg |
| **Billed on** | **ACTUAL, 1.86 kg** |

**The single most useful fact here: you will never be billed on dimensional weight.** Glass and
sugar syrup are dense, and actual weight beats volumetric by roughly 4x. That means:

1. **Do not pay for a smaller box.** Volume optimisation saves nothing. Spend the space on cushioning
   instead, because breakage is the real cost.
2. **Every carrier quote is a weight quote.** Compare Canada Post against Amazon on the 1.86 kg line
   and ignore the cubing tables.
3. **A six-pack would weigh ~3.6 kg** and stays well inside normal parcel limits, if the three-pack
   validates and you want a case rate later.

Both boxes sit far inside Canada Post's maximum dimensions (2 m longest side, 3 m length-plus-girth)
and inside normal Amazon standard-size parcel limits. **[Moderate confidence on the volumetric
divisor: carriers use 5000 or 6000 cm³/kg and it varies by service. It does not change the
conclusion, since actual weight wins under either.]**

---

## 6. Open items

| # | Item | Owner |
|---|---|---|
| 1 | **Weigh an empty bottle.** The 200 g glass figure is an estimate and drives every shipping number here | Nelson |
| 2 | Confirm carton internal dimensions against a real bottle before ordering quantity. Order **one sample** first | Nelson |
| 3 | Quote both boxes at 100 / 250 / 500 | Nelson |
| 4 | Drop-test a packed three-pack from 1 m onto concrete, on a corner. Corners fail first | Nelson |
| 5 | Decide whether singles ship at all, and if so spec the corrugated mailer they go inside | Nelson |
| 6 | Confirm the current Canada Post volumetric divisor and the Amazon size tier for 1.86 kg | Nelson |

---

## 7. Provenance

- **[High confidence, computed]** All geometry, from the bottle dimensions in
  `singlelabel/Label_PrinterSpec_Wrap_uline2026.md`. Circumference recomputed as 7.461 in against the
  7.46 in on file, and the 0.211 in wrap window against the documented 0.21 in. Both reconcile.
- **[High confidence, computed]** Syrup mass 329 g, from 250 mL × 1.316 g/mL in
  `JATEL_ProductSpec_v1.0_20260906.md`.
- **[Estimated, not measured]** Glass 200 g, cap 5 g, carton 22 g, shipper 150 g, pad 40 g. Typical
  values for this format, not weighed. Item 1 above closes this.
- **[Moderate confidence]** Carrier volumetric divisors and maximum-dimension limits.
- **[Not verified]** No supplier part number for either box has been checked.
