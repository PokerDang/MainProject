# encoding: utf-8

#导入现有的期权合约，进行分类，测算Synthetic strategy, covered call, OTM Strategy

from WindPy import *
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt
w.start()


#*********基础数据*********************************#

#读取合约
option50ETF_data = w.wset("optioncontractbasicinfo",
       "exchange=sse;windcode=510050.SH;status=trading;field=wind_code,"
       "sec_name,call_or_put,exercise_price,contract_unit,limit_month,exercise_date")
#白糖期权
optionSR_data = w.wset("optionfuturescontractbasicinfo",
       "exchange=CZCE;productcode=SR;contract=all;field=wind_code,"
       "sec_name,call_or_put,exercise_price,contract_unit,limit_month,expire_date")
#豆粕期权
optionM_data = w.wset("optionfuturescontractbasicinfo",
       "exchange=DCE;productcode=M;contract=all;field=wind_code,"
       "sec_name,call_or_put,exercise_price,contract_unit,limit_month,expire_date")

#转成pandas dataframe
option50ETF = pd.DataFrame(option50ETF_data.Data,index = option50ETF_data.Fields,
                           columns = option50ETF_data.Data[1]).T
del option50ETF['sec_name']
optionSR = pd.DataFrame(optionSR_data.Data,index = optionSR_data.Fields,
                        columns=optionSR_data.Data[1]).T
del optionSR['sec_name']
optionM = pd.DataFrame(optionM_data.Data,index = optionM_data.Fields,
                       columns=optionM_data.Data[1]).T
del optionM['sec_name']
#按行权价，到期月份从前到后排序
option50ETF = option50ETF.sort_index(by=['limit_month','exercise_price'])
optionSR = optionSR.sort_index(by=['limit_month','exercise_price'])
optionM = optionM.sort_index(by=['limit_month','exercise_price'])

#*********基础数据*********************************#



#*********交易策略*********************************#

#全局参数


DAYS2018 = pd.date_range('2018/1/1', '2018/12/31')
HOLIDAYS = pd.to_datetime(['2018/2/15','2018/2/16','2018/2/19','2018/2/20','2018/2/21',
            '2018/4/5','2018/4/6','2018/4/30','2018/5/1','2018/6/18',
	        '2018/9/24','2018/10/1','2018/10/2','2018/10/3','2018/10/4',
            '2018/10/5'])
WORKINGDAYS2018 = pd.bdate_range('2018/1/1', '2018/12/31') - HOLIDAYS#2018工作日，去掉中国的假日

calenderdays = len(DAYS2018)
workingdays = len(WORKINGDAYS2018)


lasttradingday = pd.DataFrame({'Option Last Day':['2018/1/25','2018/2/28','2018/3/28','2018/4/25','2018/5/23',
                                                  '2018/6/27','2018/7/25','2018/8/22','2018/9/26','2018/10/24',
                                                  '2018/11/28','2018/12/26'],
                               'Future Last Day':['2018/1/25','2018/2/22','2018/3/16','2018/4/20','2018/5/18',
                                                  '2018/6/15','2018/7/20','2018/8/17','2018/9/21','2018/10/19',
                                                  '2018/11/16','2018/12/21']},
                                index = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])
print lasttradingday

today = '2018/7/22'
optiontradedayAug = len(pd.bdate_range(today, '2018/8/22') - HOLIDAYS)




#*********交易策略*********************************#