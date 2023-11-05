#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
# coding: utf-8

# Created by Richard Bradshaw 28 Oct 2023
#This file must be executable chmod +x pdrfReverse_app.py

# importing libraries
from PyPDF2 import PdfReader, PdfWriter
import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd

from modules import pdfFileManager

class Application(tk.Frame):
    
    #### initialise the Application class ####
    def __init__(self, root):
        
        #attributes defined in __init are instance attributes and must use the self prefix
        #define the window size
        root.geometry("400x200")
        root.title("PDF file page reverser")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
 
        #rb fileManager
        self.fileMan = pdfFileManager.FileManager()

        rootFrame = tk.Frame(master=root, bg="lightgray")
        rootFrame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        # set the number of rows and columns
        # minimum size, in screen units (px)
        rootFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, minsize=20)  # here minsize is optional
   
        tk.Frame.__init__(self, root)

        #add a label at 0x1
        l = tk.Label(rootFrame, fg= "green", bg="lightgray", padx=2, pady=2, text="type path or choose file")
        l.grid(row=0,column=2, sticky=tk.W)

        # add a label at 1x1
        fileLabel = tk.Label(rootFrame, text="File to reverse :", fg="green", bg="lightgray", width = 13, padx=2, pady=2, font=(None, 14))
        fileLabel.grid(row=1, column=1)

        #add text entry box at 1x2
        self.fileEntry = tk.Entry(rootFrame, state="normal", textvariable=self.fileMan.fileName)
        self.fileEntry.grid(row=1, column=2, sticky=tk.W)

        #choose file button at 2x1
        # Button with black border
        border = LabelFrame(rootFrame, bd = 6, bg = "black")
        fb = tk.Button(rootFrame, text="Choose File", width = 10, fg= "green", padx=2, pady=2, command=self.fileCallback)
        fb.grid(row=2,column=2, sticky=tk.W)

        #process button at 3x1
        mb = tk.Button(rootFrame, text="Process File", width = 10, fg="green", padx=2, pady=2, command=self.msgCallback) #.pack(pady=10)
        mb.grid(row=3,column=2, sticky=tk.W)
        
    #### message dialogue displayed at process file button press ####
    def msgCallback(self):
        msg = self.msg=messagebox.askquestion("Question dialogue", self.fileMan.fileName)
        
        #msg yes for yes button pressed
        print("msg dialog", msg)
        
        #reverse the file page order
        if(msg == "yes"):
            print("right we are going to do it")
            if(self.fileMan.pathName == 'Empty'):
                self.fileMan.pathName = self.fileEntry.get()
                print("pathName = ",self.fileMan.pathName)
                print("fileName = ",self.fileMan.fileName)

            self.fileMan.get_info()
        else:
            print("cancel the request")

    #### file picker dialogue ####
    def fileCallback(self):
        fullPath= fd.askopenfilename()
        #return the full path of the picked file
        #print(fullPath)
        self.fileMan.pathName = fullPath                       #get the full path
        self.fileMan.fileName = os.path.basename(fullPath)     #get the file name
        self.fileEntry.delete(0, 'end')                          #clear the text field
        self.fileEntry.insert(0,self.fileMan.fileName)         #put the file name in the entry text box
    
    #### Utility method to resize a button image ####
    def Resize_Image(image, maxsize):
        r1 = image.size[0]/maxsize[0] # width ratio
        r2 = image.size[1]/maxsize[1] # height ratio
        ratio = max(r1, r2)
        newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio))
        image = image.resize(newsize, Image.ANTIALIAS)
        return image

#### main ####
if __name__=='__main__':

    #create a window
    rootWindow = tk.Tk()
    
    #instantiate the window and frame this will be our interface in the forever loop
    application = Application(rootWindow)
    
    #loop forever
    rootWindow.mainloop()
