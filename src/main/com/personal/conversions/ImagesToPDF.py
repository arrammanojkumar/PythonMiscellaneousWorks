#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# ###################################################################################
#                                                                                   #
# File:       ImagesToPDF.py                                                        #
# Created:    Manoj Kumar Arram                                                     #
#                                                                                   #
#####################################################################################
# Import All required libraries

"""
Create a pdf from images
"""

from fpdf import FPDF
import os


class ImagesToPDF:

    def __init__(self):
        print "Constructor"

    def convertToPDF(self, current_dir):
        if len(current_dir) < 1:
            return "Wrong Path"

        pdf = FPDF('P', 'mm', 'A4')
        x, y, w, h = 0, 0, 200, 250

        for r, d, f in os.walk(current_dir):
            for image in f:
                if ".jpeg" in image or ".png" in image or ".jpg" in image:
                    image = os.path.join(r, image)
                    pdf.add_page()
                    pdf.image(image, x, y, w, h)

        pdf_file_name = current_dir.split('/')[-1]+'.pdf'

        print "PDF Saved at location : ", os.path.join(current_dir, pdf_file_name)
        pdf.output(os.path.join(current_dir, pdf_file_name), "F")

        return "Success"
