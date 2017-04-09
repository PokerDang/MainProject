#coding:utf-8  
import matplotlib
from matplotlib import pyplot
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
from pandas import DataFrame,Series
import  numpy as np
from datetime import  datetime

import sys
def main():
    holidays  = ['2017-01-26','2017-01-27']
    normaldays = ['2017-01-26','2017-01-27','2017-01-28','2017-01-29']
    for days in normaldays:
        if days not in holidays:
            print days

main()