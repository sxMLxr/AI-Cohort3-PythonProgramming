#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:26:04 2022

@author: skciller
"""

##==== class group work test code
import numpy as np

new_array = []
twod_array = [[1,2,3,4],[5,6,7,8],[5,6,7,8]]

def time_sec(x):
    def __init__(self):
        self.x = x
    #print(x)
    hrs, mins, secs = x.split(":")
    return float(hrs)*3600 + float(mins)*60 + float(secs)

ironman_data = np.genfromtxt('2019 Ironman World Championship Results.csv', 
                             delimiter = ',', dtype = 'str', skip_header=1)

numeric_only = ironman_data[:,6:10]
numeric_only = np.where(numeric_only=='', '0:0:0', numeric_only)
numeric_only = np.array(numeric_only)

for elements in numeric_only:
    #e10,e11,e12,e13,e14 = elements[10], elements[11], elements[12], elements[13], elements[14]
    e10,e11,e12,e13 = time_sec(elements[0]), time_sec(elements[1]), time_sec(elements[2]), time_sec(elements[3])
    new_array.append([e10,e11,e12,e13])

print(np.shape(new_array))
print(np.shape(twod_array))