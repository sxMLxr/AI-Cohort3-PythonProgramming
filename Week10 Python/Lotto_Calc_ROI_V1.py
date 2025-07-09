#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:07:29 2022

@author: shames y
"""

import pandas as pd
import numpy as np
import random

def gen_5_numbers():
    numbers = []
    count = 0
    while count <5:
        numbers.append(random.randint(1,39)
        count +=1
    return numbers

def win_lotto(winning_numbers):
    user_number = gen_number()
    total_losses = 1
    highest_match = 0
    
    while user_numbers != winning_numbers:
        match =0
        user_numbers = gen_numbers()
        total_losses += 1
        for number in user_numbers:
            if number in winning_numbers:
                match+=1
        if match > highest_match:
            highest_match = match
        
        total_losses_formatted = locale.format.string("%d",total_losses, grouping=True)
        print("Highest Match: {}. Ticket_match: {}.  Tickets_Purchased: {}   {} {}"
              .format(hightest_match, match, total_losses_formatted, user_numbers, winning_numbers))
             
return "you won after {} tries".format(total_losses_formatted)

              
dfN = pd.read_csv('NCEL-Cash5.csv', header = 0)
dfND = pd.read_csv('NCEL-Cash5-Detailed.csv', header = 0)

#print(dfN.columns)
##our data: 
#['Date', 'Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5', 'DP']

#print(dfND.columns)
#our data:
#['date', 'prize_5', 'prize_4', 'winners_5', 'winners_4', 'winners_3',
#       'winners_2', 'prize_5_double_play', 'prize_4_double_play',
#       'winners_5_double_play', 'winners_4_double_play',
#       'winners_3_double_play', 'winners_2_double_play']    

"""
1. Read in the following 2 files:  NCEL-Cash5.csv and NCEL-Cash5-Detailed.csv
2. Calculate the return on investment (ROI) from playing the same 5 numbers every time the game is offered.
3. Calculate the ROI from playing 5 random numbers on each draw.
4. For an added challenge, change this calculation to occur starting at an arbitrary start date (rather than the beginning of the data set).
5. For an even greater challenge, run multiple trials for the above setup and report the average ROI for each.
"""
print(dfN.tail())
#clean the data .. search for nans, 0s and other
B1values, B1counts = np.unique(dfN['Ball 1'], return_counts=True)
B2values, B2counts = np.unique(dfN['Ball 2'], return_counts=True)
B3values, B3counts = np.unique(dfN['Ball 3'], return_counts=True)
B4values, B4counts = np.unique(dfN['Ball 4'], return_counts=True)
B5values, B5counts = np.unique(dfN['Ball 5'], return_counts=True)

#print(B1values)
#nan is present.. we need to remove it from dfN

#line 5802 needs to be removed from dfN
dfN.drop(index=5802, inplace=True)
#print(dfN.tail())
#confirmed index 5802 has been removed
#print(dfN.tail())

#Calc ROI for playing same 5 numbers every time game is offered
mynumbers = [5, 15, 36, 28, 32]

#gets some stats
total_games = 5801 #count of dfN line numbers
#get total count of all occurances of my numbers in all columns for 5801 games
total_countof5 = B1counts[4]+B2counts[4]+B3counts[4]+B4counts[4]+B5counts[4]
total_countof15 = B1counts[14]+B2counts[14]+B3counts[14]+B4counts[14]+B5counts[14]
total_countof36 = B1counts[35]+B2counts[35]+B3counts[35]+B4counts[35]+B5counts[35]
total_countof28 = B1counts[27]+B2counts[27]+B3counts[27]+B4counts[27]+B5counts[27]
total_countof32 = B1counts[31]+B2counts[31]+B3counts[31]+B4counts[31]+B5counts[31]

# check our results
print(total_countof5/5801 * 100)  
print(total_countof15)
print(total_countof36)
print(total_countof28)
print(total_countof32)

#calculation of 5 numbers over x-games
#(G, C) = G/C = G!/C!(G-C)!
#C= (games, 5) = 5801! /5!(5801-5)!
