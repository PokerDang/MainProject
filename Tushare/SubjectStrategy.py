#coding:utf-8
'''字符编码更正，python默认是acii模式，没有支持utf8'''

import tushare as ts
import pandas as pd
from pandas import Series,DataFrame




data = ts.get_concept_classified()
concept_data = DataFrame(data)
print (concept_data)