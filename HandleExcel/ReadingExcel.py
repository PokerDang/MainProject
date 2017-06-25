# coding: utf-8
import pandas as pd
from pandas import Series, DataFrame
import xlrd
from datetime import datetime
import os

data_path = r'C:\Users\hezhending\Desktop\恒泰\期权做市_20170103.xls'
book = xlrd.open_workbook(data_path.decode('utf8'))  # 需要将中文进行转换