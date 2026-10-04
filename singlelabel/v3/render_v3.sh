#!/usr/bin/env bash
# Render every deliverable from Label_BenchAndBloom_Wrap_v3.html (run build_wrap_v3.py first).
# Document = 190.5 x 76.2 mm (7.5 x 3.0 in) = trim 184.15 x 69.85 mm + 3.175 mm bleed.
set -euo pipefail
cd "$(dirname "$0")"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
N=JATEL_LabelWrap_v3.0_20261003
SRC="file://$PWD/Label_BenchAndBloom_Wrap_v3.html"

# 600 dpi raster: 190.5 mm = 720 CSS px; x 6.25 = 4500 px. 76.2 mm = 288 CSS px -> 1800 px.
"$CH" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=6.25 --window-size=720,288 \
  --virtual-time-budget=5000 --screenshot="$PWD/${N}_600dpi.png" "$SRC" 2>/dev/null
"$CH" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=6.25 --window-size=720,288 \
  --virtual-time-budget=5000 --screenshot="$PWD/${N}_PROOF-guides.png" "$SRC?guides" 2>/dev/null
# Print PDF: vector text and artwork, fonts embedded, RGB.
"$CH" --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=5000 \
  --print-to-pdf="$PWD/${N}_print.pdf" "$SRC" 2>/dev/null

python3 - "$N" <<'EOF'
import sys
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
n = sys.argv[1]
# tag 600 dpi, write JPG and CMYK TIFF
im = Image.open(f"{n}_600dpi.png").convert("RGB")
im.save(f"{n}_600dpi.png", dpi=(600, 600))
im.save(f"{n}_600dpi.jpg", quality=95, subsampling=0, dpi=(600, 600))
Image.open(f"{n}_PROOF-guides.png").convert("RGB").save(f"{n}_PROOF-guides.png", dpi=(600, 600))
# print PDF: one page, set TrimBox and BleedBox (points; 1 mm = 72/25.4 pt)
r = PdfReader(f"{n}_print.pdf"); w = PdfWriter()
pg = r.pages[0]; mm = 72 / 25.4; W, H = 190.5 * mm, 76.2 * mm
pg.mediabox = RectangleObject([0, 0, W, H]); pg.bleedbox = RectangleObject([0, 0, W, H])
b = 3.175 * mm
pg.trimbox = RectangleObject([b, b, W - b, H - b])
w.add_page(pg); w.add_metadata({"/Title": "Bench & Bloom Lavender Syrup 250 mL wrap label v3",
                                 "/Subject": "Trim 184.15 x 69.85 mm, bleed 3.175 mm"})
w.write(f"{n}_print.pdf")
# Vector dieline: trim rectangle in a spot colour named CutContour, separate file
from reportlab.pdfgen import canvas
from reportlab.lib.colors import CMYKColorSep
c = canvas.Canvas(f"{n}_dieline.pdf", pagesize=(W, H))
c.setTitle("Dieline: CutContour at trim 184.15 x 69.85 mm, square corners")
c.setStrokeColor(CMYKColorSep(0, 1, 0, 0, spotName="CutContour", density=1)); c.setLineWidth(0.25)
c.rect(b, b, W - 2 * b, H - 2 * b, stroke=1, fill=0)
c.showPage(); c.save()
EOF
# CMYK TIFF (generic conversion, LZW, 600 dpi) for printers that ask for CMYK raster
magick "${N}_600dpi.png" -colorspace CMYK -compress lzw -density 600 -units PixelsPerInch "${N}_CMYK_600dpi.tif"
ls -la ${N}*
