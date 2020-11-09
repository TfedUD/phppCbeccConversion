# -*- coding: utf-8 -*-



import pandas as pd 
import xlrd as xl
import xlwings as xw
import os
import sys 

def getDataFromPHPP():
    #
    excel_app = xw.App(visible=False)
    book = xw.Book('d:\\UDtools\\CBECCPHPPDEV\\theBrainWIP\\Debrain\\phpp.xlsx')
    sht1 = book.sheets('U-Values')
    df = sht1.range('L17:M20').value 
        
    print(df)
        
        #print(df)
    
    
    newPath = 'd:\\UDtools\\CBECCPHPPDEV\\theBrainWIP\\putputTests'
    doIt = open("d:\\UDtools\\CBECCPHPPDEV\\theBrainWIP\\putputTests\\test.txt", "w")
    doIt.write(str(df))
    doIt.close()

getDataFromPHPP()