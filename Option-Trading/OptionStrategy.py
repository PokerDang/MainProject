# encoding: utf-8

#导入现有的期权合约，进行分类，测算Synthetic strategy, covered call, OTM Strategy

from WindPy import *
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt

w.start()

#读取合约
option50ETF_data = w.wset("optioncontractbasicinfo",
       "exchange=sse;windcode=510050.SH;status=trading;field=wind_code,"
       "sec_name,call_or_put,exercise_price,contract_unit,limit_month,exercise_date")

#转成pandas dataframe
option50ETF = pd.DataFrame(option50ETF_data.Data,index = option50ETF_data.Fields).T

