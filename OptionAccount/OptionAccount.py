# coding: utf-8
import pandas as pd
from pandas import Series, DataFrame
import xlrd
from datetime import datetime
from WindPy import w

#% matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import os

# *****处理‘期权做市财务记录’Excel Begin*****#

data_path = r'E:\Programs\Python\PythonProgramming\PythonProgramming\Jupyter Notebook\Data\期权做市财务记录Data.xlsx'
book = xlrd.open_workbook(data_path.decode('utf8'))  # 需要将中文进行转换

date_series = []  # 日期序列，为每个sheet的名字读取
for sheet in book.sheets():
    value = str(sheet.name)
    time = datetime.strptime(value, '%Y%m%d').strftime('%Y-%m-%d')  # 转换日期成特定格式
    date_series.append(time)

# 初始化存储数据表格
data_list = ['InitialCashETF', 'InitialCashOption', 'InitialCashFuture', 'InitialComCashFuture' ,'CashETF',\
             'AssetETF', 'TotalAssetETF' , 'MarginOption', 'CashOption', 'MarginFuture', 'CashFuture',\
             'MarginComFuture', 'CashComFuture', 'TotalRepo', 'TotalExchangeFees', 'TotalInvestmentCash', \
             'TotalCash', 'PnLOrcTheory','PnLOrcMarket', 'PnLMarketSettle', 'PnLMarketClose']
