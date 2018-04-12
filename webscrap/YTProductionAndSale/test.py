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
import subprocess
from subprocess import Popen,PIPE
import os
##import commands
#cmd1='d:'
#cmd2='cd'+' '+'downloadTest'
#cmd3=r'E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe'+' '+'--dest-dir'+' '+r'D:/downloadTest/HTML'+' '+'600066_20180403_24.pdf'+' '+'4.html'
##os.system(cmd1)
##os.system(cmd2)
##os.system(cmd1 && cmd && cmd3)
##cmd = r'''d: &;cd downloadTest &;E:\JianLPeng\Software\pdfToHtml\pdf2htmlEX.exe --dest-dir D:\downloadTest\HTML 600066_20180403_24.pdf 4.html &;'''
#cmd=cmd1+' &;'+cmd2+' &;'+cmd3+' &;'
#cmd4=r'E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe'
##print (cmd)
#fhandle = open(r"C:\Users\suxiaolin\Desktop\123.txt", "w")  
#pipe = subprocess.Popen(cmd4, shell=True, stdout=subprocess.PIPE).stdout 
#print (pipe.read())
#fhandle.close()  
##cmd=cmd1+' && '+cmd2+' && '+cmd3
##subprocess.call(cmd, shell=True)
cmd =r'E:\JianLPeng\Software\pdfToHtml\pdf2htmlEX.exe 600066_20171202_2.pdf 4.html'
cmd1 =r'E:\JianLPeng\Software\pdfToHtml\pdf2htmlEX.exe'+' '+'600066_20171202_2.pdf'+' '+'4.html'
cmd3='E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe'
CMD=['E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe']
CMD1=['pdf2htmlEX.exe']


CMD2=['pdf2htmlEX']
pipe = subprocess.run(CMD2)

#os.system(CMD2[0])
