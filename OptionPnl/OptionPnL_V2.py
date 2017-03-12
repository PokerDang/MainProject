# -*- coding: utf-8 -*-

#**********************************************************
#此版本加入了2016年11月30日分红后的合约，在之前版本上进行修改
#**********************************************************

#*Head File*
from datetime import datetime
import pandas as pd
from pandas import DataFrame,Series
from WindPy import w
#*******************************************#

#*Initial Cash*
InitialCash_ETF = 213000000.00 
InitialCash_Option =  84000000.00 
InitialCash_Future =  32800000.00 



#*******************************************#



#*Change Parameters*
date = "2016-12-15"
TotalAsset_ETF = 241787779.47 

Margin_Option =  33903597.67 
Cash_Option = 11763013.48 

Margin_Future =  27499248.00 
Cash_Future =  8004517.92 



data = pd.read_excel\
(r'E:/Programs/Python/PythonProgramming/PythonProgramming/OptionPnl/OptionPosition/20161215-Close.xls')

#*******************************************#

 

#*Time*
#date = datetime(2016,8,11)

begin_date = date
end_date = date
#*******************************************#


#*Wind*

#*******************************************#



#*ETF*
PnL_ETF = 0.0
PnL_ETF = TotalAsset_ETF -InitialCash_ETF
#*******************************************#



#*Future*
PnL_Future = 0.0
PnL_Future = Margin_Future + Cash_Future - InitialCash_Future
#*******************************************#




#*Repo*
RepoInterestTotal = 0.0
#*******************************************#



#*Option*

TotalAsset_Option = 0.0
#contract_size = 10000


TotalAsset_Option = Margin_Option + Cash_Option


LongPositionCloseValue = 0.0  #多头收盘价市值
LongPositionSettleValue = 0.0  #多头结算价市值
ShortPositionCloseValue = 0.0  #空头收盘价市值
ShortPositionSettleValue = 0.0  #空头收盘价市值

#利用万德获取收盘价、结算价等
w.start();
data['settle_price'] = pd.Series(0.0,index=data.index)
data['close_price'] = pd.Series(0.0,index=data.index)
data['Position'] = pd.Series(0.0,index=data.index)






i=0
for code in data[u'合约代码']:
    if data.ix[i,u'合约方向']== u'\u5356\u51fa':
        data.ix[i,'Position'] = -data.ix[i,u'当日持仓数量']
    else:
        data.ix[i,'Position'] = data.ix[i,u'当日持仓数量']

    name = '%d' %code + '.SH'
    
    contract_size = w.wsd(name, "exe_ratio", begin_date, \
    end_date, "").Data[0][0] #确定合约乘数
    
    print i
    data.ix[i,'settle_price'] = w.wsd(name, "settle", begin_date, \
    end_date, "").Data[0][0]
    data.ix[i,'close_price'] = w.wsd(name, "close", begin_date,\
    end_date, "").Data[0][0]
    if data.ix[i,'Position']>0:
        LongPositionCloseValue = LongPositionCloseValue+data.ix\
            [i,'Position']*data.ix[i,'close_price']*contract_size
        LongPositionSettleValue = LongPositionSettleValue+data.ix\
            [i,'Position']*data.ix[i,'settle_price']*contract_size
    else:
        ShortPositionCloseValue = ShortPositionCloseValue+data.ix\
            [i,'Position']*data.ix[i,'close_price']*contract_size
        ShortPositionSettleValue = ShortPositionSettleValue+data.ix\
            [i,'Position']*data.ix[i,'settle_price']*contract_size
    i=i+1

PnLClose_Option = 0.0
PnLSettle_Option = 0.0

PnLSettle_Option = TotalAsset_Option + LongPositionSettleValue +\
     ShortPositionSettleValue - InitialCash_Option

PnLClose_Option = TotalAsset_Option + LongPositionCloseValue +\
     ShortPositionCloseValue - InitialCash_Option
#*******************************************#


#*Transaction Cost*

#*******************************************#

#*Total*

PnLSettle_toal = 0.0
PnLClose_toal = 0.0



PnLSettle_toal = PnL_ETF+PnL_Future + PnLSettle_Option
PnLClose_toal = PnL_ETF+PnL_Future + PnLClose_Option


#*******************************************#




#*Output*


path = 'E:\Programs\Python\PythonProgramming\PythonProgramming\OptionPnl\PnL'
filename = path + '/'+begin_date+' PnL'+'.txt'

result = open(filename,'w')
result.write('***********'+begin_date+'  PnL**************'+'\n\n')


#ETF Output

result.write('PnL_ETF: ')
result.write(str(PnL_ETF))
result.write('\n\n')

#Future Output

result.write('PnL_Future: ')
result.write(str(PnL_Future))
result.write('\n\n')

#Option Output





result.write('PnLSettle_Option: ')
result.write(str(PnLSettle_Option))
result.write('\n')
result.write('PnLClose_Option: ')
result.write(str(PnLClose_Option))
result.write('\n\n\n')





#Output Summary
result.write('Summary of PnL: ')
result.write('\n')
result.write('PnLSettle_toal: ')
result.write(str(PnLSettle_toal))
result.write('\n')
result.write('PnLClose_toal: ')
result.write(str(PnLClose_toal))
result.write('\n\n')


result.write('*****************************************')

print "PnLSettle_toal: ",PnLSettle_toal
print "PnLClose_toal: ",PnLClose_toal

result.close()
#*******************************************#



