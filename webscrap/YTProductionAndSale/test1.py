# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:26:10 2018

@author: suxiaolin
"""

import os
import shutil
import datetime

path=r"D:\downloadTest"

#if os.path.isdir(path):
#    print ("yes")
#    shutil.rmtree(path)


#li=os.listdir(path)
#print (li)


#print (os.path.join(path,'2.txt'))

a=datetime.date(2017,12,1)
print (a)
a1=a+ datetime.timedelta(days = -1)
print (a1)