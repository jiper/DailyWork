# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:11:38 2018

@author: Administrator
"""
import requests

url = r'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2018-03-06/600066_20180306_2.pdf'
target_file_name = '600066.pdf'

r = requests.get(url) # create HTTP response object
print(r.content)
with open(target_file_name,'wb') as f:
    f.write(r.content)
    