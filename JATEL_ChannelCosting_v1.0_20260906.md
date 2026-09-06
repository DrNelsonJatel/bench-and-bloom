# Bench & Bloom: Channel and Pack-Format Costing, 2026 Pilot

**Document:** JATEL_ChannelCosting_v1.0_20260906
**Question:** Amazon versus Canada Post for the 48-bottle pilot, and single bottle versus three-pack.
**Model:** `bb_channel_model.py` (accompanies this file). All figures CAD, pre-tax. GST/HST on shipping and Amazon fees is recoverable as input tax credits for a GST-registered business, so it is excluded throughout.
**Supersedes:** `pricing/Pricing_benchandbloom_2026.md`, which assumed a $5.00 FBA fee and a refrigerated product.

## 1. Answer to the headline question: there is no new Canada Post program

Canada Post's corporate news releases for 2025 and 2026 contain no new shipping program for Canadian businesses. Every release in that window is financial results, labour relations, or network restructuring. The only small-business item is a marketing contest.

What exists, and what you are almost certainly thinking of, is **Solutions for Small Business**, which has run for years. It is free, has no minimum volume and no contract, and assigns a savings level 1 to 4 that is reassessed quarterly on trailing-twelve-month spend.

Enrol anyway. It is free and there is no downside. But enrol for the right reason, which is not the one the marketing implies.

### The counterintuitive part

| Service | Level 1 discount | Level 4 discount |
|---|---|---|
| Priority | 16% | 28% |
| **Xpresspost** | **36%** | **45%** |
| Expedited Parcel | 31% | 38% |
| **Regular Parcel** | **none, not in the table** | **none** |

Regular Parcel is the cheapest published service and receives no small-business discount at all. Xpresspost receives 36% at the entry level. The result is that **discounted Xpresspost beats undiscounted Regular Parcel on price and on speed** for a single bottle to every destination tested.

### 2026 reliability context

The 2025 CUPW overtime ban and national strike cut parcel revenue roughly 40% and contributed to a $1.57 billion pre-tax loss for 2025. Contracts were ratified in June 2026 and run to 31 January 2029, so strike risk is off the table for the pilot window. Q2 2026 still showed a $277 million loss but with parcel recovery. The financial distress is real; it has not produced parcel service withdrawal.

## 2. Amazon has no Canadian shipping program either

- **Amazon Shipping**, the courier service merchants can buy for their own orders, does not operate in Canada. Service areas are the US, UK, France, Italy, Spain and India.
- **Amazon Buy Shipping is unavailable for domestic shipping in Canada.** Amazon's own carrier coverage page says so outright; the only Canadian carrier listed is China Post for international inbound. A merchant-fulfilled Canadian seller gets no discounted postage from Amazon. None.
- There is no seller-side "Buy Canadian" program. The Made in Canada storefront is customer-facing merchandising, and its intake route could not be verified as still working.

So for a Canadian seller, "Amazon's program" means **FBA**, and nothing else.

There is one real incentive: new brand-registered sellers get 10% back on the first $70,000 of branded sales. That requires Brand Registry, which requires a registered or pending trademark you own.

## 3. Unit economics

Landed COGS per bottle **$4.60**: bottle with cap $1.70 (Uline S-23397 at 3+ cases, caps included), shrink band $0.03, wrap label $1.00, syrup $1.00, allocated inbound freight $0.87. Note the old pricing sheet's separate $0.15 cap line should be removed, since the Uline bottle ships with its cap; the saving is offset by sugar rising 5.9x under the new formulation.

Filled bottle **510 g**: 175 g glass (published spec for this bottle), 329 g syrup (250 mL at the verified 1.316 g/mL), 6 g cap.

### Retail packaging

