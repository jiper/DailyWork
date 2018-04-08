# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:10:12 2018

@author: suxiaolin
"""
txtAdd = r'E:\JianLPeng\DailyWork\webscrap\pdf\out.txt'
f= open(txtAdd,'r')
TargetLine=49
endLine=143
lnum=1
data=[]
for line in f:
    if (lnum==TargetLine and TargetLine<=endLine):
        TargetLine=TargetLine+2
        line=line.replace(',','')
        #line=line.strip(',')
        line=line[:-2]
        data.append(line)
    elif (lnum == 16):
        data.append(line.split(' ')[0])
    elif (lnum == 17):
        data.append(line.split(' ')[0])
    lnum=lnum+1
print (data)
    
    
