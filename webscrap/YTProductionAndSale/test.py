# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:01:58 2018

@author: suxiaolin
"""


'''
html中抓取数据
'''
#from lxml import etree
#url=r'D:\downloadTest\HTML\3.html'
#htmlf=open(url,'r',encoding="utf-8")
#html=htmlf.read()
#selector=etree.HTML(html)
#element='//*[@id="pf1"]/div[1]/div[21]/div'
#lls=[]
#year =selector.xpath('//*[@id="pf1"]/div[1]/div[14]/div[1]/text()')[0]
#month = selector.xpath('//*[@id="pf1"]/div[1]/div[14]/div[2]/text()')[0]
#lls.append(year)
#lls.append(month)
#path1='//*[@id="pf1"]/div[1]/div['
#path2=']/div/text()'
#for i in range(0,8):
#    for j in range(1,7):
#        num=str(j+i*7+20)
#        path=path1+num+path2
#        content=selector.xpath(path)
#        lls.append(content[0])
#print (lls)
        
'''
实现转换
'''
import os

cmd1='d:'
cmd2='cd'+' '+'downloadTest'
cmd3='E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe'+' '+'--dest-dir'+' '+'D:/downloadTest/HTML'+' '+'600066_20180403_24.pdf'+' '+'4.html'
#os.system(cmd1)
#os.system(cmd2)
os.system(cmd1 && cmd && cmd3)
cmd = '''d: &;
cd downloadTest &;
E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe --dest-dir D:/downloadTest/HTML 600066_20180403_24.pdf 4.html &;
'''
print (cmd)
os.system(cmd)