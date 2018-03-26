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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FolderNotCleanException (Exception):
    pass

class UnfoundExcelFileException (Exception):
    pass



#清空文件夹
def FolderClean(path):
    for i in os.listdir(path):
       path_file = os.path.join(path,i)  # 取文件路径
       if os.path.isfile(path_file):
           os.remove(path_file)
    #文件夹必须清理干净，否则会影响后面的流程
    if os.listdir(path):   #如果文件夹没有清理干净，抛出异常
        raise FolderNotCleanException
    
def FindExcelFile(path):
    ExcelPath = ""
    for i in os.listdir(path):
       path_file = os.path.join(path,i)  # 取文件路径
       if (path_file.find('.xlsx')!=-1 or path_file.find('.xls')!=-1):  #查找后缀为.xlsx或.xls的文件
           ExcelPath = path_file
    if ExcelPath:
        return ExcelPath
    else:
        raise UnfoundExcelFileException
    

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
             
    db = pymysql.connect(user=users,password=passwords,database=databases,charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql)
    rs=cursor.fetchall()
    flag = -1
    if rs:
        flag = 0
    else:
        flag = -1
    cursor.close()
    db.close()
    return flag
    
    
# 所有的字段列表   
AllField ='''(`stock_code`,`stock_name`,`year`,`month`,`production`,`SPLY_production`,`moth_changeP`,`cumulativeP`,`SPLY_cumulativeP`,`cumulativeP_changeP`,`large_production`,`SPLY_production_large`,\
`month_changeP_large`,`cumulativeP_large`,`SPLY_cumulativeP_large`,`cumulativeP_changeP_large`,`mid_production`,`SPLY_production_mid`,`month_changeP_mid`,`cumulativeP_mid`,\
`SPLY_cumulativeP_mid`,`cumulativeP_changeP_mid`,`small_production`,`SPLY_production_small`,`month_changeP_small`,`cumulativeP_small`,`SPLY_cumulativeP_small`,\
`cumulativeP_changeP_small`,`sale`,`SPLY_sale`,`moth_changeS`,`cumulativeS`,`SPLY_cumulativeS`,`cumulativeS_changeS`,`large_sale`,`SPLY_sale_large`,`month_changeS_large`,\
`cumulativeS_large`,`SPLY_cumulativeS_large`,`cumulativeS_changeS_large`,`mid_sale`,`SPLY_sale_mid`,`month_changeS_mid`,`cumulativeS_mid`,`SPLY_cumulativeS_mid`,`cumulativeS_changeS_mid`,\
`small_sale`,`SPLY_sale_small`,`month_changeS_small`,`cumulativeS_small`,`SPLY_cumulativeS_small`,`cumulativeS_changeS_small`)'''