| Item | Product | Unit cost |
|---|---|---|
| Single bottle carton | Uline **S-7369** kraft reverse tuck, 3 x 3 x 6 in interior, $95/250 | **$0.38** |
| Single, giftable alternative | Uline **S-16852** white gloss gift box, 3 x 3 x 6 in, $54/100 | $0.54 |
| Three-pack box | Uline **S-9602** kraft pinstripe gift box, 6 x 6 x 6 in, $81/100, holds three in a triangle | **$0.81** |
| Three-pack, row format | Uline **S-15134** kraft reverse tuck, 8 x 3 x 8 in, $198/250 | $0.79 |
| Seal sticker | Jukebox Print 2 in circle vinyl, $105/250, Vancouver, 1-day production | **$0.42** |
| Seal sticker, cheaper at volume | StickerYou, $110.97/500 | $0.22 |

Two traps worth naming. Uline lists reverse tuck cartons by **interior** dimension but gift boxes by **exterior**, so they are not directly comparable. And several boxes that look right are 5 in interior, which is 0.44 in too short for this bottle; do not order S-8395, S-11609, S-11615, S-16329 or S-18296.

**No stock three-cell divider exists in Canada for a 2.375 in bottle.** Uline's bottle partitions are cut for 3 to 3.5 in wine bottles. A fitted insert has to be custom die-cut. The triangle arrangement in a 6 x 6 x 6 box avoids needing one.

**No molded pulp shipper exists for an 8 oz Boston round.** Uline's certified pulp shippers are cut for 750 mL wine bottles, 13.5 in tall and 3.25 in diameter. Your bottle would rattle loose in the cavity, which voids the point of the certification. Use foam pouch plus a heavy-grade outer instead: Uline S-5321 foam pouch $0.16, into a 275 lb heavy-duty 6 x 6 x 6 (S-4876, $1.51 at MOQ 25, $1.19 at 250). Do not use the 32 ECT lightweight boxes for glass.

## 4. The comparison

Canada Post quotes are live from the rate calculator on 2026-09-06, origin V0H 1N1, pre-tax, including the 40% fuel surcharge in effect that day. Xpresspost figures apply the Level 1 discount of 36% to the base rate before fuel.

### Shipping cost per parcel

| Destination | Regular, 1 bottle | Xpresspost L1, 1 bottle | Regular, 3-pack | Xpresspost L1, 3-pack | XP 3-pack per bottle |
|---|---|---|---|---|---|
| Kelowna | $17.35 | **$11.92** | $17.58 | **$14.19** | **$4.73** |
| Vancouver | $20.62 | **$13.94** | $21.28 | **$16.63** | **$5.54** |
| Toronto | $27.76 | **$21.02** | $29.51 | $30.60 | **$10.20** |

Xpresspost wins outright for single bottles everywhere, and for three-packs to Kelowna and Vancouver. For a 2 kg parcel to Toronto, Regular Parcel is $1.09 cheaper but takes 7 days against 3.

### Net contribution per bottle

Retail $26.99 single, $72.99 three-pack (a 10% multi-buy discount off 3 x $26.99). Direct-channel rows use Vancouver as the representative destination and include payment processing at 2.9% plus $0.30.

| Scenario | Net per bottle | Across 48 bottles |
|---|---|---|
| Direct, single, buyer pays shipping | **$18.28** | $877 |
| Direct, three-pack, buyer pays shipping | **$17.51** | $840 |
| Direct, three-pack, free shipping | **$12.12** | $582 |
| Amazon FBA, three-pack | **$10.61** | $509 |
| Amazon FBA, single | **$7.95** | $382 |
| Direct, single, free shipping | **$4.75** | $228 |

Amazon FBA rows carry: 15% Grocery referral, fulfilment fee including the 3.5% fuel and logistics surcharge in effect since 17 April 2026, storage, self-applied prep materials, and $1.10 per bottle of allocated inbound freight to the fulfilment centre. That last figure is an **estimate** and is the least certain input in the model.

### The single biggest lever is the pack format, not the channel

