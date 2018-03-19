# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:59:38 2018

@author: suxiaolin
"""

import pymysql


def CreatePSTable(users,passwords,databases):
    cmd = '''CREATE TABLE IF NOT EXISTS `ProductionSale` (
`stock_code` INT(6),
`stock_name` VARCHAR(100),
`year` INT(4),
`month` INT(2),
`production` INT(10),
`SPLY_production` INT(10),
`moth_changeP` FLOAT(10,2),
`cumulativeP` INT(10),
`SPLY_cumulativeP` INT(10),
`cumulativeP_changeP` FLOAT(10,2),
`large_production` INT(10),
`SPLY_production_large` INT(10),
`month_changeP_large` INT(10),
`cumulativeP_large` FLOAT(10,2),
`SPLY_cumulativeP_large` INT(10),
`cumulativeP_changeP_large`FLOAT(10,2),
`mid_production` INT(10),
`SPLY_production_mid` INT(10),
`month_changeP_mid` INT(10),
`cumulativeP_mid` FLOAT(10,2),
`SPLY_cumulativeP_mid` INT(10),
`cumulativeP_changeP_mid` FLOAT(10,2),
`small_production` INT(10),
`SPLY_production_small` INT(10),
`month_changeP_small` INT(10),
`cumulativeP_small` FLOAT(10,2),
`SPLY_cumulativeP_small` INT(10),
`cumulativeP_changeP_small` FLOAT(10,2),
`sale` INT(10),
`SPLY_sale` INT(10),
`moth_changeS` FLOAT(10,2),
`cumulativeS` INT(10),
`SPLY_cumulativeS` INT(10),
`cumulativeS_changeS` FLOAT(10,2),
`large_sale` INT(10),
`SPLY_sale_large` INT(10),
`month_changeS_large` INT(10),
`cumulativeS_large` FLOAT(10,2),
`SPLY_cumulativeS_large` INT(10),
`cumulativeS_changeS_large`FLOAT(10,2),
`mid_sale` INT(10),
`SPLY_sale_mid` INT(10),
`month_changeS_mid` INT(10),
`cumulativeS_mid` FLOAT(10,2),
`SPLY_cumulativeS_mid` INT(10),
`cumulativeS_changeS_mid` FLOAT(10,2),
`small_sale` INT(10),
`SPLY_sale_small` INT(10),
`month_changeS_small` INT(10),
`cumulativeS_small`  FLOAT(10,2),
`SPLY_cumulativeS_small` INT(10),
`cumulativeS_changeS_small` FLOAT(10,2),
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
    
    
def 
    
InsertPSTable(users="root",passwords="6669635",databases="db_test1")




