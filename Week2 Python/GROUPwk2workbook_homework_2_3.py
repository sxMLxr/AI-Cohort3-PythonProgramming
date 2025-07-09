#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:06:52 2022

@author: skciller
"""
# copied from class
def main():
    arr = generateIndiv(5)
    print_chart(arr)
    
    #print(arr)
    
def generateIndiv(number):
    indivArray = []
    for i in range(number):
        while True:
            try:
                mass, velocity = map(int, input(f'Please enter the mass then velocity of indiv {i}: ').split())
                break
            except:
                print("Invalid entry, try again")
        indivArray.append([mass,velocity, kineticEnergy(mass, velocity)])
    return indivArray


def print_chart(array):
    print ('Mass (kg) \t Velocity \t Kinetic Engergy in Joules by Velocity in m/sec ')
    for i in range(len(array)):
        t = array[i]
        m = t[0]
        v = t[1]
        ke = t[2]
        print(f'{m} \t \t {v} \t \t {ke}')

    
def kineticEnergy(m,v):
    return 0.5 * m * v ** 2

main()