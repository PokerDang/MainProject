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
        price_float_array = [float(price_str) for price_str in self.__price_array]

        pp_array = [(price1,price2) for price1,price2 in zip(price_float_array[:-1],price_float_array[1:])]
        change_array = map(lambda pp:reduce(lambda a,b:round((b-a)/a,3),pp),pp_array)
        change_array.insert(0,0)
        return change_array

    def _init_days(self,start_date,date_array):
        if date_array is None:
            date_array = [str(start_date + ind) for ind in enumerate(self.__price_array)]
        else:
            date_array = [str(date) for date in date_array]
        return date_array

    def _init_stock_dict(self):
        stock_namedtuple = namedtuple('stock',('date','price','change'))
        stock_dict = OrderedDict((date,stock_namedtuple(date,price,change))
                                 for date, price, change in
                                 zip(self.__date_array,self.__price_array,self.__change_array))
        return stock_dict

    def filter_stock(self,want_up=True,want_calc_sum=False):
        filter_func = (lambda day: day.change > 0) if want_up else (lambda day:day.change < 0)
        want_days = filter(filter_func,self.stock_dict.values())
        if not want_calc_sum:
            return want_days
        change_sum = 0.0
        for day in want_days:
            change_sum += day.change
        return change_sum

    def __str__(self):
        return str(self.stock_dict)

    #__repr__ = __str__()

    def __iter__(self):

        for key in self.stock_dict:
            yield self.stock_dict[key]

    def __getitem__(self, ind):
        date_key = self.__date_array[ind]
        return self.stock_dict[date_key]

    def __len__(self):
        return len(self.stock_dict)


def main():
    price_array = '30.14,29.58,26.36,32.56,32.82'.split(',')
    print price_array













