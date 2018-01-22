# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Orc中的函数

#ATM forward
def F_Atm(spot,r,T):
    return spot*np.exp(r*T)

#Synthetic forward
def F_Syn(Fatm,Fref,SSR):
    return np.power(Fatm,SSR/100)*np.power(Fref,1-SSR/100)

#log-moneyness transformation
def TranLog(X,F):
    return np.log(X/F)

#current volatility
def VolCur(vref,VCR,SSR,Fatm,Fref):
    return vref - VCR*SSR*(Fatm-Fref)/Fref

#current slope

def SlopeCur(sref,SCR,SSR,Fatm,Fref):
    return sref - SCR*SSR*(Fatm-Fref)/Fref

#volatility Wing model

def VolModel_Wing(K,spot,r,T,Fref,vref,sref,pc,vc,cc,xdc,xuc,VCR,SCR,SSR,dsm,usm,kdown=0.,kup=0.):

    Fatm = F_Atm(spot,r,T)
    Fsyn = F_Syn(Fatm,Fref,SSR)
    x = TranLog(K,Fsyn)
    volcur = VolCur(vref,VCR,SSR,Fatm,Fref)
    slopecur = SlopeCur(sref,SCR,SSR,Fatm,Fref)

#Total Six Range
#down constant range
    if x < xdc*(1+dsm):
        x1 = xdc
        x0 = x1*(1+dsm)
        return kdown*(x-x0)+volcur + slopecur*x0 + pc*np.square(x0)

#down smoothing range
    elif x>=xdc*(1+dsm) and x<xdc:
        x1 = xdc
        x0 = x1 * (1 + dsm)
        c = (2*x1*pc+slopecur-kdown)/(2*(x1-x0))
        b = kdown - (2*x1*pc+slopecur-kdown)/(x1-x0)*x0
        a = volcur + slopecur*x1 + pc*np.square(x1) - b*x1-c*x1
        return a+b*x+c*np.square(x)
#put wing
    elif x>= xdc and x<0:
        return volcur + slopecur*x + pc*np.square(x)
#call wing
    elif x>=0 and x<xuc:
        return volcur + slopecur*x + cc*np.square(x)
#up smoothing range
    elif x >= xuc and x < xuc(1+usm):
        x2 = xuc
        x3 = xuc * (1 + usm)
        c = (2*x2*cc+slopecur-kup)/(2*(x2-x3))
        b = kup - (2*x2*cc+slopecur-kup)/(x2-x3)*x3
        a = volcur + slopecur*x2 + cc*np.square(x2) - b*x2-c*x2
        return  a+b*x+c*np.square(x)
#up constant range
    else:
        x2 = xuc
        x3 = xuc*(1+usm)
        return kup*(x-x3) + volcur + slopecur*x3 + cc*np.square(x3)

