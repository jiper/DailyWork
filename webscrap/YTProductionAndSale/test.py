# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:01:58 2018

@author: suxiaolin
"""
import urllib
from bs4 import BeautifulSoup
import os
import re
url=r'D:\downloadTest\HTML/3.html'
htmlfile = open(url, 'r',encoding='utf-8')
htmlpage = htmlfile.read()
soup = BeautifulSoup(htmlpage, "html.parser") 

lls=soup.get_text() 

#print(lls)
#print (len(lls))
ss=soup.find_all(text=re.compile("[0-9.%]*"))
print (lls)


