"""Bench & Bloom: channel + pack-format economics, 2026 pilot.
All CAD, pre-tax (GST/HST recoverable as ITCs for a registered business).
Every rate is sourced; see the accompanying markdown. QAQC block at the end."""

# ---------- physical ----------
GLASS_G, SYRUP_G, CAP_G = 175, 329, 6          # syrup = 250 mL x 1.316 g/mL @ 64 Brix
# GLASS_G 175 is asserted from a published spec; the repo box spec estimates 200. NEITHER IS
# WEIGHED, and 48 bottles are in hand. 25 g/bottle moves the 3-pack by 75 g. Weigh one.
BOTTLE_G = GLASS_G + SYRUP_G + CAP_G

# ---------- COGS per bottle ----------
# shrink_band CORRECTED 2026-09-06: S-17668 is $26.00/CT on order 53425173, not $0.03/band.
# $0.104 at 250/CT, $0.052 at 500/CT. Using 250/CT. Count the carton to settle it.
COGS = dict(bottle_cap=1.70, shrink_band=0.104, wrap_label=1.00,
            syrup=1.00, inbound_freight=0.87)
COGS_B = sum(COGS.values())

# ---------- retail packaging ----------
CARTON_1   = 0.38   # Uline S-7369 kraft reverse tuck 3x3x6 in, $95/250
GIFTBOX_3  = 0.81   # Uline S-9602 kraft pinstripe 6x6x6 in, $81/100
SEAL       = 0.42   # Jukebox 2 in circle vinyl, $105/250

# ---------- ship materials ----------
SHIP_MAT_1 = 0.16 + 1.51 + 0.15   # foam pouch S-5321 + 275lb 6x6x6 S-4876 + void
SHIP_MAT_3 = 0.49 + 1.80 + 0.25   # 3 pouches + heavy-duty 8x8x6 + void

# ---------- Amazon (amazon.ca, Sept 2026, incl. 3.5% fuel/logistics surcharge) ----------
REFERRAL       = 0.15            # Grocery, >$20.00
FBA_FEE_1      = 8.23            # standard size, 800 g shipping weight
FBA_FEE_3      = 11.15           # standard size, 2000 g
FBA_STORE_1    = 0.07            # per unit-month, off-peak
FBA_STORE_3    = 0.17
FBA_PREP_1     = 0.19            # self-applied bubble bag; FBA Prep ended in CA 2026-07-01
FBA_INBOUND_B  = 1.10            # allocated cost of shipping 48 units to an FC (ESTIMATE)

# ---------- Canada Post (live quotes 2026-09-06, origin V0H 1N1) ----------
# Xpresspost base, before the Solutions for Small Business Level 1 discount (36%).
XP_BASE = {"Kelowna": (13.30, 15.84), "Vancouver": (15.56, 18.56), "Toronto": (23.46, 34.15)}
REG_BASE = {"Kelowna": (12.39, 12.56), "Vancouver": (14.73, 15.20), "Toronto": (19.83, 21.08)}
SFSB_XP_L1, FUEL = 0.36, 0.40    # Regular Parcel gets NO SfSB discount

PROC_PCT, PROC_FIX = 0.029, 0.30 # payment processing on own storefront

P1, P3 = 26.99, 72.99            # retail price single / three-pack

def cp(base, disc=0.0):
    return base * (1 - disc) * (1 + FUEL)

print(f"Filled bottle: {BOTTLE_G} g   Landed COGS/bottle: ${COGS_B:.2f}\n")

print("=== CANADA POST, per parcel, pre-tax ===")
print(f"{'dest':10} {'Reg 1btl':>9} {'XP-36% 1':>9} {'Reg 3pk':>9} {'XP-36% 3':>9} {'XP3/btl':>8}")
cp_ship = {}
for d in REG_BASE:
    r1, r3 = (cp(x) for x in REG_BASE[d])
    x1, x3 = (cp(x, SFSB_XP_L1) for x in XP_BASE[d])
    cp_ship[d] = (x1, x3)
    print(f"{d:10} {r1:9.2f} {x1:9.2f} {r3:9.2f} {x3:9.2f} {x3/3:8.2f}")

