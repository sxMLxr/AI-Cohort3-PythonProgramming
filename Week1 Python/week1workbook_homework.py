#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 08:24:27 2022

@author: skciller

"""
'''
x = 1; y = 6

while x < y:
    x += 3
    print("while: good data")
'''
'''
for x in range(1, 100, 3):
    if x < y:
        print("for: good data")
    else:
        break

number = 1.0    
total = 0.0
# while condition is true... repeat the loop and calculate the input to the total
while number > 0:
    # a negative number will break this while loop, tell the user how to quit
    # all entries will be accepted as float integers
    number = float(input('Enter a positive number (negative to quit): '))

    if number > 0:
        total = total + number
#print the output with 2 decimal values
print (f'Total = {total:.2f}') 

for x in range(1,10):
    number = float(input('Enter a positive number (negative to quit): '))

    if number > 0
        total = total + number
    else:
        break
    
print (f'Total = {total:.2f}') 

'''

caloriesPerMinute = 4.2
caloriesBurned= 0.0
minutes = 10

print ('Minutes\t\tCalories Burned')
print ('-------------------------------')
while minutes < 31:
    caloriesBurned = caloriesPerMinute * minutes
    print(minutes, "\t\t", caloriesBurned)
    minutes = minutes + 5