# -*- coding:utf-8 -*-
#Python 3.5.0

#第六章 量化工具-数学 中代码测试，将其中Tesla 换成50ETF，从万德中获得数据
from WindPy import w
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np
import seaborn as sns
from datetime import datetime,date
import statsmodels.api as sm
from statsmodels import regression

w.start();

# 取数据的命令如何写可以用命令生成器来辅助完成

sh50etf_data=w.wsd("510050.SH", "open,high,low,close,volume", "2013-01-01", "2017-12-31", "Fill=Previous")
sh300etf_data= w.wsd("510300.SH", "open,high,low,close,volume", "2013-01-01", "2017-12-31", "Fill=Previous")

sh50etf_df=pd.DataFrame(sh50etf_data.Data,index=sh50etf_data.Fields,columns=sh50etf_data.Times)
sh50etf_df = sh50etf_df.T
#sh300etf_df=pd.DataFrame(sh300etf_data.Data,index=sh300etf_data.Fields,columns=sh300etf_data.Times)
#sh300etf_df = sh300etf_df.T
#添加每日上涨下跌，neiChangeratio
sh50etf_df['netChangeRatio'] = sh50etf_df['CLOSE'].pct_change()
sh50etf_df['netChangeRatio'].ix[0] = 0
#sh300etf_df['netChangeRatio'] = sh300etf_df['CLOSE'].pct_change()
#sh300etf_df['netChangeRatio'].ix[0] = 0

sh50etf_close = sh50etf_df['CLOSE']
x=np.arange(0,sh50etf_close.shape[0])
y=sh50etf_close.values

#最小二乘法拟合

def regress_y(y):
    y=y
    x = np.arange(0,len(y))
    x=sm.add_constant(x)
    model = regression.linear_model.OLS(y,x).fit()
    return model
model = regress_y(y)
b = model.params[0]
k = model.params[1]

y_fit = k*x + b
plt.plot(x,y)
plt.plot(x,y_fit,'r')
model.summary()

#6.2.1
#**********************

from abc import ABCMeta,abstractmethod
import six

K_INIT_LIVING_DAYS = 27375
class Person(object):
    def __init__(self):
        self.living = K_INIT_LIVING_DAYS
        self.happiness = 0
        self.wealth = 0
        self.fame = 0
        self.living_day = 0
    def live_one_day(self,seek):
        consume_living,hapiness,wealth,fame = seek.do_seek_day()
        self.living -= consume_living
        self.happiness += hapiness
        self.wealth += wealth
        self.fame += fame
        self.living += 1

class BaseSeekDay(six.with_metaclass(ABCMeta,object)):
    def __init__(self):
        self.living_consume = 0
        self.happiness_base = 0
        self.weath_base = 0
        self.fame_base = 0
        self.living_factor = [0]
        self.happiness_factor = [0]
        self.weath_factor = 0
        self.fame_factor = 0
        self.do_seek_day_cnt = 0
        self._init_self()
    @abstractmethod
    def _init_(self,*args,**kwargs):
        pass
    @abstractmethod
    def _gen_living_days(self,*args,**kwargs):
        pass
    def do_seek_day(self):
        if self.do_seek_day_cnt >= len(self.living_factor):
            consume_living = self.living_factor[-1]*self.living_consume
        else:
            consume_living = self.living_factor[self.do_seek_day_cnt]*self.living_consume
        if self.do_seek_day_cnt >= len(self.happiness_factor):
            happiness = self.happiness_factor[-1] * self.happiness_base
        else:
            happiness = self.happiness_factor[self.do_seek_day_cnt]*self.happiness_base
        if self.do_seek_day_cnt >= len(self.weath_factor):
            wealth = self.weath_factor[-1] * self.weath_base
        else:
            wealth = self.weath_factor[self.do_seek_day_cnt]*self.weath_base
        if self.do_seek_day_cnt >= len(self.fame_factor):




#**********************










