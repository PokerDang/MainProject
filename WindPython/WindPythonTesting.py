#coding:utf-8


#from pandas import Series,DataFrame
#import datetime
import Import_Head
from WindPy import w  
import pandas as pd
#万德测试程序
from WindPythonDataGet import*
w.start();



#********************测试WindPythonDataGet，将wind数据格式转为DataFrame****************************************
startdate = '2016-01-01'
enddate = '2016-01-10'
code = '000016.SH'
info = 'open,high,low'

w_wsd_data=w.wsd(code, info, startdate, enddate, 'Fill=Previous')

dates = pywind_tdays(code,startdate,enddate,w)

addcode= [code,code,code,code,code]
addcode = pd.DataFrame(addcode,index = dates)
fm = pywind_data(code,info,startdate,enddate,w)
print('fm:')
print(fm)
#*****************************************************************************************************************

'''
startdate = '2016-01-01'
enddate = '2016-01-10'
w_wsd_data=w.wset('SectorConstituent','date=20160121;sectorId=0201a10000000000');
DataFrame(w_wsd_data)
print(w_wsd_data)
'''