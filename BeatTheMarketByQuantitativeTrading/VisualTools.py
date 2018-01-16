# -*- coding:utf-8 -*-
#Python 3.5.0

#第五章 量化工具-可视化 中代码测试，将其中Tesla 换成50ETF，从万德中获得数据


from WindPy import w
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import datetime
w.start();

# 取数据的命令如何写可以用命令生成器来辅助完成

wsd_data=w.wsd("510050.SH", "open,high,low,close,volume", "2017-01-01", "2017-12-31", "Fill=Previous")

fm=pd.DataFrame(wsd_data.Data,index=wsd_data.Fields,columns=wsd_data.Times)
fm = fm.T

#5.1.1  plot_demo
#**********************

def plot_demo(axs = None,just_series = False):
    drawer = plt if axs is None else axs
    drawer.plot(fm['CLOSE'],c='r')
    if not just_series:
        drawer.plot(fm['CLOSE'].index,fm['CLOSE'] + 1, c='g')
        drawer.plot(fm['CLOSE'].index.tolist(), fm['CLOSE'] + 2, c='b')
    plt.xlabel('time')
    plt.ylabel('close')
    plt.title('50ETF Close')
    plt.grid(True)
    plt.show()
#plot_demo()
#**********************

#5.1.3  K线图
#**********************
__colorup__ = "red"
__colordown__ = "green"
fm_part = fm[:60]
fig,ax =plt.subplots(figsize=(14,7))
quotes = []
for index, (d,o,c,h,l) in enumerate(\
        zip(fm_part.index,fm_part['OPEN'],fm_part['CLOSE'],fm_part['HIGH'],fm_part['LOW'])):
    d = mpf.date2num(d)
    val = (d,o,c,h,l)
    quotes.append(val)
mpf.candlestick_ochl(ax,quotes,width=0.6,colorup=__colorup__,colordown=__colordown__)
ax.autoscale_view()
ax.xaxis_date()
plt.show()


#**********************