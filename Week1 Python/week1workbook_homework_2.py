#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 08:24:27 2022

@author: skciller

## 1.3 Basic loop structures (Group):

Develop a program that will:

1. Take input from the user asking how many organisms to start with.
2. Take input from the user asking the average daily increase for the organisms.
3. Take input from the user asking the number of days to multiply.
4. Make sure the daily increase was entered as a percentage, if not correct it.
5. Print each day and the increase in organsisms for each day. 
6. Make sure to format the printing so that it is readable.
"""

organisms = int(input("how many organism: "))
while True:
    try:
        percentinput = input("daily growth percentage: ")
        '''if percentinput.__contains__("%"):
            print("values: ", percentgrowth[0], percentgrowth[1])
        '''
        if percentinput.__contains__("%"):
            break
        else:
            print(".. please enter a % after int")
    except:
        print(".. please enter a % after int")

num_days = int(input("how many days to calculate: "))
total_org = org_growth = 0

print("Organisms 		@",percentinput," Daily Growth")
print("-------------------------------")
percentgrowth = int(percentinput.strip("%"))/100 #convert to actual percentage
for days in range(num_days):
    org_growth = float(organisms + (organisms * percentgrowth) * days)
    print("Day: ", days, "\t\t", org_growth)
    