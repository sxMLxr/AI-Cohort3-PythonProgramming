#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:40:30 2022

@author: skciller
"""

import pandas as pd 
import matplotlib.pyplot as mp 

# read csv 
#d = pd.read_csv("C:\\Users\\amit_\\Desktop\\cars.csv") 
d = pd.read_csv("cars.csv") 
#Car Reg_Price 0 BMW 2000 1 Lexus 1500 2 Audi 1500 3 Jaguar 2000 4 Mustang 1500

print("\nReading the CSV file...\n",d) 

# dataframe 
dataFrame = pd.DataFrame(d.head(), columns=["Cars","Reg Price"]) 

# plotting the dataframe 
dataFrame.plot(x="Cars", y="Reg Price", kind="bar", figsize=(10, 9))

# displaying bar graph 
mp.show()