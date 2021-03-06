# -*- coding: utf-8 -*-

# ******日报************



#****万德头文件*******
from WindPy import w
w.start();
#********************

#****头文件*******
import pandas as pd
import datetime
#********************


lasttradedate = "2018-04-13" #最后交易日
lastweekdate = "2018-04-09" #最近一周起始日
lastmonthdate = "2018-04-01" #最近一月起始日
lastyeardate = "2018-01-01" #最近一年起始日



index = "000016.SH,000001.SH,000300.SH,399005.SZ"
name = [u'上证50',u'上证综指',u'沪深300',u'中小板指']

dayperiod = "startDate="+lasttradedate+";"+"endDate="+lasttradedate
weekperiod = "startDate="+lastweekdate+";"+"endDate="+lasttradedate
monthperiod = "startDate="+lastmonthdate+";"+"endDate="+lasttradedate
yearperiod = "startDate="+lastyeardate+";"+"endDate="+lasttradedate

dataday = pd.DataFrame(w.wss(index, "pct_chg_per",dayperiod).Data,columns=name,index=[u'日涨跌幅']).T
dataweek = pd.DataFrame(w.wss(index, "pct_chg_per",weekperiod).Data,columns=name,index=[u'周涨跌幅']).T
datamonth = pd.DataFrame(w.wss(index, "pct_chg_per",monthperiod).Data,columns=name,index=[u'月涨跌幅']).T
datayear = pd.DataFrame(w.wss(index, "pct_chg_per",yearperiod).Data,columns=name,index=[u'年涨跌幅']).T

datalatestprice = pd.DataFrame(w.wsd(index, "close", lasttradedate,lasttradedate,\
                                     "Fill=Previous").Data,index=[u'最新价'],columns=name).T

report = pd.concat([datalatestprice,dataday,dataweek,datamonth,datayear],axis=1,join_axes=[datalatestprice.index])#合并
#report.to_excel('report'+'_'+lasttradedate+'.xlsx',sheet_name='Sheet1')

print report,'\n\n'



#Future
IHFuture = "IH1804.CFE,IH1805.CFE,IH1806.CFE,IH1809.CFE"
IHName = ['IH1804','IH1805','IH1806','IH1809']
IHlatestprice = pd.DataFrame(w.wsd(IHFuture, "close", lasttradedate,lasttradedate,\
                                   "Fill=Previous").Data,index=[u'最新价'],columns=IHName).T

IFFuture = "IF1804.CFE,IF1805.CFE,IF1806.CFE,IF1809.CFE"
IFName = ['IF1804','IF1805','IF1806','IF1809']
IFlatestprice = pd.DataFrame(w.wsd(IFFuture, "close", lasttradedate,lasttradedate, \
                                   "Fill=Previous").Data,index=[u'最新价'],columns=IFName).T

ICFuture = "IC1804.CFE,IC1805.CFE,IC1806.CFE,IC1809.CFE"
ICName = ['IC1804','IC1805','IC1806','IC1809']
IClatestprice = pd.DataFrame(w.wsd(ICFuture, "close", lasttradedate,lasttradedate,\
                                   "Fill=Previous").Data,index=[u'最新价'],columns=ICName).T

print IHlatestprice,'\n',IFlatestprice,'\n',IClatestprice

#IHlatestprice.to_excel('test.xlsx',sheet_name='Sheet1')


#Option



#Divident

#分红实施情况
DividentSZ50 = w.wset("dividendproposal","ordertype=1;startdate="+lastyeardate+\
                       ";enddate="+lasttradedate+";sectorid=1000000087000000")#上证50
DividentHS300 = w.wset("dividendproposal","ordertype=1;startdate="+lastyeardate+\
                       ";enddate="+lasttradedate+";sectorid=1000000090000000")#沪深300
DividentZZ500 = w.wset("dividendproposal","ordertype=1;startdate="+lastyeardate+\
                       ";enddate="+lasttradedate+";sectorid=1000008491000000")#ZZ500