# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pylab
import seaborn as sns
#font.set_size(20)
x = np.linspace(1.0, 13.0, 7)
y = np.sin(x)
pylab.figure(figsize = (12,6))
pylab.scatter(x,y, s = 85, marker='x', color = 'r')
#pylab.title(u'$f(x)$离散点分布', fontproperties = font)
pylab.title(u'$f(x)$离散点分布')