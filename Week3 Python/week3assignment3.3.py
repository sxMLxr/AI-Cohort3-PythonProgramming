#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:42:08 2022

@author: skciller
"""

import random as rn

rand = rn.randint(1,50)
    
def correct(number):
    print("nice work, the number was:",rand)
    return number
    
    
def guess_again():
    number = int(input("Guess what number im thinking of: ENTER 0 to end  "))
    return number


def main():

    number = guess_again()
    print(f'You have "{number}" guesses-- good luck')
    
    for i in range(number,0,-1):
        if number == 0 or number == rand or i==0:
            correct(number)
            return 0
        elif number < rand:
            print("Guess again, too low")
        else: #number > rand:
            print("Guess again, too high")    
        guess_again()
        

if __name__ == '__main__':
    main()