# -*- coding: utf-8 -*-

#Option 类
#参数：
#     type
#     T
#     K
#     S
#     r
#     sigma
#     size
#     feedcode
#
class Option(object):
    def __init__(self,type='',T='',K=0,S=0,r=0,sigma=0,size=0,feedcode=''):
        self.type = type
        self.maturity = T
        self.strike = K
        self.underlying = S
        self.rate = r
        self.vol = sigma
        self.size = size
        self.feedcode = feedcode

    def __str__(self):
        return "Type: %s, Maturity: %s, Strike: %s, Underlying: %s, Rate: %s, Volatility: %s,Contract Size: %s, Feedcode: %s" %\
                (self.type,self.maturity,self.strike,self.underlying,self.rate,self.vol\
                ,self.size,self.feedcode)

class Vol_Surface(object):
    pass

class Orc_Risk(object):
    pass

class Orc_Option(object):
    pass

class Orc_Trading(object):
    pass
'''
def main():
    option = Option('C','2017-03-14',2.5,2.5,0.20,0.3,10000,8003714)
    print option

main()
'''