def ExcelToSql(users,passwords,databases,address,StockName,StockCode,Year,Month):
    data = xlrd.open_workbook(address)
    table =data.sheets()[0]
    nrows =table.nrows
    DataInsert = [StockCode,StockName,Year,Month]
    for i in range(nrows):
        if (table.row_values(i)[0]=='生产量'):
            #测试发现，“生产量”这一列后可能有一行空列
            if table.row_values(i)[1]:
                ColumnAdd=0
            else:
                ColumnAdd = 1 #如果存在空行，则列数加1
            break;
    for j in range(i,i+8):
            DataInsert.extend(table.row_values(j)[1+ColumnAdd:7+ColumnAdd])
    DataTuple=tuple(list(DataInsert))
    DataStr = str(tuple(DataTuple))
    sql = "INSERT INTO `ProductionSale`"+" "+AllField+" "+"VALUES"+" "+DataStr
    db = pymysql.connect(user=users,password=passwords,database=databases,charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    
   
user = "root"
password = "jip6669635"
database = "db_test1"
stock_code = "600066"



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
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", DownloadAdr)
    fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
    fp.set_preference("pdfjs.disabled", True)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    driverPDF = webdriver.Firefox(firefox_profile=fp)
    
    
    XpathTitle =StockName+year+"年"+month+"月份产销数据快报"
    title = "//a[@title=\'"+XpathTitle+"\']"
    href=driver.find_element_by_xpath(title).get_attribute('href')
    list=href.split('/')
    PDF_name=list[-1]
    
    driverPDF.get(href)
    driverPDF.implicitly_wait(10)
    driverPDF.find_element_by_id("download").click()
    driverPDF.quit()
    #driver.back()
    return PDF_name

#PDF转excel
#ExeAdr = r"E:\JianLpeng\workspace\AutoIt\UpfileWithPara.exe"
ExeAdr=r"E:\JianLpeng\DailyWork\WorkSpace\PythonSpace\YTProductionSaleSql\UpfileWithPara.exe"
def PdfToExcel(fileName,driver):
    #driver.find_element_by_xpath("//div[@class = 'settings']/div[2]/a[2]").click()  #此语句可以
    driver.find_element_by_id("filePicker").click()
    fileAdr = DownloadAdr+'\\'+fileName
    os.system(ExeAdr+" "+"firefox"+" "+fileAdr)
    time.sleep(4) 
    driver.find_element_by_xpath("//div[@class = 'btns']/a").click()
    #设置显示等待，等待时间不超过50s，每隔0.5检查一次
    locator = (By.CLASS_NAME, 'downloadBtn')
    WebDriverWait(driver, 50, 0.5).until(EC.presence_of_element_located(locator))
    
    time.sleep(15)
    driver.find_element_by_xpath("//div[@class = 'btns']/a[3]").click()
    driver.refresh()


  

DownloadAdr = "d:\\downloadTest"
def ProSaleUpdate(StockName,stock_code,YearBegin = 2015,MonthBegin = 11):
    
    #配置产销快报页面参数，实现pdf自动下载  
    try:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", DownloadAdr)
        fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
        fp.set_preference("pdfjs.disabled", True)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        driver = webdriver.Firefox(firefox_profile=fp)
        #driver.maximize_window()
        #打开页面
        url = "http://www.sse.com.cn/home/search/?webswd="+StockName+"产销快报"
        driver.get(url)
    
        
        #配置pdf转excel页面参数，实现excel文件自动下载
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', DownloadAdr)
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        #profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.ms-excel')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ')
        driverEx = webdriver.Firefox(firefox_profile=profile)
        #打开页面
        urlEx = "http://app.xunjiepdf.com/pdf2excel"
        driverEx.get(urlEx)
        #driverEx.implicitly_wait(4)
    
        #设置隐式等待，括号中的参数为最大等待时间，如果在最大等待时间内，页面加载完成，则等待立结束，否则抛出异常
        #整个driver的时间内，该设置只用设置一次
        driver.implicitly_wait(100)
        driverEx.implicitly_wait(50)
        
        #从产销快报页面获取最新一次更新的日期，月份-1作为获取数据的起始年、月参数
        (year,month)=DateLastUpdate(driver)
        if (month=="1"):
            YearInt = int(year)-1
            MonthInt= 12
        else:
            YearInt = int(year)
            MonthInt= int(month) -1       
    
        #清空下载文件夹，避免历史文件的干扰
        FolderClean(DownloadAdr)
        DateBegin =datetime.date(YearInt,MonthInt,1)
        DateEnd = datetime.date(YearBegin,MonthBegin,1)
        #count用于计数，因为一个页面只有10条数据，所以每隔10条需要翻页
        count = 0
        for i in range(0,(DateBegin-DateEnd).days+1,1):
            day = DateBegin -datetime.timedelta(days=i)
            if (day.day == 1):
                count = count+1
                YearExact = day.year
                MonthExact = day.month
                try:
                    if(count==11):
                        driver.find_element_by_id('Next').click()
                        count=0
                    TrueOrFalse = QueryPSTable(users=user,passwords=password,databases=database,stock_codes=stock_code,years=str(YearExact),months=str(MonthExact))
                    if (TrueOrFalse == -1):
                        PDF_Name = DownloadPDF(driver =driver ,StockName=StockName,stock_code=stock_code,year=str(YearExact),month=str(MonthExact))
                        PdfToExcel(fileName=PDF_Name,driver = driverEx)
                        ExcelAdr = FindExcelFile(DownloadAdr)
                        ExcelToSql(users=user,passwords=password,databases=database,address=ExcelAdr,StockName=StockName,StockCode=stock_code,Year=str(YearExact),Month=str(MonthExact))         
                        print (StockName+str(YearExact)+"年"+str(MonthExact)+"月入库成功")
                    else:
                        print (StockName+str(YearExact)+"年"+str(MonthExact)+"月数据库中已有记录")
                    FolderClean(DownloadAdr)
                except (Exception) as e:
                    print (StockName+str(YearExact)+"年"+str(MonthExact)+"月入库失败，请检查")
                    print ("检查失败原因："+str(e))
            else:
                pass
    finally:
        FolderClean(DownloadAdr)
        driver.quit()
        driverEx.quit()
            
                       
ProSaleUpdate("宇通客车","600066")        







