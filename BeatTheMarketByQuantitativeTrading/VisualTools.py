# -*- coding:utf-8 -*-
#Python 3.5.0

#第五章 量化工具-可视化 中代码测试，将其中Tesla 换成50ETF，从万德中获得数据


from WindPy import w
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np
import seaborn as sns
from datetime import datetime,date
w.start();

# 取数据的命令如何写可以用命令生成器来辅助完成

sh50etf_data=w.wsd("510050.SH", "open,high,low,close,volume", "2013-01-01", "2017-12-31", "Fill=Previous")
sh300etf_data= w.wsd("510300.SH", "open,high,low,close,volume", "2013-01-01", "2017-12-31", "Fill=Previous")

sh50etf_df=pd.DataFrame(sh50etf_data.Data,index=sh50etf_data.Fields,columns=sh50etf_data.Times)
sh50etf_df = sh50etf_df.T
sh300etf_df=pd.DataFrame(sh300etf_data.Data,index=sh300etf_data.Fields,columns=sh300etf_data.Times)
sh300etf_df = sh300etf_df.T
#添加每日上涨下跌，neiChangeratio
sh50etf_df['netChangeRatio'] = sh50etf_df['CLOSE'].pct_change()
sh50etf_df['netChangeRatio'].ix[0] = 0
sh300etf_df['netChangeRatio'] = sh300etf_df['CLOSE'].pct_change()
sh300etf_df['netChangeRatio'].ix[0] = 0



#5.1.1  plot_demo
#**********************

def plot_demo(axs = None,just_series = False):
    drawer = plt if axs is None else axs
    drawer.plot(sh50etf_df['CLOSE'],c='r')
    if not just_series:
        drawer.plot(sh50etf_df['CLOSE'].index,sh50etf_df['CLOSE'] + 1, c='g')
        drawer.plot(sh50etf_df['CLOSE'].index.tolist(), sh50etf_df['CLOSE'] + 2, c='b')
    plt.xlabel('time')
    plt.ylabel('close')
    plt.title('50ETF Close')
    plt.grid(True)
    #plt.show()
#**********************
'''
#5.1.3  K线图
#**********************
__colorup__ = "red"
__colordown__ = "green"
sh50etf_df_part = sh50etf_df[:60]
fig,ax =plt.subplots(figsize=(14,7))
quotes = []
for index, (d,o,c,h,l) in enumerate(\
        zip(sh50etf_df_part.index,sh50etf_df_part['OPEN'],sh50etf_df_part['CLOSE'],sh50etf_df_part['HIGH'],sh50etf_df_part['LOW'])):
    d = mpf.date2num(d)
    val = (d,o,c,h,l)
    quotes.append(val)
mpf.candlestick_ochl(ax,quotes,width=0.6,colorup=__colorup__,colordown=__colordown__)
ax.autoscale_view()
ax.xaxis_date()
#plt.show()
#**********************

sh50etf_df_copy = sh50etf_df.copy()

sh50etf_df_copy['RETURN'] = np.log(sh50etf_df['CLOSE']/sh50etf_df['CLOSE'].shift(1))
sh50etf_df_copy['MOV_STD'] = pd.rolling_std(sh50etf_df_copy['RETURN'],window=20,center=False)*np.sqrt(20)
sh50etf_df_copy['STD_EWM'] = pd.ewmstd(sh50etf_df_copy['RETURN'],span=20,min_periods=20,adjust=True)*np.sqrt(20)
sh50etf_df_copy[['CLOSE','MOV_STD','STD_EWM','RETURN']].plot(subplots=True,grid=True)
plt.show()

'''

'''
#5.4  Seaborn
#**********************
sns.distplot(sh50etf_df['netChangeRatio'],bins=80)
plt.show()

#**********************
'''


#5.5  可视化量化策略的交易区间
#**********************

def plot_trade(buy_date,sell_date):
    t=0
    for date in sh50etf_df.index:
        if buy_date == str(date):
            start = t
        elif sell_date == str(date):
            end = t+2
        else:
            t = t+1
    plot_demo(just_series=True)
    plt.fill_between(sh50etf_df.index,0,sh50etf_df['CLOSE'],color='blue',alpha=.08)
    if sh50etf_df['CLOSE'][end] < sh50etf_df['CLOSE'][start]:
        plt.fill_between(sh50etf_df.index[start:end],0,sh50etf_df['CLOSE'][start:end],color='green',alpha=.38)
        is_win = False
    else:
        plt.fill_between(sh50etf_df.index[start:end], 0, sh50etf_df['CLOSE'][start:end], color='red', alpha=.38)
        is_win = True
    plt.ylim(np.min(sh50etf_df['CLOSE'])-1,np.max(sh50etf_df['CLOSE'])+1)
    plt.legend(['CLOSE'],loc='best')
    return is_win
#plot_trade('2014-07-28','2014-09-05')
#**********************


#5.5  标注策略卖出原因
#**********************

def plot_trade_with_annotate(buy_date,sell_date):
    is_win = plot_trade(buy_date,sell_date)
    plt.annotate('sell for stop win' if is_win else 'sell for stop loss',\
                 xy=(sell_date,sh50etf_df['CLOSE'].asof(datetime.strptime(sell_date, "%Y-%m-%d").date())),\
                 arrowprops=dict(facecolor='yellow'),horizontalalignment='left',\
                 verticalalignment='top')
