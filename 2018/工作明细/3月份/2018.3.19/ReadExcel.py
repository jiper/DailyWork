# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:59:39 2018

@author: 54206
"""
import xlrd
address = r"E:\JianLpeng\Project\Anack\scawling\600066_20180306_2.xlsx"
data = xlrd.open_workbook(address)
table =data.sheets()[0]
nrows =table.nrows
print (table.row_values(0)[:13])
DataInsert = ['600360','宇通客车','2018','3']
for i in range(nrows):
    if (table.row_values(i)[0]=='生产量'):
        break;
for j in range(i,i+8):
        DataInsert.extend(table.row_values(j)[1:7])
DataTuple=tuple(list(DataInsert))
DataStr = str(tuple(DataTuple))


print ("nihao"+"ma")