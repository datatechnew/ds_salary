# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:57:26 2020

@author: Administrator
"""


import pandas as pd
df = pd.read_csv('glassdoor_jobs2000.csv')


'''
1.salary parsing
2.company name string only
3.state parsing
4.company age engineering
5.parsing job description(skills, degree, major, experience)
'''


#check how many null values in the headquarter columns
h = df['Headquarters'].value_counts()

#drop headquarter column from the original dataset
df.drop('Headquarters', axis= 1, inplace =True)

#check competitors value
c = df['Competitors'].value_counts()

#drop column since all values are -1, from the original dataset
df.drop('Competitors', axis= 1, inplace = True)

df.columns




#1. salary parsing
#drop values = -1 from the salary Estimate column
df = df[df['Salary Estimate'] != '-1']

#extract the numeric values from salary Estimate 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0].replace('K', '').replace('$', ''))




# 2.company name string only
df['Company'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 1 else x['Company Name'][:-3], axis = 1)



#3.state parsing
df['State'] = df['Location'].apply(lambda x: x[-2:])
df['State'].value_counts()




#4.company age engineering
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)


#5.parsing job description (skills: SAS, AWS, Python, C++, Java, )
# top 9 data science tools for ds(excel, sas, tableau, spark)
df['SAS'] = df['Job Description'].apply(lambda x: 1 if 'sas' in x.lower() else 0)
df['python']= df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['aws']= df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['tableau']= df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['spark']= df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

df.to_csv('data_cleaned', index= False)