print("\n=== NET PER BOTTLE BY CHANNEL ===")
rows = []
# Amazon FBA
a1 = P1 - P1*REFERRAL - FBA_FEE_1 - FBA_STORE_1 - FBA_PREP_1 - FBA_INBOUND_B \
     - COGS_B - CARTON_1 - SEAL
a3 = (P3 - P3*REFERRAL - FBA_FEE_3 - FBA_STORE_3 - 3*FBA_PREP_1 - 3*FBA_INBOUND_B
      - 3*COGS_B - GIFTBOX_3 - SEAL) / 3
rows += [("Amazon FBA, single", a1), ("Amazon FBA, 3-pack", a3)]

# Direct, Vancouver as the representative destination
s1, s3 = cp_ship["Vancouver"]
base1 = P1 - COGS_B - CARTON_1 - SEAL - SHIP_MAT_1
base3 = P3 - 3*COGS_B - GIFTBOX_3 - SEAL - SHIP_MAT_3
d1_pay = base1 - (PROC_PCT*(P1+s1) + PROC_FIX)
d3_pay = (base3 - (PROC_PCT*(P3+s3) + PROC_FIX)) / 3
d1_free = base1 - (PROC_PCT*P1 + PROC_FIX) - s1
d3_free = (base3 - (PROC_PCT*P3 + PROC_FIX) - s3) / 3
rows += [("Direct, single, buyer pays ship", d1_pay),
         ("Direct, 3-pack, buyer pays ship", d3_pay),
         ("Direct, single, free shipping",   d1_free),
         ("Direct, 3-pack, free shipping",   d3_free)]

for n, v in sorted(rows, key=lambda r: -r[1]):
    print(f"{n:34} ${v:7.2f}/bottle   x48 = ${v*48:8.2f}")

print("\n=== QAQC ===")
def chk(name, val, lo, hi, unit, why):
    ok = lo <= val <= hi
    print(f"[{'PASS' if ok else 'FLAG'}] {name}: {val:.2f} {unit} (expect {lo}-{hi}) :: {why}")

chk("Filled bottle mass", BOTTLE_G, 480, 560, "g",
    "175 g glass is a published spec; syrup mass follows from the verified 1.316 g/mL density")
chk("Landed COGS", COGS_B, 4.0, 5.5, "$",
    "should land near the $4.65 in the existing pricing sheet; caps are now included, sugar is up")
chk("FBA fee as % of price, single", 100*FBA_FEE_1/P1, 15, 25, "%",
    "above ~30% means the unit is too heavy or too cheap to fulfil profitably")
chk("FBA fee per bottle, 3-pack", FBA_FEE_3/3, 3.0, 4.5, "$",
    "consolidation should cut per-bottle fulfilment by roughly half")
chk("Ship cost as % of order, single to Toronto",
    100*cp(XP_BASE["Toronto"][0], SFSB_XP_L1)/P1, 0, 40, "%",
    "over 40% of order value and the single-bottle direct sale is not viable")
chk("Gross margin, best option", 100*max(v for _, v in rows)/P1, 30, 60, "%",
    "packaged goods target; under 30% leaves nothing for marketing or breakage")

sav = FBA_FEE_1 - FBA_FEE_3/3
print(f"\n[FLAG] 3-pack cuts Amazon fulfilment by ${sav:.2f}/bottle "
      f"(${FBA_FEE_1:.2f} -> ${FBA_FEE_3/3:.2f}), the single largest lever in this model.")
print(f"[FLAG] Regular Parcel carries NO small-business discount. Discounted Xpresspost beats it "
      f"to Toronto by ${cp(REG_BASE['Toronto'][0]) - cp(XP_BASE['Toronto'][0], SFSB_XP_L1):.2f} "
      f"AND arrives in 3 days instead of 7.")
print("[FLAG] Canada Post excludes glass breakage from ALL coverage, purchased or included.")