| | Amazon fulfilment fee | Per bottle |
|---|---|---|
| Single bottle, 800 g shipping weight | $8.23 | **$8.23** |
| Three-pack, 2,000 g shipping weight | $11.15 | **$3.72** |

**Consolidating into a three-pack cuts Amazon's fulfilment cost by $4.51 per bottle, a 55% reduction.** Both configurations sit in the Standard size tier and neither is dimensional-weight bound. Nothing else in this model moves the number that much.

The same effect appears on Canada Post: a three-pack to Vancouver costs $5.54 per bottle to ship against $13.94 for a single.

At $8.23, Amazon's fulfilment fee is **30.5% of the single-bottle retail price**, which is outside the healthy range for a packaged good. The three-pack brings it to 13.8%.

### What this means

Single-bottle direct-to-consumer is not viable. Shipping one bottle to Toronto costs $21.02 against a $27 product. Either the customer refuses a 78% shipping uplift, or you absorb it and net $4.75.

The two realistic options are close: **direct three-pack with free shipping at $12.12 per bottle, and Amazon FBA three-pack at $10.61.** Direct is $1.51 per bottle better, but only if you supply all the traffic yourself. Amazon costs $1.51 to rent the demand. For a 48-bottle validation run whose purpose is to learn whether anyone wants this, that is cheap.

## 5. Five things that could stop the Amazon route

1. **FBA Prep Service and item labelling ended in Canada on 1 July 2026.** Amazon will no longer bubble-wrap or label at any price. A fragile container of 120 mL or more **must** be bubble-wrapped, so all 48 bottles are wrapped and labelled by hand, by you. Shipments arriving unprepped are not eligible for damage reimbursement.
2. **Expiration dating is the real constraint.** Amazon requires remaining shelf life at check-in of 270 days for beverages, or 365 days for jams and preserves. A lavender syrup is not explicitly assigned to a band. With a 12-month best-before, the 365-day band is **arithmetically impossible** and the 270-day band leaves roughly 95 days from bottling to check-in. Confirm the band with Seller Support before bottling, not after.
3. **Grocery is a gated category on amazon.ca.** Approval takes 2 to 7 business days and requires invoices dated within 180 days, photos of all sides, and safety certifications. The invoice requirement is written for resellers and does not address the own-brand case. A rejection cannot be appealed.
4. **Stickerless operation requires Brand Registry plus a valid GS1 GTIN.** You have the GTIN (627146286305). Brand Registry needs a registered or pending trademark. Without it, apply FNSKU labels yourself, which for 48 units is fine.
5. **Peak fees.** From 15 October 2026 to 14 January 2027 the single-bottle fulfilment fee rises to $8.73 and the three-pack to $11.85, and storage roughly doubles.

## 6. And one that could stop the Canada Post route

**Canada Post excludes glass breakage from all coverage, included or purchased.** Their non-insurable contents policy names glass, ceramics, porcelain, mirrors and crystal, and states there is no liability for damage to shipments containing fragile items. The $100 included coverage and the purchasable coverage up to $5,000 both buy you nothing against a broken bottle. Packaging must survive a 1-metre drop onto concrete.

This is the largest uninsured risk in the direct channel and it argues for the heavy-duty outer carton, not the lightweight one. Third-party shipping insurance is the usual workaround.

Separately: if you ever add an alcoholic product, Solutions for Small Business membership becomes **mandatory** rather than optional, since Canada Post only accepts intoxicating beverages from contract or SfSB customers, with Proof of Age on delivery.

## 7. Recommendation

