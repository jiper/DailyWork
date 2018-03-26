# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:50:45 2018

@author: suxiaolin
"""

class Exception1(Exception):
    print ("123")

def RaiseE():
    raise Exception1
def TEST():   
    try:
        RaiseE()
        print ("1")
    except (Exception):
        print ("2")
        return
    finally:
        print ("3")
    print (4)      
TEST()
    



