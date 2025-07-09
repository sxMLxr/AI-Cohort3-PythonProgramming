#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:15:17 2022

@author: skciller
"""


tup =(100,100,100,200) #list
tup2 =[100,100,100,300] #tuple
tup3 =["100","100","100","300"] # tuple
tup4 ={200:50,200:50,200:50,300:50} #dictionary
set={"brown","cow"}

print(tup)
print(len(tup))
print(tup[0])
for i in range(len(tup)):
    print(f'list: {tup[i]}')
    
for i in range(len(tup2)):
    print(f'tuple: {tup2[i]}')
    
for i in range(len(tup3)):
    print(f'tuple: {tup3[i]}')
    
for i in tup4:
    print(f'dictionary: {i}')
    
for i in set:
        print(f'set: {i}')