#coding:utf-8
'''字符编码更正，python默认是acii模式，没有支持utf8'''

import pandas as pd
from pandas import DataFrame,Series
import numpy as np

'''
df = DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':np.random.randn(5),
                'data2':np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])

means = df['data1'].groupby([df['key1'],df['key2']]).mean()
'''
'''
close_px = pd.read_csv('D:\Programs\Python\Data\pydata-book-master\ch09\stock_px.csv',parse_dates=True,index_col=0)

rets = close_px.pct_change().dropna()

spx_corr = lambda x:x.corrwith(x['SPX'])

by_year = rets.groupby(lambda x:x.year)
'''

fec = pd.read_csv('D:\Programs\Python\Data\pydata-book-master\ch09\P00000001-ALL.csv')