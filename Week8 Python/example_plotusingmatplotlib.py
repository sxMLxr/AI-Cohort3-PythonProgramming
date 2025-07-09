#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:19:11 2022

@author: skciller
"""
import numpy as np
import matplotlib.pyplot as plt

#line graph
#creating simple arrays of EQUAL sizes
#x = np.array([0,100]) 
#print(x)
#y = np.array([0, 4])
#plt.plot(x, y)  #(x-axis, y-axis)
#plt.show()

# line graph
#x = np.array([0,10,30,20,40,100])
#y = np.array([0,1,2,3,4,30])
#plt.plot(x, y)  #(x-axis, y-axis)
#plt.show()

# scatter plot 1
#x = np.array([0,10,30,20,40,100])
#y = np.array([0,1,2,3,4,30])
#plt.plot(x, y, 'o')  #(x-axis, y-axis)
#plt.show()

#scatter plot v2
#x = np.array([0,10,30,20,40,100])
#y = np.array([0,1,2,3,4,30])
#plt.scatter(x, y)  #(x-axis, y-axis)
#plt.show()


### multiple graphs on same page
a = np.array([0,80,100])
b = np.array([0,40,92])
x = np.array([0,10,30,20,40,100])
y = np.array([0,1,2,3,4,30])
s = np.array([0,50,40, 60,40,100])
t = np.array([0,10,40, 40,40,100])

plt.plot(x, y)  #(x-axis, y-axis)
plt.plot(s, t)  #(x-axis, y-axis)
#plt.show()

plt.plot(a,b)  #(x-axis, y-axis)
plt.show()
#### plt.show is used once