OptionAccount = DataFrame(columns=data_list, index=date_series)
for sheet in book.sheets():
    value = str(sheet.name)
    time = datetime.strptime(value, '%Y%m%d').strftime('%Y-%m-%d')  # 转换日期成特定格式

    rowNum = sheet.nrows
    colNum = sheet.ncols

    for rowTemp in range(rowNum - 1):
        # 读取现货账户数据
        if sheet.cell(rowTemp, 0).value == u'初始资金':
            OptionAccount.ix[time]['InitialCashETF'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'可用金额':
            OptionAccount.ix[time]['CashETF'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'ETF市值':
            OptionAccount.ix[time]['AssetETF'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'总资产':
            OptionAccount.ix[time]['TotalAssetETF'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'总回购利息':
            OptionAccount.ix[time]['TotalRepo'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'交易费用总额':
            OptionAccount.ix[time]['TotalExchangeFees'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'投入本金总额':
            OptionAccount.ix[time]['TotalCash'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'使用资金总额':
            OptionAccount.ix[time]['TotalInvestmentCash'] = sheet.cell(rowTemp, 1).value

        # 读取商品账户数据
        if sheet.cell(rowTemp, 0).value == u'商品初始资金':
            OptionAccount.ix[time]['InitialComCashFuture'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'商品当前账户余额':
            OptionAccount.ix[time]['CashComFuture'] = sheet.cell(rowTemp, 1).value
        if sheet.cell(rowTemp, 0).value == u'商品保证金':
            OptionAccount.ix[time]['MarginComFuture'] = sheet.cell(rowTemp, 1).value


        # 读取期权账户数据
        if colNum > 3 and sheet.cell(rowTemp, 3).value == u'初始资金':
            OptionAccount.ix[time]['InitialCashOption'] = sheet.cell(rowTemp, 4).value
        if colNum > 3 and sheet.cell(rowTemp, 3).value == u'可用金额':
            OptionAccount.ix[time]['CashOption'] = sheet.cell(rowTemp, 4).value
        if colNum > 3 and sheet.cell(rowTemp, 3).value == u'保证金':
            OptionAccount.ix[time]['MarginOption'] = sheet.cell(rowTemp, 4).value
            # 读取期货账户数据
        if colNum > 6 and sheet.cell(rowTemp, 6).value == u'初始资金':
            OptionAccount.ix[time]['InitialCashFuture'] = sheet.cell(rowTemp, 8).value
        if colNum > 6 and sheet.cell(rowTemp, 6).value == u'当前账户余额':
            OptionAccount.ix[time]['CashFuture'] = sheet.cell(rowTemp, 8).value
        if colNum > 6 and sheet.cell(rowTemp, 6).value == u'保证金':
            OptionAccount.ix[time]['MarginFuture'] = sheet.cell(rowTemp, 8).value

            # 读取Orc数据
        if colNum > 3 and sheet.cell(rowTemp, 3).value == u'理论盈亏':
            OptionAccount.ix[time]['PnLOrcTheory'] = sheet.cell(rowTemp, 4).value
        if colNum > 3 and sheet.cell(rowTemp, 3).value == u'盯市盈亏':
            OptionAccount.ix[time]['PnLOrcMarket'] = sheet.cell(rowTemp, 4).value

OptionAccount = OptionAccount.reindex(index=OptionAccount.index[::-1])  # 按照时间轴进行重排序，从远到近

OptionAccount = OptionAccount.convert_objects(convert_numeric=True)  # 将DataFrame内容转换成

# 由于期权做市财务记录的是前一日收盘情况，因此需要对OptionAccount日期进行进行移位处理

new_dateseries = Series(['2016-06-27'])
new_dateseries = new_dateseries.append(Series(OptionAccount.index)[:-1])
OptionAccount = OptionAccount.set_index(new_dateseries)

# *****处理‘期权做市财务记录’Excel END*****#

'''
#*****数据画图 Begin*****#
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
spx = OptionAccount['PnLOrcTheory']
spx = spx.convert_objects(convert_numeric=True)#转换成数字，否则会出错
#spx = spx.fillna(0)
spx.plot(ax=ax,style='k-')
ax.set_title('Option Market Making PnL')
plt.show()
#*****数据画图 END*****#
'''

# *****计算PnL Begin*****#
w.start()  # 启用万德

position_path = r'E:\Programs\Python\PythonProgramming\PythonProgramming\Jupyter Notebook\Data\OptionPosition'
for pos_date in date_series:
    print pos_date, ' '
    file_date = datetime.strptime(pos_date, '%Y-%m-%d').strftime('%Y%m%d')
    filename = position_path + '/' + file_date + "-close" + ".xls"
    bench_startdate = '2017-07-10'
    bench_endate = '2017-07-12'
    holidays = ['2017-01-26','2017-04-03','2017-04-04','2017-05-01']
    if os.path.exists(filename) and pos_date>bench_startdate and pos_date<bench_endate and \
            pos_date not in holidays:  # 判断position excel文件是否存在,如果存在则调用;同时需满足日期的要求,1月26日无数据，剔除
    #if os.path.exists(filename):
        bookposition = pd.read_excel(filename)
        # 获取计算初始数据
        # Initial Cash
        InitialCashETF = OptionAccount.ix[pos_date]['InitialCashETF']
        InitialCashOption = OptionAccount.ix[pos_date]['InitialCashOption']
        InitialCashFuture = OptionAccount.ix[pos_date]['InitialCashFuture']
        InitialComCashFuture = OptionAccount.ix[pos_date]['InitialComCashFuture']

        # Change Parameters
        TotalAssetETF = OptionAccount.ix[pos_date]['TotalAssetETF']
        MarginOption = OptionAccount.ix[pos_date]['MarginOption']
        CashOption = OptionAccount.ix[pos_date]['CashOption']
        MarginFuture = OptionAccount.ix[pos_date]['MarginFuture']
        CashFuture = OptionAccount.ix[pos_date]['CashFuture']
        MarginComFuture = OptionAccount.ix[pos_date]['MarginComFuture']
        CashComFuture = OptionAccount.ix[pos_date]['CashComFuture']

        # ETF
        PnLETF = 0.0
        PnLETF = TotalAssetETF - InitialCashETF

        # Future
        PnLFuture = 0.0
        PnLFuture = MarginFuture + CashFuture - InitialCashFuture

        # Comodity
        PnlComodity = 0.0
        PnlComodity = MarginComFuture + CashComFuture - InitialComCashFuture

        # Option
        TotalAssetOption = 0.0
        TotalAssetOption = MarginOption + CashOption

        LongPositionCloseValue = 0.0  # 多头收盘价市值
        LongPositionSettleValue = 0.0  # 多头结算价市值
        ShortPositionCloseValue = 0.0  # 空头收盘价市值
        ShortPositionSettleValue = 0.0  # 空头收盘价市值

        # 利用万德获取收盘价、结算价等
        bookposition['settle_price'] = pd.Series(0.0, index=bookposition.index)
        bookposition['close_price'] = pd.Series(0.0, index=bookposition.index)
        bookposition['Position'] = pd.Series(0.0, index=bookposition.index)

        i = 0
        for code in bookposition[u'合约代码']:
            print i
            if code != code:
                i = i + 1
            else:
                if bookposition.ix[i, u'保证金占用'] != 0.0:
                    bookposition.ix[i, 'Position'] = - bookposition.ix[i, u'当日持仓数量']
                elif bookposition.ix[i, u'保证金占用'] == 0.0:
                    bookposition.ix[i, 'Position'] = bookposition.ix[i, u'当日持仓数量']
                name = '%d' % code + '.SH'
                begin_date = pos_date
                end_date = pos_date
                contract_size = w.wsd(name, "exe_ratio", begin_date, end_date, "").Data[0][0]  # 确定合约乘数
                bookposition.ix[i, 'settle_price'] = w.wsd(name, "settle", begin_date, end_date, "").Data[0][0]
                bookposition.ix[i, 'close_price'] = w.wsd(name, "close", begin_date, end_date, "").Data[0][0]
                if bookposition.ix[i, 'settle_price'] != bookposition.ix[i, 'settle_price']:
                    bookposition.ix[i, 'settle_price'] = bookposition.ix[i, 'close_price']
                elif bookposition.ix[i, 'close_price'] != bookposition.ix[i, 'close_price']:
                    bookposition.ix[i, 'close_price'] = bookposition.ix[i, 'settle_price']
                if bookposition.ix[i, 'Position'] > 0.:
                    LongPositionCloseValue = LongPositionCloseValue + bookposition.ix[i, 'Position'] * bookposition.ix[
                        i, 'close_price'] * contract_size
                    LongPositionSettleValue = LongPositionSettleValue + bookposition.ix[i, 'Position'] * \
                                                                        bookposition.ix[
                                                                            i, 'settle_price'] * contract_size
                elif bookposition.ix[i, 'Position'] < 0.:
                    ShortPositionCloseValue = ShortPositionCloseValue + bookposition.ix[i, 'Position'] * \
                                                                        bookposition.ix[
                                                                            i, 'close_price'] * contract_size
                    ShortPositionSettleValue = ShortPositionSettleValue + bookposition.ix[i, 'Position'] * \
                                                                          bookposition.ix[
                                                                              i, 'settle_price'] * contract_size
                i = i + 1
        PnLCloseOption = 0.0
        PnLSettleOption = 0.0

        PnLCloseOption = TotalAssetOption + LongPositionCloseValue + ShortPositionCloseValue - InitialCashOption
        PnLSettleOption = TotalAssetOption + LongPositionSettleValue + ShortPositionSettleValue - InitialCashOption

        # 汇总
        OptionAccount.ix[pos_date]['PnLMarketSettle'] = PnLSettleOption + PnLETF + PnLFuture + PnlComodity
        OptionAccount.ix[pos_date]['PnLMarketClose'] = PnLCloseOption + PnLETF + PnLFuture + PnlComodity


        # output
        PnL_path = 'E:\Programs\Python\PythonProgramming\PythonProgramming\Jupyter Notebook\Data\OptionPnL'
        PnL_filename = PnL_path + '/' + pos_date + ' PnL' + '.txt'
        result = open(PnL_filename, 'w')
        result.write('***********' + pos_date + '  PnL**************' + '\n\n')

        result.write('Basic Information:' + '\n')
        result.write('InitialCashETF: ')
        result.write(str(InitialCashETF))
        result.write('\n')
        result.write('InitialCashOption: ')
        result.write(str(InitialCashOption))
        result.write('\n')
        result.write('InitialCashFuture: ')
        result.write(str(InitialCashFuture))
        result.write('\n')
        result.write('TotalAssetETF: ')
        result.write(str(TotalAssetETF))
        result.write('\n')
        result.write('MarginOption: ')
        result.write(str(MarginOption))
        result.write('\n')
        result.write('CashOption: ')
        result.write(str(CashOption))
        result.write('\n')
        result.write('MarginFuture: ')
        result.write(str(MarginFuture))
        result.write('\n')
        result.write('CashFuture: ')
        result.write(str(CashFuture))
        result.write('\n\n')

        result.write('Each PnL:' + '\n')
        result.write('Option Market Making PnL:' + '\n')
        result.write('PnLSettleOption: ')
        result.write(str(PnLSettleOption))
        result.write('\n')
        result.write('PnLETF: ')
        result.write(str(PnLETF))
        result.write('\n')
        result.write('PnLFuture: ')
        result.write(str(PnLFuture))
        result.write('\n')
        result.write('\n\n')

        result.write('Option Market Making PnL:' + '\n')
        result.write('PnLMarketSettle: ')
        result.write(str(OptionAccount.ix[pos_date]['PnLMarketSettle']))
        result.write('\n')
        result.write('PnLMarketClose: ')
        result.write(str(OptionAccount.ix[pos_date]['PnLMarketClose']))
        result.write('\n')
        result.write('PnLOrcTheory: ')
        result.write(str(OptionAccount.ix[pos_date]['PnLOrcTheory']))
        result.write('\n')
        result.close()


        print 'PnLMarketSettle: ', OptionAccount.ix[pos_date]['PnLMarketSettle']
        print 'PnLMarketClose: ', OptionAccount.ix[pos_date]['PnLMarketClose']
        print 'PnLOrcTheory: ', OptionAccount.ix[pos_date]['PnLOrcTheory']
        
        print '\n'

        OptionAccount.to_csv(\
            'E:\Programs\Python\PythonProgramming\PythonProgramming\Jupyter Notebook\Data\OptionAccount.csv')
        # *****计算PnL END*****#