#coding:utf-8
'''字符编码更正，python默认是acii模式，没有支持utf8'''

#量化交易之路  P30

import six
from abc import ABCMeta,abstractmethod

class TradeStrategyBase(six.with_metaclass(ABCMeta,object)):
    @abstractmethod
    def buy_strategy(self,*args,**kwargs):
        pass
    @abstractmethod
    def sell_strategy(self,*args,**kwargs):
        pass

class TradeStrategy1(TradeStrategyBase):
    s_keep_stock_threshold = 20
    def __init__(self):
        self.keep_stock_day = 0
        self.__buy_change_threshold = 0.07
    def buy_strategy(self,trade_ind,trade_day,trade_days):
        if self.keep_stock_day == 0 and trade_day.change > self.__buy_change_threshold:
            self.keep_stock_day = 1
        elif self.keep_stock_day > 0:
            self.keep_stock_day += 1
    def sell_strategy(self,trade_ind,trade_day,trade_days):
        if self.keep_stock_day >= TradeStrategy1.s_keep_stock_threshold:
            self.keep_stock_day = 0
    @property
    def buy_change_threshold(self):
        return self.__buy_change_threshold
    @buy_change_threshold.setter
    def buy_change_threshold(self,buy_change_threshold):
        if not isinstance(buy_change_threshold,float):
            raise TypeError('buy_change_threshold must be float!')
        self.__buy_change_threshold = round(buy_change_threshold,2)

class TradeLoopBack(object):
    def __init__(self,trade_days,trade_strategy):
        self.trade_days = trade_days
        self.trade_strategy = trade_strategy
        self.profit_array = []
    def execute_trade(self):
        for ind,day in enumerate(self.trade_days):
            if self.trade_strategy.keep_stock_day > 0:
                self.profit_array.append(day.change)
            if hasattr(self.trade_strategy,'buy_strategy'):
                self.trade_strategy.buy_strategy(ind,day,self.trade_days)
            if hasattr(self.trade_strategy,'sell_strategy'):
                self.trade_strategy.sell_strategy(ind,day,self.trade_days)
class TradeStrategy2(TradeStrategyBase):
    s_keep_stock_threshold = 10
    s_buy_change_threshold = -0.10
    def __init__(self):
        self.keep_stock_day = 0
    def buy_strategy(self,trade_ind,trade_day,trade_days):
        if self.keep_stock_day == 0 and trade_ind >=1:
            today_down = trade_day.change<0
            yesterday_down = trade_days[trade_ind - 1].change <0
            down_rate = trade_day.change + trade_days[trade_ind-1].change
            if today_down and yesterday_down and down_rate < TradeStrategy2.s_buy_change_threshold:
                self.keep_stock_day += 1
            elif self.keep_stock_day > 0:
                self.keep_stock_day += 1
    def sell_strategy(self,trade_ind,trade_day,trade_days):
        if self.keep_stock_day >= TradeStrategy2.s_keep_stock_threshold:
            self.keep_stock_day = 0
    @classmethod
    def set_keep_stock_threshold(cls,keep_stock_threshold):
        cls.s_keep_stock_threshold = keep_stock_threshold
    @staticmethod
    def set_buy_change_threshold(buy_change_threshold):
        TradeStrategy2.s_buy_change_threshold = buy_change_threshold
def calc(keep_stock_threshold,buy_change_threshold):
    trade_strategy2 = TradeStrategy2()
    TradeStrategy2.set_keep_stock_threshold(keep_stock_threshold)
    TradeStrategy2.set_buy_change_threshold(buy_change_threshold)
    trade_loop_back = TradeLoopBack(trade_days,trade_strategy2)
    trade_loop_back.execute_trade()

    profit = 0.0 if len(trade_loop_back.profit_array) = 0 else \
            reduce(lambda a,b: a+b, trade_loop_back.profit_array)

    return profit










