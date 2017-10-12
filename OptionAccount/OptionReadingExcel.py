# coding: utf-8
import pandas as pd
from pandas import Series, DataFrame
import xlrd
from datetime import datetime



# *****处理‘期权做市财务记录’Excel Begin*****#

#data_path = r'E:\Programs\Python\PythonProgramming\PythonProgramming\Jupyter Notebook\Data\期权做市财务记录Data.xlsx'
data_path = r'E:\东方工作\期权业务\期权每日交易\期权做市财务记录.xlsx'

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
OptionAccount.to_csv('E:\东方工作\期权业务\期权每日交易\OptionAccountExcel.csv')
        # *****计算PnL END*****#