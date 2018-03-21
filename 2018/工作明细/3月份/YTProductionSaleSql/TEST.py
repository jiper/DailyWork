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


fp1 = "d:\\downloadTest\\"+r"600066_20180306_2_42847.xls"
print (fp1)

#data = xlrd.open_workbook(r'd:\downloadTest\test.xlsx')
data = xlrd.open_workbook(r'd:\downloadTest\600066_20180306_2_42847.xlsx',encoding_override='utf-8')