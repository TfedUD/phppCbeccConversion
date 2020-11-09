# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:22:51 2020

@author: TREVOR
"""
import tkinter as tk
from tkinter import filedialog as fd
import os




class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
            
    def create_widgets(self):
        
        self.id_paspp = tk.Button(self)
        self.id_paspp["text"] = "Give Groot your PHPP"
        self.id_paspp["command"] = self.get_paspp
        self.id_paspp.pack(side="top")
            
        self.out_cbecc = tk.Button(self)
        self.out_cbecc["text"] = "tell Groot where to place CBECC file"
        self.out_cbecc["command"] = self.new_cbecc
        self.out_cbecc.pack(side="bottom")
    
    def get_paspp(self):
        sourcePath = fd.askdirectory()
        source = sourcePath
        file = os.listdir(source)
        
    def new_cbecc(self):
        outputPath = fd.askdirectory()
        output = outputPath
        
    ## Def do the things, next up
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()