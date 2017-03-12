#coding:utf-8  
import matplotlib
from matplotlib import pyplot
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
from pandas import DataFrame,Series
import  numpy as np
from datetime import  datetime

import sys
sys.path.append('D:\Programs\Python\PythonProgramming\PythonProgramming')#添加PyFunction函数的路径

from WindPy import w

from PyFunction import*

w.start();

data = 1
name = Series(u'东方证券')
table = DataFrame(data,index = name, columns = [u'涨跌幅'])
