#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:15:13 2022

@author: skciller
"""

class savings:
    def __init__(self, acctnumber, interestrt, balance):
        self.__acctnumber = acctnumber
        self.__interestrt = interestrt
        self.__balance = balance
    
    def set_acctnumber(self, acctnum):
        self.__acctnumber = acctnum
    
    def get_acctnumber(self):
        return self.__acctnumber
    
    def set_interestrt(self, intrate):
        self.__interestrt = intrate
        
    def get_interestrt(self):
        return self.__interestrt
        
    def set_balance(self, balnc):    
        self.__balance = balnc
    
    def get_balance(self):
        return self.__balance
    
    def print_object(object_name):
        print(f'Acct #:    {object_name.__acctnumber}')
        print(f'Int rate:  {object_name.__interestrt}')
        print(f'Balance    {object_name.__balance}')  
        print(f' ')  
        
        
class cd(savings):
    def __init__(self, acctnumber, interestrt, balance, matredate):
        savings.__init__(self, acctnumber, interestrt, balance)
        self.__maturedate = matredate
    
    def set_matdate(self, mdate):
        self.__maturedate = mdate
        
    def get_matdate(self):
        return self.__maturedate
    
    
 
def main():
    primaryacct = [] 
    
    Acct_456123 = savings(456123, .15, 1023) 
    Acct_123456 = savings(123456, .10, 100)
    Acct_654987 = savings(654987, .11, 100)
    
    primaryacct = [Acct_456123, Acct_123456, Acct_654987]
    
    print("Account Number:  ", Acct_456123.get_acctnumber())
    print("   interest rt:  ", Acct_456123.get_interestrt())
    print("   balance    :  ", Acct_456123.get_balance())
  
    print("Account Number:  ", Acct_123456.get_acctnumber())
    print("   interest rt:  ", Acct_123456.get_interestrt())
    print("   balance    :  ", Acct_123456.get_balance())
    
    print("Account Number:  ", Acct_654987.get_acctnumber())
    print("   interest rt:  ", Acct_654987.get_interestrt())
    print("   balance    :  ", Acct_654987.get_balance())
    print(" ")

    primaryacct[0].set_interestrt(.20)
    primaryacct[1].set_interestrt(.21)
    primaryacct[2].set_interestrt(.15)
    
    primaryacct[0].set_balance(10000)
    primaryacct[1].set_balance(10000)
    primaryacct[2].set_balance(10000)
    
    primaryacct[0].print_object()
    primaryacct[1].print_object()
    primaryacct[2].print_object()
    
    primaryacct[0] = cd(primaryacct[0].get_acctnumber(), primaryacct[0].get_interestrt(), primaryacct[0].get_balance(), "10-2-2022")
    primaryacct[1] = cd(primaryacct[1].get_acctnumber(), primaryacct[1].get_interestrt(), primaryacct[1].get_balance(), "11-2-2022")
    primaryacct[2] = cd(primaryacct[2].get_acctnumber(), primaryacct[2].get_interestrt(), primaryacct[2].get_balance(), "12-2-2022")
    
    print(primaryacct[0].get_matdate())
    print(primaryacct[1].get_matdate())
    print(primaryacct[2].get_matdate())
    
    '''
    choices= ["(S)avings", "(B)alance", "(I)nterestRate", "(A)cctnumber"]
    while True:
        i = 0 
        accts = input(f'Enter a new acct number "(Q to quit)" ')
        if accts != ("q" or "Q"):
            intrate = input('  Current interest rate: ')
            startbalance = input('  Starting balance: ')
            accts = savings(accts, intrate, startbalance)
            listaccts.append(accts)
            primary
            i+=1
        else:
            break
        
    
    if (len(listaccts) == 0):
        print(f"No Accts created")
        return 0
        
    print(f'{choices}')
    choice_select = input("  available options: ")
    i=0
    for la in listaccts:
        print(f"accts available: [{i}]: ", la.get_acctnumber())
        i+=1
    
    for lb in accts:
        print(f"accts available: [{i}]: ", lb.get_acctnumber())
        i+=1
        

    while choice_select != ("Q" or 'q'):
            
        if choice_select == ('S' or 's'):
            for la in listaccts:
                print(f"accts available: [{i}]: ", la.get_acctnumber())
            activeacct = int(input(f"(S)avings Account to Edit: "))
            choice_select == " "
        
        elif choice_select == ('B' or 'b'):
            activeacct.get_balance()
            print(f"(B)alance Account: {choice_select} Enter new amt: ")
            balnc = input(f"==Balance Change: for acct {activeacct}" )
            listaccts[activeacct].set_balance(balnc)
            choice_select == " "
            
        elif choice_select == ('I' or "i"):
            print(f"==(I)nterest Rate Edit: {choice_select} ")
            choice_select == " "   
        
        else:
            if choice_select == ('A' or 'a'):
                print(f"==(A)ccount # Edit: {choice_select} ")            
            
        choice_select == " "
        print(f'{choices}')
        choice_select = input(  "available options: ")
        '''    
        
main()