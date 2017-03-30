## Version: Python 3.6
##
## Date: 03/30/17
##
## Author: Ada Chavez http://adachavez.com
##
## Purpose: UI that allows the user to choose a source folder and a destination folder 
## to copy over newly modified and created text files.

from tkinter import *
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
import os
import time
import shutil
from glob import glob

class FileCopier:
    # Widgets
    def __init__(self, master):

        # Styling
        master.title("File Copier")
        master.configure(background = "#7da6e8")
        master.resizable(False, False)


        self.style = ttk.Style()
        self.style.configure("TFrame", background = "#7da6e8")
        self.style.configure("TButton", background = "#7da6e8", font = ('Helvetica', 10))
        self.style.configure("TLabel", background = "#7da6e8", font = ('Helvetica', 11))
        self.style.configure("Header.TLabel", font = ('Helvetica', 18, 'bold'))

        
        # Variables
        self.sourceFolderName = StringVar()
        self.source = (self.sourceFolderName.get())
        self.destFolderName = StringVar()
        self.destination = (self.destFolderName.get())

        # Header Frame
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # Header and Label
        ttk.Label(self.frame_header, text = "File Copier", style = 'Header.TLabel').grid(row = 0, column = 0, padx = 5)
        ttk.Label(self.frame_header, wraplength = 300, anchor = CENTER,
                  text = ("This program will copy newly modified text files"
                                             " to desired folder")).grid(row = 1, column = 0, pady = 5)
        
        # Content Frame
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        # Contents: Labels and Buttons
        ttk.Label(self.frame_content, text = "Step 1: ").grid(row = 1, column = 0, padx = 5 ,sticky = 'w')
        ttk.Label(self.frame_content, text = "Step 2: ").grid(row = 4, column = 0, padx = 5, sticky = 'w')
        

        ttk.Button(self.frame_content, text = "Source Folder", command = self.selectSourceFolder).grid(row = 2, column = 0, padx = 5, sticky = 'w')
        ttk.Button(self.frame_content, text = "Destination Folder", command = self.destinationFolder).grid(row = 5, column = 0, padx = 5, sticky = 'w')

        ttk.Label(self.frame_content, text = self.sourceFolderName, textvariable = self.sourceFolderName ).grid(row = 3, column = 0)
        ttk.Label(self.frame_content, text = self.destFolderName, textvariable = self.destFolderName ).grid(row = 6, column = 0)
        

        ttk.Button(self.frame_content, text = "Initiate File Check", command = lambda: self.fileCheck(self.sourceFileCheck,self.destFileCheck)).grid(row = 7, column = 0, columnspan = 2, pady = 5)

        
    # Button Functions
    def selectSourceFolder(self): # Selects Source Folder
        self.sourceFileCheck = filedialog.askdirectory(initialdir = "C:/", title = "Select source folder")
        self.sourceFolderName.set(self.sourceFileCheck)
        
    def destinationFolder(self): # Selects Destination Folder
        self.destFileCheck = filedialog.askdirectory(initialdir = "C:/", title = "Select destination folder")
        self.destFolderName.set(self.destFileCheck)

    def fileCheck(self, sourceFileCheck, destFileCheck ): # Copies newly modified files from source folder to destination folder
        currentTime = datetime.now()
        time24HrsAgo = currentTime - timedelta(hours=24)

        
        for fileList in os.listdir(sourceFileCheck):
            # files path and the modified datetime will be shown
            files = os.path.realpath(os.path.join(sourceFileCheck,fileList))
            
            if files.endswith('.txt'):
                # shows modified time for each file
                sourceFileModifiedTime = datetime.fromtimestamp(os.path.getmtime(files))
                # compares the modified time for each file to the time 24 hours ago
                if sourceFileModifiedTime > time24HrsAgo:
                    print (files, "copied file to: ", destFileCheck)
                    shutil.copy(files,destFileCheck)
                    messagebox.showinfo(title="Message", message = "The " + files + " have been copied to: " + destFileCheck)
                    
                else:
                    print (files, "was not copied")



    

            
def main(): 
    
    root = Tk()
    root.minsize(400, 280)
    root.maxsize(400, 280)
    filecopier = FileCopier(root)
    root.mainloop()
    
if __name__ == "__main__": main()
