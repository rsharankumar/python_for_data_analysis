# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:58:14 2017

@author: skumarravindran
"""

import numpy as np
from numpy.random import randn

data1 = [6, 7.5, 8, 0, 1]
data_array = np.array(data1)
data_array = data_array * 10
data_array.dtype
new_data_array = data_array.astype(np.int64)
arr1 = new_data_array *new_data_array


arr2 = np.arange(10)
arr2[5:7] = 12
print(arr2)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

names == 'Bob'

arr3 = np.empty((8, 4))

for i in range(8):   
    arr3[i] = i

arr3 = arr3.astype(np.int64)


print(arr3[[4, 3, 1, -1]])

print(np.dot(arr3.T, arr3))

print(randn(8))
print(arr3.mean())



# random walks

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks