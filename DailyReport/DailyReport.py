# -*- coding: utf-8 -*-

# ******日报：统计每日市场交易信息************


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


#********************************************************************************************************
#读取指标数据
#主要指数指标
table1 = pd.read_excel('D:\Programs\Python\Data\DailyReport\Indice.xlsx', u'主要指数指标')
#权重个股和板块指标
table2 = pd.read_excel('D:\Programs\Python\Data\DailyReport\Indice.xlsx', u'权重个股和板块指标')
#申万一级行业指标
table3 = pd.read_excel('D:\Programs\Python\Data\DailyReport\Indice.xlsx', u'申万一级行业指标')
#申万二级行业指标
table4 = pd.read_excel('D:\Programs\Python\Data\DailyReport\Indice.xlsx', u'申万二级行业指标')
#概念板块指标
table5 = pd.read_excel('D:\Programs\Python\Data\DailyReport\Indice.xlsx', u'概念板块指标')
#********************************************************************************************************

#********************************************************************************************************
#各板块当日指标

info = 'open,close,high,low,pct_chg,amt'
info_name = [u'开盘价',u'收盘价',u'最高价',u'最低价',u'涨跌幅',u'成交额']
date = datetime(2016,7,4)


#主要指数指标
codes1 = Series(table1.ix[:,0])
names1 = Series(table1.ix[:,1])
intraday_table1=pywind_reporttable(codes1,names1,info,info_name,date,w)
#report_table1.ix['涨跌幅'].plot(kind='bar')
#plt.show()


#权重个股和板块指标
codes2 = Series(table2.ix[:,0])
names2 = Series(table2.ix[:,1])
intraday_table2=pywind_reporttable(codes2,names2,info,info_name,date,w)

#申万一级行业指标
codes3 = Series(table3.ix[:,0])
names3 = Series(table3.ix[:,1])
intraday_table3=pywind_reporttable(codes3,names3,info,info_name,date,w)

#申万二级行业指标
codes4 = Series(table4.ix[:,0])
names4 = Series(table4.ix[:,1])
intraday_table4=pywind_reporttable(codes4,names4,info,info_name,date,w)

#概念板块指标
codes5 = Series(table5.ix[:,0])
names5 = Series(table5.ix[:,1])
intraday_table5=pywind_reporttable(codes5,names5,info,info_name,date,w)

'''
#********************************************************************************************************
#统计沪深两市过去十个交易日两融余额变化
enddate_margin = datetime(2016,2,5)
offsetday_margin = -10
startdate_margin = pywind_tdaysoffset(offsetday_margin,enddate_margin,w)

#沪市
margin_sh=ts.sh_margins(PyFun_DateToStr(startdate_margin), PyFun_DateToStr(enddate_margin))#将datetime格式转换成字符串格式输入
name_margin = ['交易日期','融资余额(亿元)','融资买入额(亿元)','融券余量(万股)','融券余量金额(亿元)','融券卖出量(万股)','融资融券余额(亿元)']
margin_sh.columns = name_margin
margin_sh['融资余额(亿元)'] = margin_sh['融资余额(亿元)']/(100000000)
margin_sh['融资买入额(亿元)'] = margin_sh['融资买入额(亿元)']/(100000000)
margin_sh['融券余量金额(亿元)'] = margin_sh['融券余量金额(亿元)']/(100000000)
margin_sh['融资融券余额(亿元)'] = margin_sh['融资融券余额(亿元)']/(100000000)
margin_sh['融券余量(万股)'] = margin_sh['融券余量(万股)']/(10000)
margin_sh['融券卖出量(万股)'] = margin_sh['融券卖出量(万股)']/(10000)

#深市
margin_sz=ts.sz_margins(PyFun_DateToStr(startdate_margin), PyFun_DateToStr(enddate_margin))#将datetime格式转换成字符串格式输入




#********************************************************************************************************
'''

#找出各个板块分类中当日涨跌幅最大的板块
#********************************************************************************************************

#申万一级行业
SW1J_SortByPctHigh = intraday_table3.T #涨幅排列的板块
SW1J_SortByPctHigh = SW1J_SortByPctHigh.sort(columns=u'涨跌幅',ascending = False)

SW1J_SortByPctLow = intraday_table3.T #跌幅排列的板块
SW1J_SortByPctLow = SW1J_SortByPctLow.sort(columns=u'涨跌幅')

#申万二级行业
SW2J_SortByPctHigh = intraday_table4.T #涨幅排列的板块
SW2J_SortByPctHigh = SW2J_SortByPctHigh.sort(columns=u'涨跌幅',ascending = False)

SW2J_SortByPctLow = intraday_table4.T #跌幅排列的板块
SW2J_SortByPctLow = SW2J_SortByPctLow.sort(columns=u'涨跌幅')

#概念行业
GNHY_SortByPctHigh = intraday_table5.T #涨幅排列的板块
GNHY_SortByPctHigh = GNHY_SortByPctHigh.sort(columns=u'涨跌幅',ascending = False)

GNHY_SortByPctLow = intraday_table5.T #跌幅排列的板块
GNHY_SortByPctLow = GNHY_SortByPctLow.sort(columns=u'涨跌幅')


#输出到CSV文件
SW1J_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_SortByPctHigh.csv',encoding="gb2312")
SW1J_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_SortByPctLow.csv',encoding="gb2312")

SW2J_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_SortByPctHigh.csv',encoding="gb2312")
SW2J_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_SortByPctLow.csv',encoding="gb2312")


