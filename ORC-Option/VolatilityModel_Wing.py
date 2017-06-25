# coding: utf-8
# Volatility Wing Model


import numpy

class wingmodelPara(object):
    def __init__(self):
        self.Days = 0. #Days remaining until expiry
        self.Fatm = 0. #ATM foward
        self.Fref = 0.
        self.Volref = 0.
        self.Sref = 0.
        self.Volcur = 0.
        


