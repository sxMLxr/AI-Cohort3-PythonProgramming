#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Write a program that will do the following:

    Convert kilometers to miles.
    Take input from the user in miles
    Create a function that will convert the input to kilometers
    Output the answer to the user.

1 kilometer = .6214 miles
1 mile = 1.609 kilometers
"""

#instruction 1
def main():

    miles = 0.0
    kilometers = 0.0
    #instruction 2
    miles = float(input('Enter the number of miles to convert: '))
    #instruction 3 
    kilometers = miles_to_kilometers(miles)
    #instruction 4
    print (f'{miles} miles = {kilometers} kilometers')
    
def miles_to_kilometers(miles):
    #using kilometer/ miles conversion
    return 1.609 * miles

main()