#plot_trade_with_annotate('2014-07-28','2014-09-05')
#plot_trade_with_annotate('2015-01-28','2015-03-11')
#plot_trade_with_annotate('2015-04-10','2015-07-10')
#plot_trade_with_annotate('2015-10-02','2015-10-14')
#plot_trade_with_annotate('2016-02-10','2016-04-11')
#plt.show()

#**********************



#5.6  两只股票观察
#**********************
def plot_two_stock(stock1,stock2,axs=None):
    drawer = plt if axs is None else axs
    drawer.plot(stock1,c='r')
    drawer.plot(stock2,c='g')
    drawer.grid(True)
    drawer.legend(['510050','510300'],loc='best')
#plot_two_stock(sh50etf_df['CLOSE'],sh300etf_df['CLOSE'])
#plt.title('510050 and 510300')
#plt.xlabel('time')
#plt.ylabel('Close')
#plt.show()

#**********************


'''
#5.6.2  标准化两只股票
#**********************
def two_mean_list(one,two,type_look='look_max'):
    one_mean = one.mean()
    two_mean = two.mean()
    if type_look == 'look_max':
        one,two = (one, one_mean/two_mean*two) if one_mean > two_mean else (one*two_mean/one_mean,two)
    elif type_look == 'look_min':
        one, two = (one * two_mean/one_mean, two) if one_mean > two_mean else (one, two * one_mean / two_mean)
    return one,two
def regular_std(group):
    return (group - group.mean()) /group.std()
def regular_mm(group):
    return (group - group.min())/(group.max() - group.min())
_, axs=plt.subplots(nrows=2,ncols=2,figsize=(14,10))

drawer = axs[0][0]
plot_two_stock(regular_std(sh50etf_df['CLOSE']),regular_std(sh300etf_df['CLOSE']),drawer)
drawer.set_title('(group - group.mean()) /  group.std()')


drawer = axs[0][1]
plot_two_stock(regular_mm(sh50etf_df['CLOSE']),regular_mm(sh300etf_df['CLOSE']),drawer)
drawer.set_title('(group - group.min()) /  group.std()')

drawer = axs[1][0]
one,two = two_mean_list(sh50etf_df['CLOSE'],sh300etf_df['CLOSE'],type_look='look_max')
plot_two_stock(one,two,drawer)
drawer.set_title('two_mean_list type=look_max')

drawer = axs[1][1]
one,two = two_mean_list(sh50etf_df['CLOSE'],sh300etf_df['CLOSE'],type_look='look_min')
plot_two_stock(one,two,drawer)
drawer.set_title('two_mean_list type=look_min')

_,ax1 = plt.subplots()
ax1.plot(sh50etf_df['CLOSE'],c='r',label='510050')
ax1.legend(loc=2)
ax1.grid(False)

ax2 = ax1.twinx()
ax2.plot(sh300etf_df['CLOSE'],c='g',label='510300')
ax2.legend(loc=1)

plt.show()

#**********************
'''

'''
#5.7  黄金分割线
#**********************
from collections import namedtuple
from scipy import stats
sp382_stats = stats.scoreatpercentile(sh50etf_df['CLOSE'],38.2)
sp618_stats = stats.scoreatpercentile(sh50etf_df['CLOSE'],61.8)

cs_max = sh50etf_df['CLOSE'].max()
cs_min = sh50etf_df['CLOSE'].min()
sp382 = (cs_max - cs_min)*0.382 + cs_min
sp618 = (cs_max - cs_min)*0.618 + cs_max

def plot_golden():
    above618 = np.maximum(sp618,sp618_stats)
    below618 = np.minimum(sp618,sp618_stats)
    above382 = np.maximum(sp382, sp382_stats)
    below382 = np.minimum(sp382, sp382_stats)

    plt.plot(sh50etf_df['CLOSE'])
    plt.axhline(sp382,c='r')
    plt.axhline(sp382_stats,c='m')
    plt.axhline(sp618,c='g')
    plt.axhline(sp618_stats,c='k')
    plt.fill_between(sh50etf_df.index,above618,below618,alpha=0.5,color="r")
    plt.fill_between(sh50etf_df.index, above382, below382, alpha=0.5, color="g")
    return namedtuple('golden',['above618','below618','above382','below382'])(above618,below618,above382,below382)
golden = plot_golden()
plt.legend(['close','sp382','sp382_stats','sp618','sp618_stats'],loc='best')
plt.show()
#**********************
'''

#5.8  技术指标的可视化
#**********************
import talib
k1_index = sh50etf_df.index

dif,dea,bar = talib.MACD(sh50etf_df['CLOSE'].values,fastperiod=12,slowperiod=26,signalperiod=9)
plt.plot(k1_index,dif,label='macd dif')
plt.plot(k1_index,dea,label='signal dea')
bar_red = np.where(bar>0,bar,0)
bar_green = np.where(bar < 0, bar,0)
plt.bar(k1_index,bar_red,facecolor='red',label='hist bar')
plt.bar(k1_index,bar_green,facecolor='green',label='hist bar')
plt.legend(loc='best')
plt.show()

#**********************