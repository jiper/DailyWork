# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:26:10 2018

@author: suxiaolin
"""

import os
import shutil

path=r"D:\downloadTest"

#if os.path.isdir(path):
#    print ("yes")
#    shutil.rmtree(path)


li=os.listdir(path)
print (li)