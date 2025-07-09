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
            
print(ULIST['Cla_20031'])

#print(YEAR_QTR_ALL)
#print(YEAR_QTR_All)      
#print(COUNTRY_YEAR_QTR_All)
#print(Contact_COUNTRY_YEAR_QTR_All)

import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)

def sales_plot(self, indexer, loYQS, Prodline):
    def __init__(self):
        index = indexer
        listofyr_qtr_sales = loYQS
        productline = Prodline
        
        axs[index].set_ylabel('2003 QT1-QT4')
        qt1_2003 = [M_20031["SALES"].sum(), M_20032["SALES"].sum(), M_20033["SALES"].sum(), M_20034["SALES"].sum()]
        axs[index].plot(qt1_2003)

#axs[index].set_title('Motorcycle Sales')


fig.set_size_inches(6.0, 6.0)
fig.set_dpi(100)

#call sales_plot()
#axs[0].plot(qt1_2003)


"""
axs[1].set_ylabel('QT2')
axs[1].plot(YEAR_QTR_ALL2["SALES"].sum())

axs[2].set_ylabel('QT3')
axs[2].plot(YEAR_QTR_ALL3["SALES"].sum())

axs[3].set_ylabel('QT4')
axs[3].plot(YEAR_QTR_ALL4["SALES"].sum())
"""

plt.show()