# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:50:45 2018

@author: suxiaolin
"""

import os
import sys
import xlrd

def search(path, word,word2):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            if os.path.isfile(fp) and word2 in filename:
                print (fp)
    return (fp)

DownloadAdr = "d:\\downloadTest"
word="600066_20180306_2"

fp = search(DownloadAdr, word,"xls")
print (type(fp))

#xlrd.Book.encoding = "gbk"
fp1 = "d:\\downloadTest\\"+r"600066_20180306_2_3.xlsx"
print (fp1)

#f = open(fp1, 'rb')
#lines = f.readlines()
#for line in lines:
#    line = line.decode('gb2312').encode('utf8') 
#    print (line)

#data = xlrd.open_workbook(r'd:\downloadTest\test.xlsx')

#xlrd.open_workbook(r'd:\downloadTest\600066_20180306_2_6.xls')
data = xlrd.open_workbook(fp1)
    
    
#import pandas as pd
#
#df=pd.read_excel(fp1,sheetname=0)
#print (df.head())


