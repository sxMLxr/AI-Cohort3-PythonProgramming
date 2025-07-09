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

# line graph matplotlib default x and y axis
#x = np.array([0,10,30,20,40,100])
#y = np.array([0,1,2,3,4,30])
#plt.plot(x)  #(x-axis, y-axis)
#plt.show()
#defaults to y = ([0 1 2 3 4 5 ...])



##===========================================
#change markers in matplotlib
x = np.array([0,1,2,3,4])
y = np.array([20,30,50,100,80])


#change color line reference and graphs
plt.plot(x,y,color="red", linestyle="--", marker='<', markersize=8, lw=2)
##plt.plot(x,y,color="red", linestyle="--", marker='<', ms=8)

## color styles
#plt.plot(x,y,color="blue")
#plt.plot(x,y,color="green")
#plt.plot(x,y,c="aqua")

## change marker size (simplified to ms)
#plt.plot(x,y,marker='o', markersize=5)   5 is default

##change marker color (simplified to mfc)
#.... , markerfacecolor='blue')

##change marker edge color (simplified to mec)
#... , markeredgecolor='blue'

## line width - linewidth=2 (simplified to lw)
#default is 1

plt.show()

"""Marker code
"."  point
","  pixel
"o"  circle
"v"  triangle down
"^"  triangle up
"<"  triangle left
">"  triangle right
"1"  tri_down
"2"  tri_up
"3"  tri_left
"4"  tri_right
"8"  octagon
....
"""
