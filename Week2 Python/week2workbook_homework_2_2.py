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
    mass_velocity = dict()
    mass_velocity = ("100:6","200:5","125:4","145:3","140:2")
    
        
    print ('KE\t results')
    print ('-----------------------------')
    
    KE = kinetic_energy(mass_velocity)
    
        
def kinetic_energy(massvel):
    kenergy = list()
    
    for count in massvel:
        print (f'{massvel[count]}')
        print (f'{massvel[count].values()}')
        """kenergy.append(1/2(int(massvel[count]) * int(massvel[count].values())**2))
        """

def print_dict(dictionary):
    return print(dictionary)

def print_list(n_list):
    print(n_list)
    
main()