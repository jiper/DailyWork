  
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:25:31 2018

@author: JianLPeng
"""




import requests
from requests.exceptions import RequestException
import re
import json
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

import datetime

if (datetime.date(2017,8,9).__ge__(datetime.date(2017,4,5))):
    print ("1")