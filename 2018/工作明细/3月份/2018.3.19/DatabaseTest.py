# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:59:38 2018

@author: 翦林鹏


需要设置几个地址
"""

import pymysql
import xlrd
import datetime
import os
import time

def CreatePSTable(users,passwords,databases):
    cmd = '''CREATE TABLE IF NOT EXISTS `ProductionSale` (
`stock_code` VARCHAR(100),
`stock_name` VARCHAR(100),
`year` VARCHAR(100),
`month` VARCHAR(100),
`production` VARCHAR(100),
`SPLY_production` VARCHAR(100),
`moth_changeP` VARCHAR(100),
`cumulativeP` VARCHAR(100),
`SPLY_cumulativeP` VARCHAR(100),
`cumulativeP_changeP` VARCHAR(100),
`large_production` VARCHAR(100),
`SPLY_production_large` VARCHAR(100),
`month_changeP_large` VARCHAR(100),
`cumulativeP_large` VARCHAR(100),
`SPLY_cumulativeP_large` VARCHAR(100),
`cumulativeP_changeP_large`VARCHAR(100),
`mid_production` VARCHAR(100),
`SPLY_production_mid` VARCHAR(100),
`month_changeP_mid` VARCHAR(100),
`cumulativeP_mid` VARCHAR(100),
`SPLY_cumulativeP_mid` VARCHAR(100),
`cumulativeP_changeP_mid` VARCHAR(100),
`small_production` VARCHAR(100),
`SPLY_production_small` VARCHAR(100),
`month_changeP_small` VARCHAR(100),
`cumulativeP_small` VARCHAR(100),
`SPLY_cumulativeP_small` VARCHAR(100),
`cumulativeP_changeP_small` VARCHAR(100),
`sale` VARCHAR(100),
`SPLY_sale` VARCHAR(100),
`moth_changeS` VARCHAR(100),
`cumulativeS` VARCHAR(100),
`SPLY_cumulativeS` VARCHAR(100),
`cumulativeS_changeS` VARCHAR(100),
`large_sale` VARCHAR(100),
`SPLY_sale_large` VARCHAR(100),
`month_changeS_large` VARCHAR(100),
`cumulativeS_large` VARCHAR(100),
`SPLY_cumulativeS_large` VARCHAR(100),
`cumulativeS_changeS_large`VARCHAR(100),
`mid_sale` VARCHAR(100),
`SPLY_sale_mid` VARCHAR(100),
`month_changeS_mid` VARCHAR(100),
`cumulativeS_mid` VARCHAR(100),
`SPLY_cumulativeS_mid` VARCHAR(100),
`cumulativeS_changeS_mid` VARCHAR(100),
`small_sale` VARCHAR(100),
`SPLY_sale_small` VARCHAR(100),
`month_changeS_small` VARCHAR(100),
`cumulativeS_small`  VARCHAR(100),
`SPLY_cumulativeS_small` VARCHAR(100),
`cumulativeS_changeS_small` VARCHAR(100),
primary key (`stock_code`,`stock_name`,`year`,`month`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    db = pymysql.connect(user=users,password=passwords,database=databases,charset="utf8")
    cursor = db.cursor()
    cursor.execute(cmd)
    db.commit()
    cursor.close()
    db.close()

def InsertPSTable(users,passwords,databases):
    sql = '''INSERT INTO `ProductionSale` (`stock_code`,`stock_name`,`year`,`month`)
             VALUES (600360,'宇通客车',2018,3)'''
    db = pymysql.connect(user=users,password=passwords,database=databases,charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    
    
def QueryPSTable(users,passwords,databases,stock_codes,years,months):
    
    sql = "SELECT * FROM `ProductionSale` WHERE `stock_code`="+stock_codes+" AND `year`="+years+" AND `month`="+months
  
    #sql = '''SELECT * FROM `ProductionSale` 
    #         WHERE `stock_code`=600360 AND `stock_name`='宇通客车' AND `year`=2018 AND `month`=9'''
             
    db = pymysql.connect(user=users,password=passwords,database=databases,charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql)
    rs=cursor.fetchall()
    flag = -1
    if rs:
        flag = 0
    else:
        flag = -1
    #print (rs)
    cursor.close()
    db.close()
    return flag
    
    

    
#CreatePSTable(users="root",passwords="jip6669635",databases="db_test1")
#InsertPSTable(users="root",passwords="jip6669635",databases="db_test1")

#QueryPSTable(users="root",passwords="jip6669635",databases="db_test1")
    
AllField ='''(`stock_code`,`stock_name`,`year`,`month`,`production`,`SPLY_production`,`moth_changeP`,`cumulativeP`,`SPLY_cumulativeP`,`cumulativeP_changeP`,`large_production`,`SPLY_production_large`,\
`month_changeP_large`,`cumulativeP_large`,`SPLY_cumulativeP_large`,`cumulativeP_changeP_large`,`mid_production`,`SPLY_production_mid`,`month_changeP_mid`,`cumulativeP_mid`,\
`SPLY_cumulativeP_mid`,`cumulativeP_changeP_mid`,`small_production`,`SPLY_production_small`,`month_changeP_small`,`cumulativeP_small`,`SPLY_cumulativeP_small`,\
`cumulativeP_changeP_small`,`sale`,`SPLY_sale`,`moth_changeS`,`cumulativeS`,`SPLY_cumulativeS`,`cumulativeS_changeS`,`large_sale`,`SPLY_sale_large`,`month_changeS_large`,\
`cumulativeS_large`,`SPLY_cumulativeS_large`,`cumulativeS_changeS_large`,`mid_sale`,`SPLY_sale_mid`,`month_changeS_mid`,`cumulativeS_mid`,`SPLY_cumulativeS_mid`,`cumulativeS_changeS_mid`,\
`small_sale`,`SPLY_sale_small`,`month_changeS_small`,`cumulativeS_small`,`SPLY_cumulativeS_small`,`cumulativeS_changeS_small`)'''


def ExcelToSql(users,passwords,databases):
    address = r"E:\JianLpeng\Project\Anack\scawling\600066_20180306_2.xlsx"
    data = xlrd.open_workbook(address)
    table =data.sheets()[0]
    nrows =table.nrows
    print (table.row_values(0)[:13])
    DataInsert = ['600360','宇通客车','2018','3']
    for i in range(nrows):
        if (table.row_values(i)[0]=='生产量'):
            break;
    for j in range(i,i+8):
            DataInsert.extend(table.row_values(j)[1:7])
    DataTuple=tuple(list(DataInsert))
    DataStr = str(tuple(DataTuple))
    sql = "INSERT INTO `ProductionSale`"+" "+AllField+" "+"VALUES"+" "+DataStr
    db = pymysql.connect(user=users,password=passwords,database=databases,charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    
   
    
#ExcelToSql(users="root",passwords="jip6669635",databases="db_test1")



'''
上层逻辑：
ProductionSaleUpdate (StockList,year=datetime.datetime.now().year,month= datetime.datetime.now().month):
    for (EveryYear,EveryMonth) in (range(YearBegin,year),....):
        if 如果数据库中有记录：
            break
        else:
            去网站找数据
            入库
        

'''

user = "root"
password = "jip6669635"
database = "db_test1"
stock_code = "600360"
year = "2018"
month ="4"
#TrueOrFalse = QueryPSTable(users=user,passwords=password,databases=database,stock_codes=stock_code,years=year,months=month)
#print (TrueOrFalse)



from selenium import webdriver

#获取最后更新的日期
def DateLastUpdate(driver):
    content = driver.find_element_by_xpath("//div[@id='sse_query_list']/dl/dd/a/span").text
    date = content.split('-')
    year = date[0]
    month = date[1]
    return (year,month)


#下载某年某月的产销快报
DownloadAdr = "d:\\downloadTest"
def DownloadPDF(driver,StockName,stock_code,year,month):
    XpathTitle =StockName+year+"年"+month+"月份产销数据快报"
    title = "//a[@title=\'"+XpathTitle+"\']"
    print (title)
    href=driver.find_element_by_xpath(title).get_attribute('href')
    list=href.split('/')
    print (list)
    PDF_name=list[-1]
#    PDF_list = PDF_name.split('.')
#    FileName = PDF_list[0]
    print (PDF_name)
    driver.get(href)
    driver.implicitly_wait(10)
    driver.find_element_by_id("download").click()
    driver.back()
#    print (FileName)
    return PDF_name

#PDF转excel
ExeAdr = r"E:\JianLpeng\workspace\AutoIt\UpfileWithPara.exe"
def PdfToExcel(fileName,driver):
    driver.find_element_by_xpath("//div[@class = 'settings']/div[2]/a[2]").click()
    driver.find_element_by_id("filePicker").click()
    fileAdr = DownloadAdr+'\\'+fileName
    os.system(ExeAdr+" "+"firefox"+" "+fileAdr)
    time.sleep(4) 
    driverEx.find_element_by_xpath("//div[@class = 'btns']/a").click()
    #以下语句还需要优化
    time.sleep(15)
    driver.find_element_by_xpath("//div[@class = 'btns']/a[3]").click()
    driver.refresh()

##import os
##ExeAdr = r"E:\JianLpeng\workspace\AutoIt\UpfileWithPara.exe"
#fileName = "600066_20180306_2.pdf"
##DownloadAdr = "d:\\downloadTest"
##fileAdr = DownloadAdr+'\\'+fileName
##os.system(ExeAdr+" "+"firefox"+" "+fileAdr)
#profile = webdriver.FirefoxProfile()
#profile.set_preference('browser.download.dir', 'd:\\downloadTest\\')
#profile.set_preference('browser.download.folderList', 2)
#profile.set_preference('browser.download.manager.showWhenStarting', False)
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.ms-excel')
#driverEx = webdriver.Firefox(firefox_profile=profile)
#urlEx = "http://app.xunjiepdf.com/pdf2excel"
#driverEx.get(urlEx)
#PdfToExcel(fileName=fileName,driver=driverEx)
    


DownloadAdr = "d:\\downloadTest"
def ProSaleUpdate(StockName,stock_code):
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
    
    #pdf转EXCEL
    urlEx = "http://app.xunjiepdf.com/pdf2excel"
    driverEx=webdriver.Firefox(firefox_profile=fp)
    driverEx.get(urlEx)
    #driverEx.implicitly_wait(4)
   
    
    url = "http://www.sse.com.cn/home/search/?webswd="+StockName+"产销快报"
    driver.get(url)
    driver.implicitly_wait(50)
    
    (year,month)=DateLastUpdate(driver)
    
    #假设起始日期为2017.1
    DateBegin = (year-2000)*12+month
    DateEnd = (2017-2000)*12+1
    for DateExact in range(DateBegin,DateEnd-1,-1):
        YearExact = (int)(DateExact/12) +2000
        MonthExact= DateExact%12
        TrueOrFalse = QueryPSTable(users=user,passwords=password,databases=database,stock_codes=stock_code,years=YearExact,months=MonthExact)
        #if (TrueOrFalse == -1):
            判断是否翻页
            转换
            入库
        else：
            break
            
            
        
#StockName = "宇通客车"
#stock_code = "600066"
#fp = webdriver.FirefoxProfile()
#fp.set_preference("browser.download.folderList", 2)
#fp.set_preference("browser.download.manager.showWhenStarting", False)
#fp.set_preference("browser.download.dir", DownloadAdr)
#fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
#fp.set_preference("pdfjs.disabled", True)
#fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
#driver = webdriver.Firefox(firefox_profile=fp)
#driver.implicitly_wait(10)
#driver.maximize_window()
#url = "http://www.sse.com.cn/home/search/?webswd="+StockName+"产销快报"
#driver.get(url)
#driver.implicitly_wait(50)
#DownloadPDF(driver=driver,StockName=StockName,stock_code=stock_code,year="2018",month="2")






