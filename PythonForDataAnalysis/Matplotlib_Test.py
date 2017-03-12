import pandas as pd
import matplotlib.pyplot as plt

from numpy.random import  randn
from datetime import  datetime

'''
fig = plt.figure()
fig.show()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)



plt.plot(randn(50).cumsum(),'k--')
'''
plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig.show()

data = pd.read_csv('D:\Programs\Python\Data\pydata-book-master\ch08\spx.csv',index_col=0,parse_dates=True)
spx = data['SPX']

spx.plot(ax=ax,style='k-')

crisis_data = [(datetime(2007,10,11),'Peak of bull market'),(datetime(2008,3,12),'Bear Stearns Fails'),
               (datetime(2008,9,15),'Lehman Bankruptcy')]

for date, label in crisis_data:
    ax.annotate(label,xy=(date,spx.asof(date)+50),xytext=(date,spx.asof(date)+200),arrowprops=dict(facecolor='black'),
                horizontalalignment='left',verticalalignment='top')

ax.set_xlim(['1/1/2007','1/1/2011'])
ax.set_ylim([600,1800])
ax.set_title('Important dates in 2008-2009 financial crisis')







