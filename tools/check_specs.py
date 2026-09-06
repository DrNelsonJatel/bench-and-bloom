#!/usr/bin/env python3
"""
Bench & Bloom — spec consistency checker.

These specs have been revised many times, by more than one author, and at least once
a corrected block reverted underneath us. This asserts that the facts of record agree
across every document, so a stale figure cannot quietly survive in one file.

  python3 tools/check_specs.py
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS = ["JATEL_ProductSpec_v1.0_20260906.md",
         "singlelabel/Label_PrinterSpec_Wrap_uline2026.md",
         "JATEL_BoxPackagingSpec_v1.0_20260906.md",
         "JATEL_SealStickerSpec_v1.0_20260906.md"]

# Text that must NOT appear outside a superseded/before-after context.
FORBIDDEN = [
    ("stale-brix-precision",   r"64\.8",            "Brix is stated as 64; no decimal"),
    ("wrong-postal-code",      r"V0H\s*1N0",        "farm postal code is V0H 1N1"),
    ("home-address",           r"Bernard\s*Ave|V1Y\s*6P7", "home address must never appear"),
    ("printed-date-in-art",    r"Packaged\s*/\s*Emball[ée]:\s*YYYY", "no date prints; coding panel is blank"),
    ("old-lot-only-format",    r"LOT:\s*2026-001",  "lot format is YYYYMMDD-nn"),
    ("stale-serving-15ml",     r"per\s*15\s*mL",    "prescribed serving is 30 mL"),
    # only flag "not required" when REQUIRED does not also appear on the line,
    # so the July-vs-current comparison rows do not trip it
    ("stale-fop-not-required", r"(?!.*REQUIRED).*symbol[^.]{0,40}not\s+required",
                               "the sugars symbol IS required"),
]
# Context words that legitimise a forbidden match (before/after tables, supersession notes).
EXCUSE = re.compile(r"supersed|July artwork|previously|was wrong|~~|abandoned|prior version|"
                    r"old two-label|corrected|WRONG|historical|\| ~14\.5 \||"
                    r"existing artwork|artwork prints|artwork currently|must not print|"
                    r"is confirmed wrong|fix in the redraw|STALE|do not use", re.I)

# Facts that MUST appear somewhere in the named file.
REQUIRED = [
    ("JATEL_ProductSpec_v1.0_20260906.md", r"3820 Partridge Rd",           "farm address"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"V0H\s*1N1",                   "farm postal code"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"STATE AS ≤ 3\.5",              "pH of record (reverted once by an outside edit — keep asserting it)"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"351",                          "batch 2026-001 hue of record"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"coding panel",                 "coding panel, not printed dates"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"YYYYMMDD-nn",                 "lot format"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"NOT printed on the label",    "pH/Brix off-label decision"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"30 mL",                       "prescribed serving"),
    ("JATEL_ProductSpec_v1.0_20260906.md", r"rounding boundary",           "NFt sensitivity warning"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"3820 Partridge Rd", "farm address"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"51 × 12\.5 mm",  "coding panel size"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"coating knockout", "the ink-on-BOPP fix"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"REQUIRED",       "sugars symbol required"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"lavender-milk",  "QR repointed"),
    ("singlelabel/Label_PrinterSpec_Wrap_uline2026.md", r"Made in Canada", "origin claim"),
]

fails = 0
def flag(msg):
    global fails; fails += 1; print(f"  [FLAG] {msg}")

print("="*76); print("SPEC CONSISTENCY"); print("="*76)
for rel in SPECS:
    p = ROOT / rel
    if not p.exists():
        flag(f"missing spec: {rel}"); continue
    lines = p.read_text().splitlines()
    for name, pat, why in FORBIDDEN:
        for i, line in enumerate(lines, 1):
            if re.search(pat, line, re.I) and not EXCUSE.search(line):
                flag(f"{rel}:{i}  {name} — {why}\n         {line.strip()[:100]}")
print("  forbidden-text scan complete")

for rel, pat, why in REQUIRED:
    p = ROOT / rel
    if not (p.exists() and re.search(pat, p.read_text(), re.I)):
        flag(f"{rel}  MISSING required fact: {why}  ({pat})")
print("  required-fact scan complete")

print(f"\n{fails} FLAG(s).")
sys.exit(1 if fails else 0)
