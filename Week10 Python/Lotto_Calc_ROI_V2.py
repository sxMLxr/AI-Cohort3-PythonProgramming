#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:07:29 2022

@author: shames y
"""

import pandas as pd
import numpy as np
import random
import locale

def gen_5_numbers():
    numbers = []
    count = 0
    while count < 5:
        numbers.append(random.randint(1,39))
        count += 1
    return numbers


def win_lotto(df, my_numbers):
    
    numberlist = df[:].loc(1)
    string = numberlist["Ball 1","Ball 2","Ball 3","Ball 4","Ball 5"]
    counter = 0 
    myn= my_numbers
    n1,n2,n3,n4,n5,n6 = str(string.values[counter]).split(".")
    n1 = n1[1:]
    n6 = n6[:3]  #leaving this out
    winn = [int(n1), int(n2), int(n3), int(n4), int(n5)] 
    
   
    total_losses = 1
    highest_match = 0

    while myn != winn:
        match =0
        total_losses += 1
        
        n1,n2,n3,n4,n5,n6 = str(string.values[counter]).split(".")
        n1 = n1[1:]
        n6 = n6[:3]  #leaving this out
        winn = [int(n1), int(n2), int(n3), int(n4), int(n5)] 
        
        for number in myn:
            if number in winn:
                match+=1
                 
        if match > highest_match:
            highest_match = match
            historycounter = counter 
            
        total_losses_formatted = locale.format_string("%d",total_losses, grouping=True)
        #print("Highest Match: {}. Ticket_match: {}.  Tickets_Purchased: {}   !{} !!{}"
        #      .format(highest_match, match, total_losses_formatted, myn, winn))
             
        if match == 5:
            #print('Won after {} tries'.format(historycounter))
            dollar = dfJOINED["prize_5"].values[historycounter-5801]
            percent = ((dollar - historycounter)/historycounter)*100
            print(f'With 5 matches, ${dollar} with ROI from {historycounter} tries, at {percent}%')
            break
        elif counter == 5801:
            #print('Won after {} tries, with: {} matches '.format(historycounter, highest_match, historycounter))
            print(string.values[historycounter])
            dollar = dfJOINED["prize_4"].values[historycounter-5801]
            percent = ((dollar-historycounter)/historycounter)*100
            print(f'With {highest_match} matches, ${dollar} with ROI from {historycounter} tries, at {percent:.2f}%')
            break
       
        counter += 1
        
       


my_numbers = gen_5_numbers()

#win_lotto(winning_numbers)
"""
1. Read in the following 2 files:  NCEL-Cash5.csv and NCEL-Cash5-Detailed.csv
2. Calculate the return on investment (ROI) from playing the same 5 numbers every time the game is offered.
3. Calculate the ROI from playing 5 random numbers on each draw.
4. For an added challenge, change this calculation to occur starting at an arbitrary start date (rather than the beginning of the data set).
5. For an even greater challenge, run multiple trials for the above setup and report the average ROI for each.
"""
              
dfN = pd.read_csv('NCEL-Cash5.csv', header = 0)
dfND = pd.read_csv('NCEL-Cash5-Detailed.csv', header = 0)


dfN.drop(index=5802, inplace=True)
#print(dfN.tail())
#print(dfND.tail())
# confirmed last entry was removed.

#lets join the two files after sorting dfN
dfN.sort_index(ascending=False, inplace=True)

#print(dfN.head())
#descending order confirmed

#join files
dfJOINED = dfN.join(dfND.set_index(['date']), on=['Date'])

print(my_numbers)
numberlist = dfN[:].loc(1)

#print(data, val1, val2, val3, val4, val5, DPval)

win_lotto(dfN, my_numbers)

#things to fix... duplicate values in random string
#highest match to calculate ROI 