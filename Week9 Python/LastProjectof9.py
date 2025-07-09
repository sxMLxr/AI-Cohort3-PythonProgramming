#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:46:04 2022

@author: skciller
"""


import pandas as pd
import numpy as np

df = pd.read_csv('sales_data_sample.csv', header = 0, encoding='Latin-1')
#df.head(20)
#values, counts = np.unique(df['YEAR_ID'], return_counts=True)
#print(values, '\n', counts)  
#data covers years 2003, 2004, 2005
#[2003 2004 2005] 
#[1000 1345  478]
df.head(20)
#values, counts = np.unique(df['PRODUCTLINE'], return_counts=True)
#print(values, '\n', counts) 
#['Classic Cars' 'Motorcycles' 'Planes' 'Ships' 'Trains' 'Trucks and Buses' 'Vintage Cars'] 
# [967            331          306       234     77       301                607]

df.describe()
#lets narrow down our search to determine year, and productline type
#YEAR_QTR_All = df.groupby(["YEAR_ID","QTR_ID"])["PRODUCTLINE","QTR_ID","YEAR_ID"].agg(['mean','count','sum'])
YEAR_QTR_All = df.groupby(["PRODUCTLINE","YEAR_ID","QTR_ID"])["PRODUCTLINE","SALES"].agg(['mean','count','sum'])

print(YEAR_QTR_All)
                                                
#print(YEAR_QTR_All["PRODUCTLINE","QUANTITYORDERED","SALES"].sum())
#ex: df.groupby(['publication', 'date_m'])[['claps', 'reading_time']].agg(['mean', 'count', 'sum'])