1. **Make the three-pack the primary sellable unit** in both channels. It is worth $4.51 per bottle on Amazon and $8.40 per bottle on Canada Post. Sell singles too, but expect them to be a local and farmgate item, not a shipped one.
2. **Enrol in Solutions for Small Business today.** Free, and it unlocks the 36% Xpresspost discount that makes direct shipping merely painful instead of impossible.
3. **Ship the pilot to FBA as three-packs**, 16 units of three. Resolve the expiration band with Seller Support and start Grocery category approval before bottling, since both have external turnaround you do not control.
4. **Order Uline S-7369 for singles and S-9602 for three-packs**, plus 250 Jukebox seal stickers. Total packaging outlay is roughly $95 + $81 + $105 = $281, which covers well beyond the pilot.
5. **Use the heavy-duty 275 lb outer carton** for anything you ship yourself, given that breakage is uninsurable.

## 8. Confidence and provenance

- **[High confidence, retrieved]** Absence of a new Canada Post program; SfSB discount table; live Canada Post rate quotes; volumetric divisors; glass breakage exclusion; Amazon referral 15% above $20; FBA size tiers and fulfilment fees including the 3.5% surcharge; storage rates; Buy Shipping unavailability in Canada; FBA Prep discontinuation 1 July 2026; bubble-wrap requirement at 120 mL; Grocery gating; Uline and sticker pricing.
- **[Moderate confidence, calculated]** Xpresspost discounted totals assume the fuel surcharge is applied to the discounted base rather than the list base. If Canada Post applies fuel to the list base, discounted Xpresspost rises by roughly 14%, which does not change the ranking.
- **[Low confidence, estimated]** The $1.10 per bottle allocated inbound freight to an Amazon fulfilment centre. Replace with a real quote once the FC assignment is known.
- **[Unverified]** The shelf-life band Amazon assigns to syrup; whether an inbound placement service fee exists on amazon.ca; whether the Made in Canada storefront still accepts submissions; discounted Expedited Parcel pricing, which cannot be quoted without an account.
- **Not modelled:** your own labour, breakage and replacement rate, returns, the $29.99 monthly Professional plan (break-even 20.1 units per month), advertising, and the 10% new-brand rebate.

## 9. References

Canada Post. *Shipping discounts and solutions, Solutions for Small Business.* https://www.canadapost-postescanada.ca/cpc/en/small-business/shipping-discounts.page

Canada Post. *Find a Rate.* https://www.canadapost-postescanada.ca/information/app/far/business/findARate

Canada Post. *Non-insurable contents.* https://www.canadapost-postescanada.ca/cpc/en/support/kb/claims/non-insurable-contents.page

Canada Post. *Corporate news releases.* https://www.canadapost-postescanada.ca/cpc/en/our-company/news-and-media/corporate-news/news-release-list.page

Amazon. *Selling on Amazon fee schedule (amazon.ca).* https://sellercentral.amazon.ca/help/hub/reference/external/G200336920

Amazon. *FBA fulfilment fees.* https://sellercentral.amazon.ca/help/hub/reference/external/G201112670

Amazon. *Product size tiers.* https://sellercentral.amazon.ca/help/hub/reference/external/G201105770

Amazon. *Inventory storage fees.* https://sellercentral.amazon.ca/help/hub/reference/external/G200612770

Amazon. *Packaging liquids* and *Product packaging requirements.* https://sellercentral.amazon.ca/help/hub/reference/external/G200280130

Amazon. *FBA Prep Service discontinued in Canada.* https://sellercentral.amazon.ca/help/hub/reference/external/G201023020

Amazon. *Expiration dates on FBA products.* https://sellercentral.amazon.ca/help/hub/reference/external/G201003420

Amazon. *Carrier coverage (Buy Shipping).* https://sellercentral.amazon.ca/help/hub/reference/external/GFGYZ53UP4QT7BZX

Uline Canada. Product pages for S-23397, S-7369, S-9602, S-16852, S-15134, S-5321, S-4876. https://www.uline.ca

Jukebox Print. *Circle stickers.* https://www.jukeboxprint.com/custom-stickers/circle

StickerYou. *Custom labels, Canada.* https://www.stickeryou.com/en-ca/products/custom-labels/173
