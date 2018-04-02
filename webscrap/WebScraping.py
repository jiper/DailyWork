  
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:25:31 2018

@author: JianLPeng
"""



import urllib.request as ur
import urllib


url = r"http://www.sse.com.cn/home/search/?webswd=%E5%AE%87%E9%80%9A%E5%AE%A2%E8%BD%A6%E4%BA%A7%E9%94%80%E5%BF%AB%E6%8A%A5"
#url=urllib.parse.quote(url)
url1 = r"http://www.baidu.com"
html = ur.urlopen(url).read()
print (html)