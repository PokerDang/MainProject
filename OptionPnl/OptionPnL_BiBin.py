# -*- coding: utf-8 -*-

#*************
#此版本为毕斌比较根网与恒泰比较，有较多的输出
#*************

#*Head File*
from datetime import datetime
import pandas as pd
from pandas import DataFrame,Series
from WindPy import w
#*******************************************#

#*Initial Cash*
InitialCash_ETF = 158000000.00 
InitialCash_Option =  49000000.00 
InitialCash_Future =  22800000.00 



#*******************************************#



#*Change Parameters*
date = "2016-10-12"
TotalAsset_ETF = 184115566.49 
Margin_Option =  16067663.80 
Cash_Option = 9614426.20 

Margin_Future = 12645540.00 
Cash_Future = 11088487.01 


data = pd.read_excel\
(r'E:/Programs/Python/PythonProgramming/PythonProgramming/OptionPnl/OptionPosition/20161012-Close.xls')

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
contract_size = 10000


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
    print i
    if data.ix[i,u'合约方向']== u'\u5356\u51fa':
        data.ix[i,'Position'] = -data.ix[i,u'当日持仓数量']
    else:
        data.ix[i,'Position'] = data.ix[i,u'当日持仓数量']

    name = '%d' %code + '.SH'
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


path = 'E:\Programs\Python\PythonProgramming\PythonProgramming\OptionPnl\BiBin'
filename = path + '/'+begin_date+' PnL'+'.txt'

result = open(filename,'w')
result.write('***********'+begin_date+'  PnL**************'+'\n\n')


#ETF Output
result.write('TotalAsset_ETF: ')
result.write(str(TotalAsset_ETF))
result.write('\n')

result.write('InitialCash_ETF: ')
result.write(str(InitialCash_ETF))
result.write('\n')

result.write('PnL_ETF: ')
result.write(str(PnL_ETF))
result.write('\n\n')

#Future Output
result.write('Margin_Future: ')
result.write(str(Margin_Future))
result.write('\n')

result.write('Cash_Future: ')
result.write(str(Cash_Future))
result.write('\n')

result.write('InitialCash_Future: ')
result.write(str(InitialCash_Future))
result.write('\n')

result.write('PnL_Future: ')
result.write(str(PnL_Future))
result.write('\n\n')

#Option Output


result.write('TotalAsset_Option: ')
result.write(str(TotalAsset_Option))
result.write('\n')

result.write('InitialCash_Option: ')
result.write(str(InitialCash_Option))
result.write('\n')

result.write('LongPositionCloseValue: ')
result.write(str(LongPositionCloseValue))
result.write('\n')

result.write('ShortPositionCloseValue: ')
result.write(str(ShortPositionCloseValue))
result.write('\n')

result.write('LongPositionSettleValue: ')
result.write(str(LongPositionCloseValue))
result.write('\n')

result.write('ShortPositionSettleValue: ')
result.write(str(ShortPositionCloseValue))
result.write('\n')




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



