#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:46:04 2022

@author: skciller
"""


import pandas as pd
import numpy as np


df = pd.read_csv('sales_data_sample.csv', header = 0, encoding='Latin-1')
df.head(2)

Yvalues, Ycounts = np.unique(df['YEAR_ID'], return_counts=True)
#print(values, '\n', counts)  
#data covers years 2003, 2004, 2005
#[2003 2004 2005] 
#[1000 1345  478]

df.drop('ORDERNUMBER', inplace=True, axis=1)  #drop ordernumber column
df.drop('ORDERLINENUMBER', inplace=True, axis=1)  #drops orderlinenumber column
df.drop('STATUS', inplace=True, axis=1)  #drops orderlinenumber column
df.drop('ADDRESSLINE2', inplace=True, axis=1)  #drops orderlinenumber column
df.drop('QUANTITYORDERED', inplace=True, axis=1)  #drops Quantity Ordered column
df.drop('MSRP', inplace=True, axis=1)  #drops MSRP column
df.drop('CUSTOMERNAME', inplace=True, axis=1)  #drops MSRP column
df.drop('PHONE', inplace=True, axis=1)  #drops MSRP column
df.drop('ADDRESSLINE1', inplace=True, axis=1)  #drops MSRP column
df.drop('CITY', inplace=True, axis=1)  #drops MSRP column
df.drop('STATE', inplace=True, axis=1)  #drops MSRP column
df.drop('PRICEEACH', inplace=True, axis=1)  #drops MSRP column
df.drop('ORDERDATE', inplace=True, axis=1)  #drops MSRP column
df.drop('MONTH_ID', inplace=True, axis=1)  #drops MSRP column
df.drop('PRODUCTCODE', inplace=True, axis=1)
df.drop('POSTALCODE', inplace=True, axis=1)
df.drop('COUNTRY', inplace=True, axis=1)
df.drop('TERRITORY', inplace=True, axis=1)
df.drop('CONTACTLASTNAME', inplace=True, axis=1)
df.drop('CONTACTFIRSTNAME', inplace=True, axis=1)
df.drop('DEALSIZE', inplace=True, axis=1)

Pvalues, Pcounts = np.unique(df['PRODUCTLINE'], return_counts=True)
#print(values, '\n', counts) 
#['Classic Cars' 'Motorcycles' 'Planes' 'Ships' 'Trains' 'Trucks and Buses' 'Vintage Cars'] 
# [967            331          306       234     77       301                607]

Qvalues, Qcounts = np.unique(df['QTR_ID'], return_counts=True)
#print(Qvalues, '\n', Qcounts) 

#df.describe()
#lets narrow down our search to determine year, and productline type
#YEAR_QTR_All = df.groupby(["YEAR_ID","QTR_ID"])["PRODUCTLINE","QTR_ID","YEAR_ID"].agg(['mean','count','sum'])
##YEAR_QTR_All = df.groupby(["PRODUCTLINE","YEAR_ID","QTR_ID"])["SALES"].agg(['median','mean','count','sum'])
#YEAR_QTR_All = df.groupby(["PRODUCTLINE","YEAR_ID","QTR_ID"]).agg(['median','mean','count','sum'])
##COUNTRY_YEAR_QTR_All = df.groupby(["COUNTRY","PRODUCTLINE","YEAR_ID","QTR_ID"])["SALES"].agg(['median','mean','count','sum'])
##Contact_COUNTRY_YEAR_QTR_All = df.groupby(["CONTACTLASTNAME","COUNTRY","PRODUCTLINE","YEAR_ID","QTR_ID"])["SALES"].agg(['median','mean','count','sum'])

#convert to a function
"""
M_20031 = df[
    (df["PRODUCTLINE"]=='Motorcycles') &
    (df["YEAR_ID"]==2003) &
    (df["QTR_ID"]==1) 
    ]
M_20031.drop('PRODUCTLINE', inplace=True, axis=1)
"""
#make a copy dataframe
dfbackup = df 

#filter the data we want to gets some stats
ULIST = {}
for Pvals in Pvalues:
    for Yvals in Yvalues:
        for Qtrs in Qvalues:
            #print(Pvals, Yvals, Qtrs)
            UvariableN = f'{Pvals[:3]}_{Yvals}{Qtrs}'
            UvariableD = UvariableN
            try:
                UvariableD = dfbackup[
                    (dfbackup["PRODUCTLINE"]==Pvals) &
                    (dfbackup["YEAR_ID"]==Yvals) &
                    (dfbackup["QTR_ID"]==Qtrs) 
                    ]
                #UvariableD.drop('PRODUCTLINE', inplace=True, axis=1)    
            #print(Uvariable)
            except SettingWithCopyWarning:
                UvariableD = "No Data"
            finally:
                ULIST[UvariableN]=UvariableD
            

import matplotlib.pyplot as plt

fig, axs = plt.subplots(3,4)
# to use a 3x4 matrix we need to reshape our list to a 3x4 matrix
#for ease of programming

fig.set_size_inches(15.0, 15.0)
fig.set_dpi(100)


def sales_plot(CounterA, CounterB, str_indextext):
    LOPi = str(str_indextext)
    LOP = str(str_indextext[:8])
    #index = int()
    LOP1 = f'{LOP}{1}'
    LOP2 = f'{LOP}{2}'
    LOP3 = f'{LOP}{3}'
    LOP4 = f'{LOP}{4}'
        
    axs[int(CounterA)][int(CounterB)].set_ylabel(str_indextext[:8]+'\nQT1-QT4')
    axs[int(CounterA)][int(CounterB)].set_xlabel("QTR")
    
    LOPi = [ULIST[LOP1]["SALES"].sum(), ULIST[LOP2]["SALES"].sum(), ULIST[LOP3]["SALES"].sum(), ULIST[LOP4]["SALES"].sum()]
    
    return axs[int(CounterA)][CounterB].plot(LOPi)
   
#print(ULIST['Cla_20031'])
#print(ULIST.keys())

#make a generic list so we can index through them
listofproducts = []
for items in ULIST:
    listofproducts.append(items)
#    print(items)
# print(listofproducts[:12]) # test successful
print(listofproducts)
#listofproducts.shape()

# since we know there are 4 qtrs per year and year starts at 2003, 
# we can us this as our indexer to cycle through the list to create some graphs
CounterA = 0
CounterB = 0
"""
for indexer in range(0,len(listofproducts)+1,4):
    str_index = listofproducts[indexer]
    #print(str_index)
    if CounterA <= 3:
        for CounterB in range(0,4):
            sales_plot(CounterA, CounterB, str_index)
        #print(count)
    else:
        break
    CounterA +=1

plt.show()
"""