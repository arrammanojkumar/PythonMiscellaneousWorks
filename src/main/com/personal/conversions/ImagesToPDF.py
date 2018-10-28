import os
from pdf2image import convert_from_path
import zipfile
current_dir = "/Users/marram/Downloads/Pun_Files/manu_pdf_files"
extract_dir = "/Users/marram/Downloads/Pun_Files/manu_pdf_files/Pdf_images"

# current_dir = "/Users/marram/Downloads/Pun_Files/manu_pdf_files/ZIP_FILES"
# extract_dir = "/Users/marram/Downloads/Pun_Files/manu_pdf_files/ZIP_FILES/All_Files"
j = 1

# for r,d,f in os.walk(current_dir):
#     for file in f:
#         if '.zip' in file:
#             try:
#                 path_to_zip_file = os.path.join(r, file)
#                 zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
#                 zip_ref.extractall(extract_dir)
#                 zip_ref.close()
#             except:
#                 print "Error in ", file
from shutil import copyfile

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
                # os.rmdir(pdf_directory)
                print "Folder Exists"
                # raise
