# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:07:08 2017

@author: skumarravindran
"""

import pandas as pd
import numpy as np

names1880 = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch02/names/yob1880.txt', names=['name', 'sex', 'births'])
names1880

names1880.groupby('sex')['births'].sum()

# 2010 is the last available year right now 
years = range(1880, 2011)
pieces = [] 
columns = ['name', 'sex', 'births']
for year in years:    
    path = 'C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch02/names/yob%d.txt' % year    
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year    
    pieces.append(frame)
    # Concatenate everything into a single DataFrame 
    names = pd.concat(pieces, ignore_index=True)
    


total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

def add_prop(group):    # Integer division floors    
    births = group.births.astype(float)
    group['prop'] = births / births.sum()    
    return group 

names_new = names.groupby(['year', 'sex']).apply(add_prop)


def get_top1000(group):    
    return group.sort_index(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex']) 
top1000 = grouped.apply(get_top1000)

alt_sort = names.groupby(['year', 'sex']).apply(get_top1000)

prop_cumsum = names_new.sort_index(by='prop', ascending=False).prop.cumsum()

get_last_letter = lambda x: x[-1] 

names['last_char'] = names.name.map(get_last_letter) 

names.groupby(['year', 'sex'])['births'].sum()

table = names.pivot_table('births', index='last_char', columns=['sex', 'year'], aggfunc = sum)

subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
