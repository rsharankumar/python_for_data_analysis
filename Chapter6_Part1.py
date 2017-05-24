# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:34:32 2017

@author: skumarravindran
"""
import pandas as pd
from pandas import Series, DataFrame
import json
import sqlite3

ex1 = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch06/ex1.csv', sep=',')

ex2 = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch06/ex2.csv', header=None)

ex2 = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch06/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

ex2 = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch06/ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col = ['message'])

ex6 = pd.read_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch06/ex6.csv', nrows=5)

# writing back to the drive
ex2.to_csv('C:/Users/skumarravindran/Desktop/Python/pydata-book-master/ch06/out.csv')

obj = """ {"name": "Wes", 
           "places_lived": ["United States", "Spain", "Germany"], 
           "pet": null, 
           "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},              
                        {"name": "Katie", "age": 33, "pet": "Cisco"}] } """
           

result = json.loads(obj)

siblings = DataFrame(result['siblings'], columns=['name', 'age', 'pet'])


query = """ CREATE TABLE test (a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER );"""

con = sqlite3.connect(':memory:') 
con.execute(query) 
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),        
        ('Tallahassee', 'Florida', 2.6, 3),        
        ('Sacramento', 'California', 1.7, 5)] 

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data) 
con.commit()

cursor = con.execute('select * from test')