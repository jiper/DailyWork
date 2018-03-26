# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:12:38 2018

@author: 54206
"""

import requests

url = r'http://www.baidu.com'


r = requests.get(url) # create HTTP response object
print(r.content)

print ("********************************************************************************************")
r1 = requests.post(url) # create HTTP response object
print(r1.content)
