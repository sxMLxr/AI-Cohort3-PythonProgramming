#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:19:11 2022

@author: skciller
"""
import numpy as np
import matplotlib.pyplot as plt

##
##  Legends, Labels, and fonts
##
## changing the fonts (color, font, size, etc)
font1 = {'family': 'serif', 'size': 23, 'color': 'red'}
#add fontdict=font1) to end of plt.title
#add fontdict=font1) to end of plt.xlabel
#add fontdict=font1) to end of plt.ylabel


x = np.array([0,1,2,3,4])
y = np.array([20,30,50,100,80])
plt.plot(x, y, label="Class 1")

## add a title with fonts, color, size
plt.title('shoe size vs height for two classes', fontdict=font1)

## setting up a x and y labels (you just need one)
plt.xlabel('shoe size')
plt.ylabel('height (cm)')

a = np.array([10,5,2,12,5])
b = np.array([10,21,45,60,50])
plt.plot(a, b, label="Class 2")
## setting up a x and y labels



## plot legend
plt.legend()

#last command show the graph
plt.show()
