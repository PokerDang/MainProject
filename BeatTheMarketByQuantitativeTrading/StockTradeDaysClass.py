#coding:utf-8
'''字符编码更正，python默认是acii模式，没有支持utf8'''

#量化交易之路  P26

from collections import namedtuple
from collections import OrderedDict

class StockTradeDays(object):
    def __init__(self,price_array,start_date,date_array=None):
        self.__price_array = price_array
        self.__date_array = price_array
        self.__change_array = self.__init_change()
        self.stock_dict = self._init_stock_dict()

    def __init_change(self):

