#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:15:13 2022

@author: skciller
"""

class savings:
    def __init__(self, acctnumber, interestrt, balance):
        self.acctnumber = acctnumber
        self.interestrt = interestrt
        self.balance = balance
    
    def set_acctnumber(self, acctnum):
        self.acctnumber = acctnum
    
    def get_acctnumber(self):
        return self.acctnumber
    
    def set_interestrt(self, intrate):
        self.interestrt = intrate
        
    def get_interestrt(self):
        return self.interestrt
        
    def set_balance(self, balnc):    
        self.balance = balnc
    
    def get_balance(self):
        return self.balance
        
class cd(savings):
    def __init__(self, matrdate):
        self.maturedate = matredate
    
    def set_matdate(self, mdate):
        self.maturedate = mdate
        
    def get_matdate(self):
        return self.maturedate
    
def print_object(object_name):
        print(object_name.acctnumber)
        print(object_name.interestrt)
        print(object_name.balance)  
    
 
def main():
    listaccts = [] #global list
    choices= ["(s)avings", "(b)alance", "(i)nterestRate", "(a)cctnumber"]
    
    while True:
        i = 0 
        accts = input(f'Enter a new acct number "(Q to quit)" ')
        if accts != ("q" or "Q"):
            intrate = input('  Current interest rate: ')
            startbalance = input('  Starting balance: ')
            accts = savings(accts, intrate, startbalance)
            listaccts.append(accts)
            i+=1
        else:
            break
    
    print(f'{choices}')
    choice_select = input("  available options: ")
    for la in listaccts:
        print("accts available: ", la.get_acctnumber())
    activeacct = input(f"(S)avings Account to Edit: ")
    
    while choice_select != ("Q" or 'q'):
            
        if choice_select == ('S' or 's'):
            for la in listaccts:
                print("accts available: ", la.get_acctnumber())
            activeacct = input(f"(S)avings Account to Edit: ")
            
        elif choice_select == ('B' or 'b'):
            print(f"(B)alance Account: {choice_select}")
            
        elif choice_select == ('I' or "i"):
            print(f"(I)nterest Rate Edit: {choice_select}")
        
        elif choice_select == ('A' or 'a'):
            print(f"(A)ccount # Edit: {choice_select}")            
        
        else:
            print(f'{choices}')
            choice_select = input(  "available options: ")
            
        
main()