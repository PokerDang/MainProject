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

def VolModel_Wing(K,spot,r,T,Fref,vref,sref,pc,cc,xdc,xuc,VCR,SCR,SSR,dsm,usm):

    Fatm = F_Atm(spot,r,T)
    Fsyn = F_Syn(Fatm,Fref,SSR)
    x = TranLog(K,Fsyn)
    volcur = VolCur(vref,VCR,SSR,Fatm,Fref)
    slopecur = SlopeCur(sref,SCR,SSR,Fatm,Fref)

#Total Six Range
#down constant range
    if x < xdc*(1+dsm):
        vol_x = volcur + xdc*(2+dsm)*slopecur*0.5+(1+dsm)*pc*np.square(xdc)
        return vol_x

#down smoothing range
    elif x>=xdc*(1+dsm) and x<xdc:
        vol_x = volcur -(1+1/dsm)*pc*np.square(xdc)-(slopecur*xdc)/(2*dsm)+\
                (1+1/dsm)*(2*pc*xdc+slopecur)*x - (pc/dsm + slopecur/(2*xdc*dsm))*np.square(x)
        return vol_x
#put wing
    elif x>= xdc and x<0:
        return volcur + slopecur*x + pc*np.square(x)
#call wing
    elif x>=0 and x<xuc:
        return volcur + slopecur*x + cc*np.square(x)
#up smoothing range
    elif x >= xuc and x < xuc(1+usm):
        vol_x = volcur -(1+1/usm)*cc*np.square(xuc)-(slopecur*xuc)/(2*usm)+\
                (1+1/usm)*(2*cc*xuc+slopecur)*x - (cc/usm + slopecur/(2*xuc*usm))*np.square(x)
        return  vol_x
#up constant range
    else:
        vol_x = volcur + xuc*(2+usm)*slopecur*0.5+(1+usm)*cc*np.square(xuc)
        return vol_x


