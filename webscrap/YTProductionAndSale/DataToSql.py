# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:22:21 2018

@author: JianLpeng
"""
import pymysql
import PdfDown
import PDF_TXT


class ProductionSaleToSql:
    def __init__(self,user,password,database,stock_code,StockName,YearBegin = 2017,MonthBegin = 6,DownloadAdr="d:\\downloadTest"):
        self.user = user                      #用户名 
        self.password = password              #密码
        self.database = database              #数据库
        self.stock_code = stock_code          #股票代码
        self.StockName = StockName            #股票名称
        self.DownloadAdr = DownloadAdr        #下载路径
        self.YearBegin = YearBegin            #起始日期
        self.MonthBegin = MonthBegin          #结束日期
        # 所有的字段列表   
        self.AllField ='''(`stock_code`,`stock_name`,`year`,`month`,`production`,`SPLY_production`,`moth_changeP`,`cumulativeP`,`SPLY_cumulativeP`,`cumulativeP_changeP`,`large_production`,`SPLY_production_large`,\
        `month_changeP_large`,`cumulativeP_large`,`SPLY_cumulativeP_large`,`cumulativeP_changeP_large`,`mid_production`,`SPLY_production_mid`,`month_changeP_mid`,`cumulativeP_mid`,\
        `SPLY_cumulativeP_mid`,`cumulativeP_changeP_mid`,`small_production`,`SPLY_production_small`,`month_changeP_small`,`cumulativeP_small`,`SPLY_cumulativeP_small`,\
        `cumulativeP_changeP_small`,`sale`,`SPLY_sale`,`moth_changeS`,`cumulativeS`,`SPLY_cumulativeS`,`cumulativeS_changeS`,`large_sale`,`SPLY_sale_large`,`month_changeS_large`,\
        `cumulativeS_large`,`SPLY_cumulativeS_large`,`cumulativeS_changeS_large`,`mid_sale`,`SPLY_sale_mid`,`month_changeS_mid`,`cumulativeS_mid`,`SPLY_cumulativeS_mid`,`cumulativeS_changeS_mid`,\
        `small_sale`,`SPLY_sale_small`,`month_changeS_small`,`cumulativeS_small`,`SPLY_cumulativeS_small`,`cumulativeS_changeS_small`)'''

      
    #建表
     #命名规则 P：生产量 S：销售量  SPLY：去年同期
    def CreatePSTable(self):
        cmd = '''CREATE TABLE IF NOT EXISTS `ProductionSale` (
    `stock_code` VARCHAR(100),                           #股票代码
    `stock_name` VARCHAR(100),                           #股票名称
    `year` VARCHAR(100),                                 #年
    `month` VARCHAR(100),                                #月
    `production` VARCHAR(100),                           #当月生产量
    `SPLY_production` VARCHAR(100),                      #去年同期（生产量）
    `moth_changeP` VARCHAR(100),                         #当月数量同比变动（生产量）
    `cumulativeP` VARCHAR(100),                          #本年累计（生产量）
    `SPLY_cumulativeP` VARCHAR(100),                     #去年同期累计（生产量）
    `cumulativeP_changeP` VARCHAR(100),                  #累计数量同比变动（生产量）
    `large_production` VARCHAR(100),                     #当月生产量（大型生产量）
    `SPLY_production_large` VARCHAR(100),                #去年同期（大型生产量）
    `month_changeP_large` VARCHAR(100),                  #单月数量同比变动（大型生产量）
    `cumulativeP_large` VARCHAR(100),                    #本年累计（大型生产量）
    `SPLY_cumulativeP_large` VARCHAR(100),               #去年同期累计（大型生产量）
    `cumulativeP_changeP_large`VARCHAR(100),             #累计数量同比变动（大型生产量）
    `mid_production` VARCHAR(100),                       #当月生产量（中型生产量）
    `SPLY_production_mid` VARCHAR(100),                  #去年同期（中型生产量）
    `month_changeP_mid` VARCHAR(100),                    #当月数量同比变动（中型生产量）
    `cumulativeP_mid` VARCHAR(100),                      #本年累计（中型生产量）
    `SPLY_cumulativeP_mid` VARCHAR(100),                 #去年同期累计（中型生产量）
    `cumulativeP_changeP_mid` VARCHAR(100),              #累计数量同比变动（中型生产量）
    `small_production` VARCHAR(100),                     #当月生产量（轻型生产量）
    `SPLY_production_small` VARCHAR(100),                #去年同期（轻型生产量）
    `month_changeP_small` VARCHAR(100),                  #当月数量同比变动（轻型生产量）
    `cumulativeP_small` VARCHAR(100),                    #本年累计（轻型生产量）
    `SPLY_cumulativeP_small` VARCHAR(100),               #去年同期累计（轻型生产量）
    `cumulativeP_changeP_small` VARCHAR(100),            #累计数量同比变动（轻型生产量）
    `sale` VARCHAR(100),                                 #当月销售量
    `SPLY_sale` VARCHAR(100),                            #去年同期（当月销售量）
    `moth_changeS` VARCHAR(100),                         #单月数量同比变动（当月销售量）
    `cumulativeS` VARCHAR(100),                          #本年累计（销售量）
    `SPLY_cumulativeS` VARCHAR(100),                     #去年同期累计（销售量）
    `cumulativeS_changeS` VARCHAR(100),                  #累计数量同比变动（销售量）
    `large_sale` VARCHAR(100),                           #当月销售量（大型销售量）
    `SPLY_sale_large` VARCHAR(100),                      #去年同期（大型销售量）
    `month_changeS_large` VARCHAR(100),                  #单月数量同比变动（大型销售量）
    `cumulativeS_large` VARCHAR(100),                    #本年累计（大型销售量）
    `SPLY_cumulativeS_large` VARCHAR(100),               #去年同期累计（大型销售量）
    `cumulativeS_changeS_large`VARCHAR(100),             #累计数量同比变动（大型销售量）
    `mid_sale` VARCHAR(100),                             #当月销售量（中型销售量）
    `SPLY_sale_mid` VARCHAR(100),                        #去年同期（大型销售量）
    `month_changeS_mid` VARCHAR(100),                    #当月数量同比变动（大型销售量）
    `cumulativeS_mid` VARCHAR(100),                      #本年累计（大型销售量）
    `SPLY_cumulativeS_mid` VARCHAR(100),                 #去年同期累计（大型销售量）
    `cumulativeS_changeS_mid` VARCHAR(100),              #累计数量同比变动（大型销售量）
    `small_sale` VARCHAR(100),                           #小型当月销售量（小型销售量）
    `SPLY_sale_small` VARCHAR(100),                      #去年同期（小型销售量）
    `month_changeS_small` VARCHAR(100),                  #单月数量同比变动（小型销售量）
    `cumulativeS_small`  VARCHAR(100),                   #本年累计（小型销售量）
    `SPLY_cumulativeS_small` VARCHAR(100),               #去年同期累计（小型销售量）
    `cumulativeS_changeS_small` VARCHAR(100),            #累计数量同比变动（小型销售量）
    primary key (`stock_code`,`year`,`month`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
        db = pymysql.connect(user=self.user,password=self.password,database=self.database,charset="utf8")
        cursor = db.cursor()
        cursor.execute(cmd)
        db.commit()
        cursor.close()
        db.close()
    
    #数据库插入
    def InsertPSTable(self):
        sql = '''INSERT INTO `ProductionSale` (`stock_code`,`stock_name`,`year`,`month`)
                 VALUES (600360,'宇通客车',2018,3)'''
        db = pymysql.connect(user=self.user,password=self.password,database=self.database,charset="utf8")
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        
    #数据库查询，返回查询结果  
    def QueryPSTable(self,years,months):
        
        sql = "SELECT * FROM `ProductionSale` WHERE `stock_code`="+self.stock_code+" AND `year`="+years+" AND `month`="+months
                 
        db = pymysql.connect(user=self.user,password=self.password,database=self.database,charset="utf8")
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
    
 
    def TxtToSql(self,txtAdd):    
        f= open(txtAdd,'r')
        TargetLine=49
        endLine=143
        lnum=1
        data=[self.stock_code,self.StockName]
        for line in f:
            if (lnum==TargetLine and TargetLine<=endLine):
                TargetLine=TargetLine+2
                line=line.replace(',','')
                #line=line.strip(',')
                line=line[:-2]
                data.append(line)
            elif (lnum == 16):
                data.append(line.split(' ')[0])
            elif (lnum == 17):
                data.append(line.split(' ')[0])
            lnum=lnum+1
        print (data)
        DataTuple=tuple(list(data))
        DataStr = str(tuple(DataTuple))
        sql = "INSERT INTO `ProductionSale`"+" "+self.AllField+" "+"VALUES"+" "+DataStr
        db = pymysql.connect(user=self.user,password=self.password,database=self.database,charset="utf8")
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
                
    def ProSaleUpdate(self):
        self.CreatePSTable()
        downLoad = PdfDown.PdfDownLoad(self.YearBegin,self.MonthBegin)
        downLoad.GetAllPdfFile()
        print (downLoad.pdfList)
        TxtTrans = PDF_TXT.PDFToTXT(PDFList=downLoad.pdfList)
        TxtTrans.TransAll()
        for Txt in TxtTrans.TxtList:
            txtAdd=self.DownloadAdr+'/'+Txt
            self.TxtToSql(txtAdd)
            print (Txt+'入库成功')
            
     
if __name__ == "__main__":
    user = "root"
    password = "jip6669635"
    database = "db_test1"
    stock_code = "600066"
    StockName = "宇通客车"
    DownloadAdr = "d:\\downloadTest"
    Update = ProductionSaleToSql(user=user,password=password,database=database,stock_code=stock_code,StockName=StockName,DownloadAdr=DownloadAdr,YearBegin = 2017,MonthBegin = 6)
   # Update.ParametersSet(user=user,password=password,database=database,stock_code=stock_code,StockName=StockName,DownloadAdr=DownloadAdr,ExeAdr=ExeAdr,YearBegin = 2017,MonthBegin = 6)
    Update.ProSaleUpdate()
    
"""
self.user = user                      #用户名 
self.password = password              #密码
self.database = database              #数据库
self.stock_code = stock_code          #股票代码
self.StockName = StockName            #股票名称
self.DownloadAdr = DownloadAdr        #下载路径
self.ExeAdr = ExeAdr                  #可执行文件路径
self.YearBegin = YearBegin            #起始日期
self.MonthBegin = MonthBegin          #结束日期
"""
