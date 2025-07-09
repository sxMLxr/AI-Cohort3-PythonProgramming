#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:52:01 2022

@author: skciller
"""
def main():
   
    number = int(input('Give me a number for the Fibonacci Sequence: '))

    print("Fibonacci series: ")
    print(print_fnum(number).values())  #no need to save variable just print

def print_fnum(N):   

    arr = {}
    arr[0] = 1 
    arr[1] = 1
    
    if N in arr: #
        return arr[N] 
    else:
        for i in range(2,N+1): #start at index 2, as 0 & 1 already defined
            #do some math to get fibonacci sequence
            arr[i] = arr[i-1] + arr[i-2]
            
    return arr
                           
if __name__ == '__main__':
    main()
 