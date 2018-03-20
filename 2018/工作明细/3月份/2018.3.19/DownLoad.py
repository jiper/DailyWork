# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:05:39 2018

@author: suxiaolin
"""

#coding=utf-8
from selenium import webdriver
import time
import os
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "d:\\downloadTest")
fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
fp.set_preference("pdfjs.disabled", True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
driver = webdriver.Firefox(firefox_profile=fp)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.sse.com.cn/home/search/?webswd=宇通客车产销快报")
driver.implicitly_wait(50)

driver.find_element_by_id('Next').click()

href=driver.find_element_by_xpath("//a[@title='宇通客车2018年2月份产销数据快报']").get_attribute('href')
content = driver.find_element_by_xpath("//div[@id='sse_query_list']/dl/dd/a/span").text
print (content)
list=href.split('/')
print (list)
PDF_name=list[-1]
print (PDF_name)
#driver.quit()
driver.get(href)

#driver.find_element_by_xpath("//a[@title='宇通客车2018年2月份产销数据快报']/h2").click()
driver.implicitly_wait(10)
driver.find_element_by_id("download").click()
driver.quit()




DownloadAdr = "d:\\downloadTest"

def DateLastUpdate():
    
def PdfDownload():

    
    
def DownloadPDF(StockName):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", DownloadAdr)
    fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
    fp.set_preference("pdfjs.disabled", True)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.implicitly_wait(10)
    driver.maximize_window()
    url = "http://www.sse.com.cn/home/search/?webswd="+StockName+"产销快报"
    driver.get(url)
    
    driver.implicitly_wait(50)
    
    content = driver.find_element_by_xpath("//div[@id='sse_query_list']/dl/dd/a/span").text
    date = content.split('-')
    year = date[0]
    month = date[1]
   
    
    
    
    
    
    
    
    