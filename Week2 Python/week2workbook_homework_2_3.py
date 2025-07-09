#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program that will do the following:

    Compute the kinetic energy for five different individuals.
    You may input the values for the individuals or hard-code them.
    Store the results for the individuals in some fashion, think list or dictionary.
    Print the results that have been stored.
    Implement each of the above items in different functions, think modularly.

KE = 1/2 m v^2 where: KE = kinetic energy(J), m = mass(Kg), v = velocity(m/s)
"""


def main():
    #mass = ("100","200","125","145","140")  test with tuples
    mass = [100,200,125,145,140]
    #velocity = ("6","5","4","3","2")  test with tuples
    velocity = [6,5,4,3,2]
    KE= list()
    
    print ('KE\t results')
    print ('-----------------------------')
    print(mass)
    print(velocity)
    
    KE = kinetic_energy(mass, velocity)
    print_list(KE)
    
    
def kinetic_energy(mas, vel):
    kenergy = list()
    
    for x in range(len(mas)):
        kenergy.append(1/2 * mas[x] * vel[x]**2)
        # test with tuples -- 
        # kenergy.append(1/2 * int(mas[x].strip("'")) * int(vel[x].strip("'")) **2)
    return kenergy

def print_list(n_list):
    print(n_list)
    
main()
