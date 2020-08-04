# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:15:33 2020

@author: Administrator
"""


import glassdoor_scaper as gs
import pandas as pd
path = "/Users/Administrator/Documents/ds_salary_proje/chromedriver"

df = gs.get_jobs("data scientist", 3500, False, path, 15)

df
