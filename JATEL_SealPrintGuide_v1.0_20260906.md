# Bench & Bloom — Box seal: home printing guide

**Document:** JATEL_SealPrintGuide_v1.0_20260906
**Supersedes** the trade-print approach in `JATEL_SealStickerSpec_v1.0_20260906.md` (§4 material,
§6 ordering). The **compliance rule in §1 of that spec still governs** and is repeated below.
**Files:** `sticker/`

---

## 1. Size: 2 inch round, one size for both boxes

| Box | Seal face | 2 in seal | Verdict |
|---|---|---|---|
| Single, S-7369 (3 × 3 × 6 in) | 3 in wide | 67% of the face, 0.5 in margin each side | Reads as a wax seal. Right. |
| Three-pack, S-9602 (6 × 6 × 6 in) | 6 in wide | 33% of the face, 2 in margin | Reads as a seal on a large field. Right. |

**Use one size.** One template, one sheet type, one artwork file, nothing to mix up mid-run. 2 in
round is the most widely stocked round label size, typically **12 per sheet** on US Letter.

Apply it **across the closure**, not centred on a face — half on the tuck flap or lid, half on the
panel below. That is what makes it a seal rather than a decoration.

*If you later want the three-pack bolder, 2.5 in is the size to add alongside, not to replace with.*

## 2. What to buy

- **2 inch round labels, US Letter, matte white**, laser or inkjet to match your printer.
- **Laser is better** if you have the choice: toner is fused and shrugs off a damp hand. Inkjet on
  matte label paper will smudge if it meets moisture.
- **Matte, not gloss.** Gloss fights the brand and shows fingerprints.
- Common template families are Avery's 2 in round range and equivalents from Staples or Amazon
  house brands. **Confirm "2 inch / 50.8 mm round" on the package** rather than trusting a template
  number — I have not verified any specific product code.
- **Quantity:** 48 singles + 16 three-packs = **64 needed. Buy 120** (10 sheets at 12 up). Hand
  application wastes some, you will want spares for photography, and the second pack is pennies.

## 3. The design, and why it looks like that

`sticker/BenchAndBloom_BoxSeal_2in.pdf` — sprig mark, **Bench & Bloom** in Fraunces, a thin gold
rule, **NARAMATA BENCH BOTANICALS** in tracked Inter. Gold ring inset 0.155 in from the die cut.

**Nothing is printed within 0.155 in of the cut line, and that is the whole design constraint.**
A home printer cannot register perfectly against a pre-cut die. Any ink that runs to the edge will
show white slivers on one side and get trimmed on the other. So the label stock is left bare as the
background, and the only edge-adjacent element is a ring that sits comfortably inside the cut. This
is the single biggest difference from a trade-printed label, which would bleed.

Consequences worth knowing:
- **Do not "fix" the design by adding a filled background.** It will look worse, not better.
- Your printer will not match `#5A4A78` exactly. It does not matter here: there is no large flat
  field for a colour cast to show in, which is another reason this design suits home printing.

## 4. Files

| File | Use |
|---|---|
| `BenchAndBloom_BoxSeal_2in.pdf` | **One seal, exact 2 in.** Best source for Avery Design & Print, Word or Pages label templates. |
| `BenchAndBloom_BoxSeal_2in_600dpi.png` | 1200 × 1200 px (600 dpi). For tools that want an image. |
| `BenchAndBloom_BoxSeal_2in_Sheet12up_Letter.pdf` | **12 up on Letter**, 3 across × 4 down, faint dashed cut guides. Fallback if you would rather print a whole sheet than use a template. |
| `*.html` | Editable sources. Fonts are embedded base64, so they render anywhere. |

**Prefer the template route.** Load `BenchAndBloom_BoxSeal_2in.pdf` or the PNG into your label
software and let *its* template own the positions. The template knows your specific product's grid;
my 12-up sheet assumes a common one and may not match your stock exactly.

## 5. Before you print 10 sheets

1. **Print one page on plain paper.** Hold it against a label sheet up to a window. The circles must
   line up. If they do not, use the template route instead of the 12-up sheet.
2. Set the printer to **Actual size / 100% scale**. "Fit to page" will shrink it a few percent and
   nothing will line up.
3. Turn **off** any borderless or edge-to-edge setting.
4. Print **one label**, stick it on a real carton flap, and look at it. Then print the rest.
5. Let toner or ink set for a minute before stacking.

## 6. The rule that still governs (carried from the sticker spec)

**Brand only. No product identity, no claims, no net quantity, no barcode.**

The moment this carries the common name, a nutrition claim or a net quantity, it stops being
decoration and becomes **part of the label**, which pulls bilingual mandatory-information
requirements onto a two-inch circle that cannot hold them. Mark, wordmark, descriptor: safe.
"Lavender Syrup", "250 mL", any sugars reference: not.

> ⚠️ **This collides with the three-pack plan.** A three-pack sold on Amazon needs **its own GTIN**,
> and a barcode is product identity. It cannot go on this seal and the box spec says the box is
> unprinted. **Decide where the three-pack barcode lives before ordering boxes.** See
> `JATEL_ChannelCostingVerification_v1.0_20260906.md` §1.

## 7. Regenerating

`scratchpad/build_seal.py` builds all four files: it embeds the Fraunces and Inter woff2 from
`node_modules/@fontsource/`, lays out the seal in CSS at exact inch dimensions, and renders through
headless Chrome. Same pattern as the wrap label. Edit the CSS block and re-run.

**Not verified:** no label product code, price or sheet grid has been confirmed. Sizes and materials
are specified by property, as with the boxes.
