#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:01:40 2022

@author: skciller
"""
import random as rand

class employee:
    def __init__(self, employeeid, jobtitle, monthlyincome, name):
        self.employeeid = employeeid
        self.jobtitle = jobtitle
        self.monthlyincome = monthlyincome
        self.name = name
    
        
    def get_employeeid(self):
        return self.employeeid
    
    def get_jobtitle(self): 
        return self.jobtitle

    def get_monthlyincome(self):
        return self.montlyincome
        
    def get_name(self): 
        return self.name

    
def main():
    randm = int(rand.random() * 1000)
    print (randm)
    print_info("empname", randm)
    
def print_info(emp_name, randm):
    employeeid = f'empname_{randm}'
    print(f'{employeeid}')
    #complete the assignment
    
    
if __name__ == "__main__":
            main()