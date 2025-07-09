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
#instruction 1
organisms = int(input("how many organism: "))


while True:
    try:
        # instruction 2
        percentinput = input("daily growth percentage: ")
        # instruction 4
        if percentinput.__contains__("%"):
            break
        else:
            print(".. please enter a % after int")
    except:
        print(".. please enter a % after int")

# instruction 3
num_days = int(input("how many days to calculate: "))
total_org = org_growth = 0

print("Organisms 		@",percentinput," Daily Growth")
print("-------------------------------")

#strip the percent character and 
#convert to actual percentage
percentgrowth = int(percentinput.strip("%"))/100

#instruction 6 
for days in range(num_days):
    org_growth = float(organisms + (organisms * percentgrowth) * days)
    # instruction 5
    print("Day: ", days, "\t\t", org_growth)
    