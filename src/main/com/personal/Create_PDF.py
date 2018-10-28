from fpdf import FPDF
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-location", help="FOLDER LOCATION PATH")

args = parser.parse_args()

if len(vars(args)) < 1:
    print('Usage python Create_PDF.py -location C://Documents//Scanned_Copies')
    sys.exit(1)

image_list = []
current_dir = args.location
pdf = FPDF('P', 'mm', 'A4')
x, y, w, h = 0, 0, 200, 250

for r, d, f in os.walk(current_dir):
    for file in f:
        if ".jpeg" in file or ".png" in file or ".jpg" in file:
            image = os.path.join(r, file)
            pdf.add_page()
            pdf.image(image, x, y, w, h)

pdf_file_name = current_dir.split('/')[-1]+'.pdf'

print "PDF Saved at location : ", os.path.join(r, pdf_file_name)

pdf.output(os.path.join(r, pdf_file_name), "F")