GNHY_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_SortByPctHigh.csv',encoding="gb2312")
GNHY_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_SortByPctLow.csv',encoding="gb2312")

#********************************************************************************************************


#找出过去N日涨跌幅最大的板块
#********************************************************************************************************
N5 = -5
N10 = -10
N20 = -20

SW1J_5day = pywind_NdayPct(codes3,names3,N5,date,w)  #申万一级行业最近五日收益率
SW1J_10day = pywind_NdayPct(codes3,names3,N10,date,w) #申万一级行业最近十日收益率
SW1J_20day = pywind_NdayPct(codes3,names3,N20,date,w) #申万一级行业最近二十日收益率

SW2J_5day = pywind_NdayPct(codes4,names4,N5,date,w)  #申万二级行业最近五日收益率
SW2J_10day = pywind_NdayPct(codes4,names4,N10,date,w) #申万二级行业最近十日收益率
SW2J_20day = pywind_NdayPct(codes4,names4,N20,date,w) #申万二级行业最近二十日收益率

GNHY_5day = pywind_NdayPct(codes5,names5,N5,date,w)  #概念行业最近五日收益率
GNHY_10day = pywind_NdayPct(codes5,names5,N10,date,w) #概念行业最近十日收益率
GNHY_20day = pywind_NdayPct(codes5,names5,N20,date,w) #概念行业最近二十日收益率


SW1J_5day_SortByPctHigh = SW1J_5day.sort(columns=str(-N5)+u'日涨跌幅',ascending = False)
SW1J_5day_SortByPctLow = SW1J_5day.sort(columns=str(-N5)+u'日涨跌幅')
SW1J_10day_SortByPctHigh = SW1J_10day.sort(columns=str(-N10)+u'日涨跌幅',ascending = False)
SW1J_10day_SortByPctLow = SW1J_10day.sort(columns=str(-N10)+u'日涨跌幅')
SW1J_20day_SortByPctHigh = SW1J_20day.sort(columns=str(-N20)+u'日涨跌幅',ascending = False)
SW1J_20day_SortByPctLow = SW1J_20day.sort(columns=str(-N20)+u'日涨跌幅')


SW2J_5day_SortByPctHigh = SW2J_5day.sort(columns=str(-N5)+u'日涨跌幅',ascending = False)
SW2J_5day_SortByPctLow = SW2J_5day.sort(columns=str(-N5)+u'日涨跌幅')
SW2J_10day_SortByPctHigh = SW2J_10day.sort(columns=str(-N10)+u'日涨跌幅',ascending = False)
SW2J_10day_SortByPctLow = SW2J_10day.sort(columns=str(-N10)+u'日涨跌幅')
SW2J_20day_SortByPctHigh = SW2J_20day.sort(columns=str(-N20)+u'日涨跌幅',ascending = False)
SW2J_20day_SortByPctLow = SW2J_20day.sort(columns=str(-N20)+u'日涨跌幅')


GNHY_5day_SortByPctHigh = GNHY_5day.sort(columns=str(-N5)+u'日涨跌幅',ascending = False)
GNHY_5day_SortByPctLow = GNHY_5day.sort(columns=str(-N5)+u'日涨跌幅')
GNHY_10day_SortByPctHigh = GNHY_10day.sort(columns=str(-N10)+u'日涨跌幅',ascending = False)
GNHY_10day_SortByPctLow = GNHY_10day.sort(columns=str(-N10)+u'日涨跌幅')
GNHY_20day_SortByPctHigh = GNHY_20day.sort(columns=str(-N20)+u'日涨跌幅',ascending = False)
GNHY_20day_SortByPctLow = GNHY_20day.sort(columns=str(-N20)+u'日涨跌幅')

SW1J_5day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_5day_SortByPctHigh.csv',encoding="gb2312")
SW1J_5day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_5day_SortByPctLow.csv',encoding="gb2312")
SW1J_10day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_10day_SortByPctHigh.csv',encoding="gb2312")
SW1J_10day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_10day_SortByPctLow.csv',encoding="gb2312")
SW1J_20day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_20day_SortByPctHigh.csv',encoding="gb2312")
SW1J_20day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW1J_20day_SortByPctLow.csv',encoding="gb2312")

SW2J_5day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_5day_SortByPctHigh.csv',encoding="gb2312")
SW2J_5day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_5day_SortByPctLow.csv',encoding="gb2312")
SW2J_10day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_10day_SortByPctHigh.csv',encoding="gb2312")
SW2J_10day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_10day_SortByPctLow.csv',encoding="gb2312")
SW2J_20day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_20day_SortByPctHigh.csv',encoding="gb2312")
SW2J_20day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/SW2J_20day_SortByPctLow.csv',encoding="gb2312")

GNHY_5day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_5day_SortByPctHigh.csv',encoding="gb2312")
GNHY_5day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_5day_SortByPctLow.csv',encoding="gb2312")
GNHY_10day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_10day_SortByPctHigh.csv',encoding="gb2312")
GNHY_10day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_10day_SortByPctLow.csv',encoding="gb2312")
GNHY_20day_SortByPctHigh.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_20day_SortByPctHigh.csv',encoding="gb2312")
GNHY_20day_SortByPctLow.to_csv('D:/Programs/Python/PythonProgramming/PythonProgramming/OutData/GNHY_20day_SortByPctLow.csv',encoding="gb2312")
#********************************************************************************************************