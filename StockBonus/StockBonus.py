# -*- coding: utf-8 -*-

# ******分红：计算成分股分红点数************


# ************************************头文件********************************************************************

import pandas as pd
from pandas import DataFrame,Series
import sys
sys.path.append('D:\Programs\Python\PythonProgramming\PythonProgramming')#添加PyFunction函数的路径

import matplotlib.pyplot as plt
import numpy as np
import tushare as ts
from datetime import datetime
#******************************************************************************************************************



#******************************************************************************************************************
#引入编写函数
from PyFunction import*
#******************************************************************************************************************


#**************************************万德头文件******************************************************************
from WindPy import w
w.start();
#********************************************************************************************************

data =w.wset("IndexConstituent","date=20160705;windcode=000016.SH;field=wind_code,i_weight")

