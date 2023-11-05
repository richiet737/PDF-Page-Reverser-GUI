#FileManager is a class in the Application to manage the pdf file manipulation
#make sure this file is not executable to avoid trying to run it

import os
import tkinter as tk
from PyPDF2 import PdfReader, PdfWriter

class FileManager():
    def __init__(self):
        #fileName is the picked file without path information
        self.fileName = tk.StringVar()
        self.fileName = "Empty"
        
        #pathName is the full picked path including file name
        self.pathName = tk.StringVar()
        self.pathName = "Empty"

    def get_info(self):
        with open(self.pathName, 'rb') as f:
            pdf = PdfReader(f)
            number_of_pages = len(pdf.pages)
            print("processing", self.pathName, number_of_pages, "pages")
        
            if number_of_pages == 1:
                sys.exit('only one page found')
            
            # build output PDF filename
            writer = PdfWriter()
            bpath, ext = os.path.splitext(self.pathName)

            #save the new file to the same location as the original with _reversed
            pdfrev = os.path.abspath(bpath + '_reversed' + ext)
            print("bpath = ",bpath)
            print("pdfrev = ",pdfrev)
        
            # n is sequential page increase, r is the reversed page number
            for n in (reversed(range(0, number_of_pages))):
                writer.add_page(pdf.pages[n])
       
            pdf_out = open(pdfrev, 'wb')
            writer.write(pdf_out)
            pdf_out.close()
