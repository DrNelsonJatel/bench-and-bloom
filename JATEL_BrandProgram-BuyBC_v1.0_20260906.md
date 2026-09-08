# Brand program: Buy BC

**Document:** JATEL_BrandProgram-BuyBC_v1.0_20260906
**Recommendation:** apply. It is **free**, it is the right programme, and eligibility turns on a
decision you have not yet made.

## What it is, and why it is the right one

There is **no national membership programme** for "Made in Canada". Those words are a *claim* under
CFIA rules, not a club you join, and there is no logo to license. Ontario has **Ontario Made**, but it
requires the last substantial transformation to occur in Ontario, so it is closed to you.

**Buy BC** is the B.C. Ministry of Agriculture's programme. Over 1,000 B.C. businesses use the mark
on more than 10,000 products, the **logo licence is free**, and producers, processors and
cooperatives are eligible. Apply at **buybc.gov.bc.ca/join-buy-bc/**.

## ⚠️ Eligibility is a coin flip, and you control the coin

Buy BC uses a **cost** test, not the mass test that already disqualified you from "Product of
Canada": **51% or more of total direct production cost must originate in B.C.**, counting raw
material, direct labour, variable processing and packaging.

| | $/bottle | B.C.? |
|---|---|---|
| Direct labour | 1.50 | **yes** |
| Estate lavender + water | 0.25 | **yes** |
| **Wrap label** | **1.00** | **only if printed in B.C.** |
| **Retail box + seal sticker** | **0.60** | **only if bought in B.C.** |
| Glass bottle w/ cap (Uline, Lacey WA) | 1.70 | no |
| Inbound freight | 0.87 | no |
| Cane sugar | 0.47 | no |
| Shrink band, citric acid, butterfly pea | 0.13 | no |

| Scenario | B.C. share | Result |
|---|---|---|
| Label and packaging bought outside B.C. | 26.8% | fails |
| One of the two in B.C. | 39.1% | fails |
| **Both in B.C.** | **51.3%** | **qualifies** |

**The label and the boxes are the swing, worth 25 percentage points.** Every box supplier already
quoted is in B.C. (Racer, BC Box, OK Eco-Packaging), and the seal-sticker quote is Vancouver. **You
are one sourcing decision away from qualifying, and you were probably going to make it anyway.**

> **[Moderate confidence.]** These cost splits are this project's own estimates and the $1.50 labour
> figure is unverified. Buy BC requires their **Direct Cost of Producing Products Calculator**, which
> may treat freight and labour differently. **Run their calculator before assuming the answer.**

## Status on the site

The logo is **licensed** and must not appear before the licence is granted — the same rule this
project already applies to the Bee Friendly Farming mark. So:

- `BUY_BC.licensed` in `src/consts.ts` is **false**, and the logo block on `/syrup` is gated behind
  it. Flip it to `true` when the licence arrives and the mark appears in both languages.
- The copy guard **fails the build** if a Buy BC mark reaches published output while unlicensed.
- A **truthful provenance section is live now** in English and French. It says the lavender is grown
  on the bench and the syrup is made in the Okanagan, and it says plainly that the cane sugar is
  imported and that the bottle therefore reads "Made in Canada from domestic and imported
  ingredients" rather than "Product of Canada". Owning that is better positioning than dodging it.

## What to do

1. **Run the Direct Cost of Producing Products Calculator** with real figures.
2. **Buy the label and the boxes in B.C.** if the numbers are close, which they are.
3. **Apply** at buybc.gov.bc.ca/join-buy-bc/. Free, no downside.
4. When the licence lands: add the logo file, flip `BUY_BC.licensed`, and the block appears.

**Not verified:** whether Buy BC accepts a producer below the $30,000 revenue bar (that threshold is
stated for the separate *Partnership Program* funding stream, not for the logo licence), and their
exact treatment of freight and owner labour.
