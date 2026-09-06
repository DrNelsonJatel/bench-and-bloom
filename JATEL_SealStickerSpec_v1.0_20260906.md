# Bench & Bloom — Box Seal Sticker Specification

**Document:** JATEL_SealStickerSpec_v1.0_20260906
**Status:** First issue.
**Purpose:** The single branded element on an otherwise plain white box. Seals the closure flap on
both the single-bottle carton and the three-bottle shipper, and makes the box unmistakably ours.
**Companions:** `JATEL_BoxPackagingSpec_v1.0_20260906.md`, `JATEL_ProductSpec_v1.0_20260906.md`.

---

## 1. The one compliance rule that governs this design

**Keep the sticker brand-only. No product identity, no claims, no ingredients, no net quantity.**

Under Canadian food labelling rules, a "label" is any legend, word or mark applied to a prepackaged
product. The moment this sticker carries the common name, a nutrition claim, an ingredient reference
or a net quantity, it stops being decoration and becomes **part of the label**, which drags bilingual
requirements and mandatory-information rules onto a 2-inch circle that cannot carry them.

**Safe on the sticker:** the sprig mark, the wordmark "Bench & Bloom", the descriptor "Naramata Bench
Botanicals", the website, a decorative rule.
**Not on the sticker:** "Lavender Syrup", "250 mL", "no essential oils", "earthy and warm", any
sugars reference, any nutrition or health claim, any origin claim.

*"Naramata Bench Botanicals" is a house descriptor rather than an origin claim, and the website is an
address rather than a claim, so both are safe. If in doubt, drop to mark plus wordmark only.*
**[Moderate confidence. This is the kind of line the CFIA Industry Labelling Tool settles in ten
minutes, and it is worth asking while you are in there for the label.]**

---

## 2. Size: one size, both boxes

| Box | Closure face | Sticker |
|---|---|---|
| Single carton | 2.500 in wide tuck flap | **2.0 in** round |
| Three-bottle shipper | 7.75 in wide centre seam | **2.0 in** round |

**Order one size: 2.0 in (50.8 mm) round.**

On the single carton a 2.0 in circle centred on the 2.5 in flap leaves 0.25 in of white either side,
which reads deliberate rather than tight. On the shipper the same circle sits centred over the tape
seam and reads as a wax-seal gesture against a much larger white field, which is the effect you want.

Two sizes would mean two SKUs, two minimum order quantities and two artboards, to solve a problem
that does not exist. **[If you later want the shipper to read bolder, 2.5 in is the size to add, not
to replace with.]**

---

## 3. Artwork

- **Shape:** circle, 2.0 in diameter.
- **Bleed:** 0.0625 in (1.6 mm) beyond the cut line. Circles are cut on a rotary die and drift
  slightly, so the background must run past the edge.
- **Safe zone:** keep all artwork **0.125 in inside** the cut line. Nothing important within
  0.125 in of the edge.
- **Ground:** **Chalk White `#F7F3EE`**, full bleed. Matches the label ground so the sticker and the
  bottle read as one system.
- **Content, centred and stacked:**
  1. Sprig mark (lavender buds + sage stem)
  2. **Bench & Bloom** in Fraunces, Lavender Deep `#5A4A78`
  3. Thin Bench Gold `#C2A05E` rule
  4. NARAMATA BENCH BOTANICALS in Inter, tracked caps, Gold Deep `#7A5E28`
  5. *optional* benchandbloom.com in Inter, small, Ink Soft `#5A5266`
- **Fonts:** Fraunces and Inter, **outlined to vector** before output.
- **Minimum type size:** nothing below **5 pt** after scaling to 2.0 in. The descriptor and URL are
  the two that will want to go too small; drop the URL before you shrink the descriptor.

### Palette (carried from the label spec, unchanged)

| Role | Name | HEX | CMYK |
|---|---|---|---|
| Ground | Chalk White | `#F7F3EE` | 0 / 2 / 4 / 3 |
| Wordmark | Lavender Deep | `#5A4A78` | 25 / 38 / 0 / 53 |
| Rule / accent | Bench Gold | `#C2A05E` | 22 / 31 / 70 / 4 |
| Descriptor | Gold Deep | `#7A5E28` | 22 / 41 / 90 / 36 |
| Sprig stem | Sage | `#8A9A78` | 26 / 9 / 40 / 16 |
| Small text | Ink Soft | `#5A5266` | 12 / 19 / 0 / 60 |

