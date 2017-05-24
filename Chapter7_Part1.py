# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:26:15 2017

@author: skumarravindran
"""
import pandas as pd
import numpy as np


df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})

df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})

df12 = pd.merge(df1, df2)

df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})

df4 = DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})

f3df4 = pd.merge(df3, df4, left_on='lkey', right_on='rkey')

pd.merge(df1, df2, how='outer')

arr = np.arange(12).reshape((3, 4))

arr1 = np.concatenate([arr, arr], axis=0)

df1n = pd.concat([df1, df1], axis=0)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)

pd.crosstab(data.Gender, data.Handedness, margins=True)