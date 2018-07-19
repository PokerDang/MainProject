# encoding: utf-8

from WindPy import *
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt

w.start()

dat= w.wsd("002739.SZ", "open,high,low,close,volume,amt", "2016-05-17",
           "2016-06-16", "TradingCalendar=SZSE;Fill=Previous")

fm=pd.DataFrame(dat.Data,index=dat.Fields,columns=dat.Times)#pandas timeseries type
fm=fm.T
 
print fm

