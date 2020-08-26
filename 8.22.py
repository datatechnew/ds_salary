# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:09:29 2020

@author: Administrator
"""


import pandas as pd 

df = pd.read_csv("data_cleaned.csv")

df.head()

df.columns



df6 = df[['Job Title', 'Salary Estimate','Company Name', 'Location', 'Size', 'Founded', 'Type of ownership','Industry', 'salary', 'Company', 'State']]

a = pd.DataFrame(df6)
a.to_csv("shy.csv", index = False)
