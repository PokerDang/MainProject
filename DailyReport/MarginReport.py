# -*- coding: utf-8 -*-

# ******统计两融信息************





import sys
sys.path.append('D:\Programs\Python\PythonProgramming\PythonProgramming')#添加PyFunction函数的路径

from WindPy import w
from WindPython.PyWindTimeFunction import*
w.start();



#融资融券
w_wset_data1=w.wset('MarginTradingUnderlying','date=20160216'); #融资标的余额统计
MarginBuy1=Series();# 融资买入额
MarginBuy2=Series();# 融资偿还额
MarginBuy3=Series();# 融资余额
margin_num = len(w_wset_data1.Data[1]) #截止日融资标的数量
margin_code = Series(w_wset_data1.Data[1])
margin_name = Series(w_wset_data1.Data[2])
#MarginList = DataFrame() #融资标的列表

BeginDay = datetime(2016,2,15)
EndDay = datetime(2016,2,15)
MarginData = DataFrame()
MarginData=MarginData.reindex(index=margin_code,columns=[u'股票名称',u'融资买入额',u'融资偿还额',u'融资余额'])  #命名索引

num = 0
for code in margin_code:
    data=w.wsd(code,'mrg_long_amt,mrg_long_repay,mrg_long_bal',BeginDay,EndDay)
    MarginBuy1 = data.Data[0][0] #从万德取出的是list数据，需要取值
    MarginBuy2 = data.Data[1][0]
    MarginBuy3 = data.Data[2][0]
    MarginData.ix[code] = [margin_name[num],MarginBuy1,MarginBuy2,MarginBuy3]
    num = num + 1

#汇总
MarginDataTotal = DataFrame()
MarginDataSH = Series()
MarginDataSZ = Series()


MarginDataTotal=MarginDataTotal.reindex(index=[u'两市',u'沪市',u'深市'],columns=[u'融资买入额',u'融资偿还额',u'融资余额'])
