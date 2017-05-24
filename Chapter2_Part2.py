# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:38:25 2017

@author: skumarravindran
"""

import json 
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

unames = ['user_id', 'gender', 'age', 'occupation', 'zip'] 
users = pd.read_table('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch02/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp'] 
ratings = pd.read_table('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch02/movielens/ratings.dat', sep='::', header=None, names=rnames)


mnames = ['movie_id', 'title', 'genres'] 
movies = pd.read_table('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch02/movielens/movies.dat', sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(users, ratings), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

mean_ratings_occ = data.pivot_table('rating', index='occupation', columns='gender', aggfunc='mean')

ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings = mean_ratings.ix[active_titles]

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

# difference of two columns
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

# calculating the std deviation
rating_std_by_title = data.groupby('title')['rating'].std()