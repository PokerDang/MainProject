# encoding: utf-8


'''
应用简介：
基于Python语言，使用wsq订阅数据，然后存储到硬盘中。

使用介绍：
该案例是演示wsq实时行情订阅的使用，订阅模式主要有两部分组成，一部分是用wsq函数订阅所需要的行情，
另一部分是编写自己的回调函数，用于处理实时推送过来的行情数据
myCallback(indata) 即为本案例所使用的回调函数，回调函数有且只能有一个参数：indata
indata的数据结构如下：
indata.ErrorCode 错误码，如果为0表示运行正常
indata.StateCode 状态字段，使用时无需处理
indata.RequestID 存放对应wsq请求的RequestID
indata.Codes 存放行情对应的code
indata.Fields 存放行情数据对应的指标
indata.Times 存放本地时间，注意这个不是行情对应的时间，要获取行情对应的时间，请订阅rt_time指标
indata.Data 存放行情数据

取消订阅可使用w.cancelRequest(requestID),如果想取消全部订阅，可使用w.cancelRequest(0)

例如:
indata.ErrorCode=0
indata.StateCode=1
indata.RequestID=3
indata.Codes=[IF.CFE]
indata.Fields=[RT_LAST]
indata.Times=[20151123 15:12:40]
indata.Data=[[3623.0]]
'''



import threading
from WindPy import *
w.start();
from datetime import datetime

#define the callback function
def myCallback(indata):
    if indata.ErrorCode!=0:
        print('error code:'+str(indata.ErrorCode)+'\n');
        return();

    global begintime
    lastvalue ="";
    for k in range(0,len(indata.Fields)):
         if(indata.Fields[k] == "RT_LAST"):
            lastvalue = str(indata.Data[k][0]);
    string =  lastvalue +"\n";
    print(string);
    #应该在w.cancelRequest后调用pf.close()
    #pf.close();



exit=False

class feeder(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        w.start()
        w.wsq("RB.SHF","rt_time,rt_last",func=myCallback)
#to subscribe if14.CFE

thread1 =feeder(1,"feder-1")
thread1.start()
while(1):
    if (exit):
        break;