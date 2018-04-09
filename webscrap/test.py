  
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:25:31 2018

@author: JianLPeng
"""


import subprocess
filename=r'D:\downloadTest\600066_20171202_2'
filename1=r'D:\downloadTest\600066_20171202_2.html'
subprocess.call("C:/Users/suxiaolin/Desktop/2/pdf2htmlEX.exe pdf/"+filename+".pdf  --dest-dir  pdf/"+filename1, shell=True)