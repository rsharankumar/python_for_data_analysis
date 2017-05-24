# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:55:29 2017

@author: skumarravindran
"""

from pandas import Series, DataFrame
import pandas as pd
from pandas_datareader import data, wb
import pandas_datareader.data as web

obj = Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print("printing index:", obj.index)
obj[2] = 6
print(obj[2])


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]} 

frame = DataFrame(data)
print(frame)
new_frame = frame.sort_index(axis = 1)
new_frame = frame.sort_index(by = 'pop')
print(new_frame)

obj = Series([7, -5, 7, 4, 2, 0, 4])
print(obj)

print(obj.rank(ascending = False))

frame.describe()

#all_data = {} 
#for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:    
#    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

#price = DataFrame({tic: data['Adj Close']                   
#    for tic, data in all_data.iteritems()}) 

#volume = DataFrame({tic: data['Volume']                    
#    for tic, data in all_data.iteritems()})
    
stock_data = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/Sharan Coding/sample.csv', header=0)

pd.DataFrame.corr(stock_data)

stock_data['AAPL'] = stock_data['AAPL'].replace('NA', 0)