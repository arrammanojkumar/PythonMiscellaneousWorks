#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# ###################################################################################
#                                                                                   #
# File:       PdfToImages.py                                                        #
# Created:    Manoj Kumar Arram                                                     #
#                                                                                   #
#####################################################################################
# Import All required libraries

"""
Traverse all files in the given path and converts all pdf to images
"""

import os
from pdf2image import convert_from_path
from shutil import copyfile

current_dir = "Current Directory Path"
extract_dir = "Output Directory Path"

for r, d, f in os.walk(current_dir):
    for file in f:
        if ".pdf" in file:
            pdf = os.path.join(r, file)
            pdf_directory = pdf.split('.')[-2]
            pdf_name = pdf_directory.split("/")[-1]
            pdf_directory = extract_dir+"/"+pdf_name
            print pdf_directory

            try:
                os.makedirs(pdf_directory)
                copyfile(pdf, pdf_directory+"/"+pdf_name+".pdf")
                pages = convert_from_path(pdf, 150)
                pdf_name = pdf_directory.split("/")[-1]
                i = 1
                for page in pages:
                    name = pdf_directory + "/" + pdf_name + "_" + str(i) + ".jpg"
                    print "\t", name
                    i += 1
                    page.save(name, "JPEG")
            except:
                print "Folder Exists"
