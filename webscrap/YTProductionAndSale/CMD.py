# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:43:41 2018

@author: suxiaolin
"""

# -*-coding:utf8-*-
import subprocess


def execute_command(cmd):
    print('start executing cmd...')
    s = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stderrinfo, stdoutinfo = s.communicate()
    print('stderrinfo is -------> %s and stdoutinfo is -------> %s' % (stderrinfo, stdoutinfo))
    print('finish executing cmd....')
    return s.returncode


cmd = r'D:\downloadTest create project --target 8  --name source2apk --path D:\HelloCSDN\ --package com.csdn.lhy --activity MainActivity'
cmd1=r'E:/JianLPeng/Software/pdfToHtml/pdf2htmlEX.exe'
cmd2 =r'E:\JianLPeng\Software\pdfToHtml\pdf2htmlEX.exe 600066_20171202_2.pdf 4.html'
cmd2 =r'E:\JianLPeng\Software\pdfToHtml\pdf2htmlEX.exe --dest-dir D:\downloadTest\HTML D:\downloadTest\600066_20171202_2.pdf 4.html'
result = execute_command(cmd2)
print('result:------>', result)