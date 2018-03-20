# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:21:13 2018

@author: suxiaolin
"""

#仅仅是做测试，可以删除
from selenium import webdriver


driver1 = webdriver.Firefox()
driver2=webdriver.Firefox()

driver1.get("https://www.baidu.com")
driver2.get("https://www.sina.com")
driver1.quit()