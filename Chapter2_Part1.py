# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = 'C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

open(path).readline()

records = [json.loads(line) for line in open(path)]

#print records[19]['tz']

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

frame = DataFrame(records)

tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')

clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()

tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)

indexer = agg_counts.sum(1).argsort()

count_subset = agg_counts.take(indexer)[-10:]

#PLotting

# plot 1
count_subset.plot(kind='barh', stacked=True)
# plot 2 - normalized
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)

