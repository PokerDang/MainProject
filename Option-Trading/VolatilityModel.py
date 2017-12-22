# coding: utf-8
# Volatility Model

import numpy




#***************Option Setting Begin********************#
def InitialOptionParameters(feedcode='',type='',T='',K=0,S=0,r=0,vol=0,offsets=0):
    option = {}
    option['feedcode'] = feedcode
    option['offsets'] = offsets
    option['vol'] = vol
    option['r'] = r

    return option
#***************Option Setting END*********************#




#***************Option Greeks Begin********************#

def CalcGreeks(Option):
    Greeks = {}
    Greeks['delta'] = 0
    Greeks['skewdelta'] = 0
    Greeks['cashdelta'] = 0
    Greeks['skewcashdelta'] = 0
    Greeks['cashgammma'] = 0
    Greeks['skewcashgammma'] = 0
    Greeks['skewcashgammma1per'] = 0
    Greeks['vega'] = 0
    Greeks['skewvega'] = 0
    Greeks['theta'] = 0
    Greeks['voltheta'] = 0

    return Greeks




#***************Option Greeks Begin********************#






#***************Wing Model Begin*******************#
def InitialWingModelParameters(Days,F_atm,F_ref,Vol_ref,Slope_ref,Vol_cur,Slope_cur,Call_cur,Put_cur,\
                        Down_cut,Up_cut,VCR,SCR,SSR,Down_sm,Up_sm):
    parameters = {}
    parameters['Days'] =  Days
    parameters['F_atm'] = F_atm
    parameters['F_ref'] = F_ref
    parameters['Vol_ref'] = Vol_ref
    parameters['Slope_ref'] = Slope_ref
    parameters['Vol_cur'] = Vol_cur
    parameters['Slope_cur'] = Slope_cur
    parameters['Call_cur'] = Call_cur
    parameters['Put_cur'] = Put_cur
    parameters['Down_cut'] = Down_cut
    parameters['Up_cut'] = Up_cut
    parameters['VCR'] = VCR
    parameters['SCR'] = SCR
    parameters['SSR'] = SSR
    parameters['Down_sm'] = Down_sm
    parameters['Up_sm'] = Up_sm
    return parameters

def Volatility_Wing(parameters):
    vol = 0
    


    return vol
#************Wing Model END*********************#




def Volatility_CubicStatic(parameters):
    vol = 0
    return vol

def Volatility_CubicDynamic(parameters):
    vol = 0
    return vol

def Volatility_CubicStddev(parameters):
    vol = 0
    return vol


def Volatility_SABR(parameters):
    vol = 0
    return vol
