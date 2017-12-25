#coding:utf-8
'''字符编码更正，python默认是acii模式，没有支持utf8'''

#*********************************************
#将Wind中的时间函数，转换成正常格式输出

#*********************************************







from datetime import  datetime
import numpy as np
import pandas as pd
import math
from pandas import Series,DataFrame
from WindPy import w


#pywind_tdays_count：返回startdate和enddate之间的交易日数
#***输入参数：
#code: 标的代码，如'000016.SH'
#startdate:开始日期，可用字符串格式'2016-02-05'或者datetime格式
#enddate  :结束日期，可用字符串格式'2016-02-05'或者datetime格式
#w        :万德传入参数
#***返回参数：
#pywind_tdays_count:开始日期与结束日期间交易日总数
def pywind_tdays_count(code,startdate,enddate,w):
    tdays = w.tdays(startdate,enddate)
    return len(tdays.Times)





#pywind_tdays：返回startdate和enddate之间的交易日序列
#***输入参数：
#code: 标的代码，如'000016.SH'
#startdate:开始日期，可用字符串格式'2016-02-05'或者datetime格式
#enddate  :结束日期，可用字符串格式'2016-02-05'或者datetime格式
#w        :万德传入参数
#***返回参数：
#pywind_tdays_count:开始日期与结束日期间交易日序列
def pywind_tdays(code,startdate,enddate,w):
    tdays = w.tdays(startdate,enddate)
    dates = pd.Series()
    for line in tdays.Times:
        day = str(line)[0:10]
        dates=dates.append(pd.Series(day))
    return dates




#pywind_data：返回startdate和enddate之间的日交易数据
#***输入参数：
#code: 标的代码，如'000016.SH'
#info:价格信息，如'open,high,low,close'
#startdate:开始日期，可用字符串格式'2016-02-05'或者datetime格式
#enddate  :结束日期，可用字符串格式'2016-02-05'或者datetime格式
#w        :万德传入参数
#***返回参数：
#pywind_data:开始日期与结束日期间交易日护具

def pywind_data(code,info,startdate,enddate,w):
    tdays = w.tdays(startdate,enddate)
    dates = pywind_tdays(code,startdate,enddate,w)
    w_wsd_data=w.wsd(code, info, startdate, enddate, 'Fill=Previous')
    fm=pd.DataFrame(w_wsd_data.Data,index = w_wsd_data.Fields,columns=dates)
    fm = fm.T
    #codename = ['Codes']
    #添加代码序列
    #addcode = [code]*pywind_tdays_count(code,startdate,enddate,w)
    #addcode = pd.DataFrame(addcode,index = dates,columns=['Codes'])
#    dat1.merge(dat2, on=['secID', 'tradeDate'])
    #fm = pd.concat([addcode,fm],axis=1)
    return fm
    #index==w_wsd_data.Fields,


#pywind_reporttable：返回date日的相关交易统计
#***输入参数：
#codes: 标的代码，如'000016.SH'
#names: 标的代码对应的中文名称
#info:价格信息，如'open,high,low,close'
#info_name:info对应中文名称
#date:日期，可用字符串格式'2016-02-05'或者datetime格式
#w        :万德传入参数
def pywind_reporttable(codes,names,info,info_name,date,w):
    report_table=DataFrame()
    colnum = len(names)
    for i in range(colnum):
        w_wsd_data=w.wsd(codes[i], info, date, date, 'Fill=Previous')
        fm = DataFrame(w_wsd_data.Data,index=info_name,columns=Series(names[i]))
        report_table = pd.concat([report_table,fm],axis=1)
    report_table.ix[u'成交额']=report_table.ix[u'成交额']/100000000  #成交额单位亿元
    return report_table

#pywind_reporttable：天数回退，按交易日算
#***输入参数：
#offset: 回退天数，'-1'表示回退一个交易日
#date: 日期，可用字符串格式'2016-02-05'或者datetime格式
#w        :万德传入参数
#输出参数
#pywind_tdaysoffset: datetime 格式日期
def pywind_tdaysoffset(offset,date,w):
    return w.tdaysoffset(offset,date).Times[0]

#pywind_pct：date日算起，过去N个交易日涨跌幅,以收盘价算
#***输入参数：
#code: 标的代码
#date: 回退日期，可用字符串格式'2016-02-05'或者datetime格式
#N: 回退交易日数
#w        :万德传入参数
#输出参数
#pywind_pct: 涨跌幅百分比
def pywind_pct(code,date,offset,w):
    back_date = pywind_tdaysoffset(offset,date,w)
    back_close = w.wsd(code,'close',back_date,back_date).Data[0][0]
    close = w.wsd(code,'close',date,date).Data[0][0]
    if(np.isnan(back_close) or np.isnan(close) ):
        return np.nan
    else:
        return (close - back_close)/back_close



def pywind_NdayPct(codes,names,Nday,date,w):
    table = DataFrame(index = names, columns = [str(-Nday)+u'日涨跌幅'])
    colnum = len(names)
    for i in range(colnum):
        stockPct = pywind_pct(codes[i],date,Nday,w)
        table.ix[i] = stockPct
    return table




#PyFun_DateToStr：将Python中Datetime格式的日期返回为字符串格式
#***输入参数：
#date: Python Datetime格式的日期
#***输出参数：
#PyFun_DateToStr: 字符串格式，如'2016-01-02'
def PyFun_DateToStr(date):
    return date.strftime('%Y-%m-%d')

