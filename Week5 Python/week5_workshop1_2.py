#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:15:37 2022

@author: skciller
"""

class salary:
    def __init__(self, monthlyincome, bonus):
        self.monthlyincome = monthlyincome
        self.bonus = bonus
        
    def get_monthlyincome(self):
        return self.monthlyincome
    
    def get_bonus(self):
        return self.bonus
        
    def set_monthlyincome(self, monthlyincome):
        self.monthlyincome = monthlyincome

    def set_bonus(self, bonus):
        self.bonus = bonus

class employee:
    def __init__(self, monthlyincome, bonus, employeeid, jobtitle):
        self.salary = salary(monthlyincome, bonus) #object composition
        self.employeeid = employeeid
        self.jobtitle = jobtitle
        
    def set_employeeid(self, employeeid):
        self.employeeid = employeeid
    
    def set_jobtitle(self, jobtitle): 
        self.jobtitle = jobtitle

    def get_employeeid(self):
        return self.employeeid
        
    def get_jobtitle(self): 
        return self.jobtitle
           


def main():

    employee1 = employee(5000,4000, "127654", "manager")
    employee2 = employee(4500, 250, "987654", "supervisor")
    
    print_info(employee1)
    print_info(employee2)
    
def print_info(employeeinfo):
    print(f'{employeeinfo.get_employeeid()}\n{employeeinfo.get_jobtitle()}')
    print(f'{employeeinfo.salary.get_bonus()}\n')
    
    
   
if __name__ == "__main__":
        main()
            