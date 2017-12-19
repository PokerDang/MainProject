# coding: utf-8
# Volatility Wing Model


import numpy

def InitialParameters(Days,F_atm,F_ref,Vol_ref,Slope_ref,Vol_cur,Slope_cur,Call_cur,Put_cur,\
                        Down_cut,Up_cut,VCR,SCR,SSR,Down_sm,Up_sm):
    parameters = {}
    parameters['Days'] =  Days
    parameters['F_atm'] = F_atm
    parameters['F_ref'] = F_ref
    parameters['Vol_ref'] = Vol_ref
    parameters['Slope_ref'] = Slope_ref
    parameters['Vol_cur'] = Vol_cur
    parameters['Slope_cur'] = Slope_cur
    parameters['Call_cur'] = Put_cur
    parameters['Down_cut'] = Down_cut
    parameters['Up_cut'] = Up_cut
    parameters['VCR'] = VCR
    parameters['SCR'] = SCR
    parameters['SSR'] = SSR
    parameters['Down_sm'] = Down_sm
    parameters['Up_sm'] = Up_sm
    return parameters

def Volatility_Wing():

        
def Volatility_CubicStatic():


def Volatility_CubicDynamic():


def Volatility_CubicStddev():

def Volatility_SABR():

