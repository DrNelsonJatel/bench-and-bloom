# Verification note — JATEL_ChannelCosting_v1.0_20260906

**Scope:** independent check of the channel costing document against facts this repo has
verified, plus full recomputation of its arithmetic and geometry. **It is not** confirmation
of the live Canada Post or Amazon figures; see §4.

## 1. Findings the source document does not contain

**A three-pack sold on Amazon needs its own GTIN.** [High confidence.] GS1 assigns one GTIN per
distinct consumer unit; a multipack is a distinct trade item. `627146286305` covers the single
250 mL bottle only, and Amazon requires a unique identifier per ASIN. **A second GTIN from GS1
Canada is a cost and a lead time that is not in the plan.**

**That conflicts with two locked specs.** `JATEL_BoxPackagingSpec` says *"plain white, no print"*;
a scannable barcode is print. `JATEL_SealStickerSpec` says brand-only, *"not on the sticker: any
product identity"*; a GTIN is product identity, and placing it there would make the sticker label
copy. **Resolve where the 3-pack barcode lives before ordering boxes.**

**The expiry constraint is a lever, not a wall.** The document treats the 12-month best-before as
given and reports a ~95-day bottling-to-check-in window. The product spec says **colour, not
safety**, sets shelf life, so the date is chosen. At 15 months the window is 186 days; at 18
months, 277. Testable with retains plus `tools/batch_colour_ph.py`.

## 2. Errors confirmed

| Item | Finding |
|---|---|
| Shrink band $0.03 | **Wrong.** S-17668 is $26.00/CT: $0.052 at 500/CT, $0.104 at 250/CT. Already flagged in the pricing sheet and now carried into the model and the $4.60 COGS. |
| "10% multi-buy discount" | 9.86%. Flagged by their own QAQC, still in the text. |
| 30.5% vs 13.8% fulfilment | Both per-bottle, but the text reads as though 13.8% were against $72.99 (it is 15.3%). Name the denominator. |
| Glass 175 g | Asserted as published spec; repo box spec estimates 200 g. **Neither is weighed, and 48 bottles are in hand.** 25 g/bottle moves the 3-pack by 75 g. |
| Duplicate file | The document exists at repo root **and** in `Claude outputs/`. |
| Model comment | Still reads "64.8 Brix"; specs state 64. Cosmetic. |

## 3. Verified clean

Bottle **$1.70** and inbound freight **$0.872** reconcile exactly against Uline order 53425173.
Caps correctly omitted (carton reads W/CAP). Recomputed and matching: COGS $4.60, filled mass
510 g, FBA single 30.49% of price, 3-pack $3.717/bottle, $4.513 saving, 54.84% reduction, Toronto
77.88%, $281 packaging, 20.13-unit break-even.

Geometry holds: three 2.375 in bottles need a **5.117 in** enclosing circle, so a 6×6 in triangle
leaves 0.88 in slack; S-7369 at 3×3×6 clears the bottle by 0.625 in diametral and 0.563 in height.

**Unresolved conflict:** S-9602 (6×6×6 triangle, 216 in³) versus this repo's box spec (row shipper,
7.769 × 2.673 × 5.798 in, 141.7 in³). Both work; theirs is a real stock SKU, mine was explicitly
not SKU-verified and is 52% more material-efficient. **Two specs in one repo disagree.**

## 4. Not verified, and why

Canada Post rates come from an interactive calculator and Amazon fee pages are login-gated, so
neither is reachable from this session. Unverified here: all Canada Post rates, the 36% Xpresspost
discount and 40% fuel surcharge, no-discount-on-Regular-Parcel, FBA fees $8.23/$11.15, the 3.5%
surcharge, the **270-day beverage expiry band**, FBA Prep ending 2026-07-01, Buy Shipping
unavailability, the glass-breakage exclusion, all Uline pricing, and peak fees.

> The authoring session **fabricated these same figures once** and labelled them
> "[High confidence, retrieved]" before self-correcting. This note is **not** independent
> confirmation of the re-run. **The 270-day band is the one worth checking twice**, being the only
> unverified claim that could kill the channel outright.

---

# Addendum — verification of v1.1 (2026-09-06)

v1.1 is a genuine improvement. The verification-status section is honest about what is sourced,
what is inferred and what is estimated, and the FBA fee corrections are material and in the right
direction. Arithmetic recomputes clean: $7.40 × 1.035 = $7.66, $10.50 × 1.035 = $10.87, the $4.04
consolidation saving, 53%, the 79% Toronto uplift, and the 41.5% fuel surcharge applied to the v1.0
base rates. Three genuinely new and valuable findings: the expiry **date-format conflict**, the
31 March 2026 **barcode rule change**, and the recommendation to **file the trademark**.

## 1. The fee quotes rest on a superseded bottle weight

v1.1 still uses **175 g glass + 6 g cap = 510 g filled**. Uline's own listing for S-23397 gives a
unit weight of **0.46 lb (0.21 kg) = 209 g with the cap included and shipped attached**, so the
filled bottle is **540 g**. That was verified after v1.1 was written.

| | v1.1 | Corrected |
|---|---|---|
| Packaged single | 535 g | **565 g** |
| Packaged three-pack | 1,620 g | **1,710 g** |

**This matters more here than a 6% error normally would, because v1.1 itself identifies the single
as band-sensitive.** It notes 535 g sits in the 500–600 g row at $7.40 base and warns that heavier
bubble wrap tips it into 600–700 g at $7.71. At the corrected 565 g the headroom to that break is
**35 g** — about one sheet of bubble wrap, which is mandatory for a fragile container over 120 mL.
That is a coin flip, not a margin, and it costs **$0.32 per bottle** if it lands wrong.

The three-pack moves 90 g. Standard-size rows step every 100 g in this range, so **$10.87 is not
safe as quoted.**

**The conclusion survives; the dollar figures do not.** Even if the three-pack fee rose a full
dollar, consolidation would still save $3.70 per bottle, 48%, and remain the largest lever in the
model. Requote both configurations at 565 g and 1,710 g.

## 2. Three date formats, and a box that cannot carry them

v1.1 correctly identifies that Amazon accepts `MM-DD-YYYY` or `MM-YYYY` while the label carries the
CFIA bilingual convention. It is resolvable — Amazon's rule is to sticker over the original — but the
follow-through is not costed. An FBA unit needs the brand seal, an FNSKU label, an expiry sticker,
the expiry again outside the bubble wrap, and the expiry on the outer box at 36 pt.

**That is incompatible with "plain white, no print" as written in the box spec**, and with the
sticker spec's brand-only rule. Nothing has to be reordered, but roughly **240 hand applications,
about 80 minutes**, sit in the "not modelled" column alongside labour. Both specs now say so.

## 3. Two corrections from the v1.0 review that did not carry into v1.1

- **Shrink band is still $0.03**, so COGS is still $4.60. S-17668 is **$26.00 per carton** on order
  53425173: $0.052 to $0.104 per band. `pricing/bb_channel_model.py` has been corrected to $0.104
  and reads $4.67; the document has not.
- **The three-pack still has no GTIN of its own.** v1.1 discusses barcodes at length and says
  "your GTIN must come directly from GS1… yours does" — singular. A three-pack sold as its own ASIN
  is a distinct trade item and needs a second GTIN. Recommendation 3 ships the pilot as three-packs.
  Still unbudgeted, still unscheduled.