---

## 4. Material

- **Face stock:** **matte white paper**, not film. This sticker lives on a dry paperboard box in a
  parcel, not on a bottle in a fridge, so the waterproof BOPP specified for the label is unnecessary
  cost here. Matte paper also takes a hand-written lot number if you ever want that.
- **Adhesive:** **permanent**, rated for corrugated and coated paperboard. Say "for corrugated" to
  the printer; general-purpose paper adhesive can lift off a coated SBS carton in cold transit.
- **Finish:** matte or uncoated. **No gloss laminate**, for the same reason as the label.
- **Format:** **rolls**, not sheets. A roll is faster to apply by hand and does not curl. Ask for
  them wound **face out** with a 3 in core.
- **Alternative worth pricing:** **kraft** face stock instead of chalk white. It suits the
  wine-country positioning and hides scuffing better in transit. Get both quoted; the cost is
  usually identical.

---

## 5. Tamper evidence

A seal sticker across a closure **is** informal tamper evidence: the box cannot be opened without
visibly tearing or lifting it. That is proportionate for a food product going direct to consumers and
matches what small producers do.

**It is not a tamper-evident seal in the regulatory sense, and the product does not need one**, because
the bottle already carries the **shrink band (Uline S-17668)** over the cap. The band is the actual
tamper evidence and it stays. Do not let the sticker be treated as a substitute for it.

If you ever want the sticker itself to be genuinely tamper-evident, the stock is **destructible
vinyl**, which shatters on removal. It costs more, cannot be repositioned during hand application,
and is overkill for a 48-bottle pilot. Not recommended now.

---

## 6. Quantity and ordering

- **Pilot need:** 48 singles + 16 three-packs = **64 stickers minimum.**
- **Order 150.** Hand application wastes some, you will want spares for photography and samples, and
  the price break between 100 and 250 is usually small enough that the second hundred is nearly free.
- Typical suppliers for a run this size: StickerYou, Jukebox, Avery WePrint, or the same trade
  printer doing the wrap label. **Ask the label printer to quote both together**, since it is one
  setup and one shipment.

> **No supplier SKU or price is quoted here, because I have not verified any.**

---

## 7. Pre-print checklist

- [ ] Confirm with the CFIA Industry Labelling Tool that a brand-only sticker is not "label" copy (§1)
- [ ] Outline Fraunces and Inter to vector
- [ ] Confirm 0.0625 in bleed and 0.125 in safe zone with the printer's template
- [ ] Check the smallest type at final 2.0 in size on a **printed proof**, not on screen
- [ ] Confirm permanent adhesive rated for **corrugated**
- [ ] Order on rolls, face out
- [ ] Apply one to a real carton flap and one to a taped shipper seam before ordering quantity
- [ ] Price chalk white against kraft

---

## 8. Open items

| # | Item | Owner |
|---|---|---|
| 1 | Confirm the §1 brand-only determination with CFIA | Nelson |
| 2 | Decide chalk white vs kraft | Nelson |
| 3 | Decide whether the URL stays on the 2.0 in artboard or is dropped for legibility | designer |
| 4 | Produce the artboard from the existing outlined logo lockup | designer |
| 5 | Quote alongside the wrap label as one job | Nelson |

---

## 9. Provenance

- **[High confidence, computed]** Sizing against the carton and shipper faces in
  `JATEL_BoxPackagingSpec_v1.0_20260906.md`.
- **[High confidence, carried]** Palette, fonts and the shrink-band SKU, from
  `singlelabel/Label_PrinterSpec_Wrap_uline2026.md`.
- **[Moderate confidence, training]** The §1 determination on when a sticker becomes label copy, and
  the tamper-evidence framing. Both are the general shape of Canadian practice, neither is quoted
  from a specific regulation. Item 1 closes this.
- **[Not verified]** No supplier, SKU, price or lead time.
