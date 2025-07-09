#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 08:49:53 2022

@author: skciller
"""
class person:
    def __init__(self, name, addr, phnnum):
        self.name = name
        self.addr = addr
        self.phnnum = phnnum
    
    def get_name(self):
        return self.name
        
    def get_addr(self):
        return self.addr
        
    def get_phnnum(self):
        return self.phnnum
    
    def set_name(self, name):
        self.name = name
        
    def set_addr(self, addr):
        self.addr = addr
        
    def set_phnnum(self, phnnum):
        self.phnnum = phnnum
        
    
    
class customer(person):
    def __init__(self, name, addr, phnnum, cust_num, purmnt):
        super().__init__(name, addr, phnnum)
        self.cust_num = cust_num
        self.purmnt = purmnt

    def get_cust_num(self):
        return self.cust_num
        
    def get_purmnt(self):
        return self.purmnt
    
    def set_cust_num(self, cust_num):
        self.cust_num = cust_num
        
    def set_purmnt(self, purmnt):
        self.purmnt = purmnt

   
    
def main():
    customer0 = customer("john","1456 east st.","1019758462","123456","1000")
    customer1 = customer("jake", "123 lane st", "4561237894", "456123", "1000.00")
    customer2 = customer("jane", "456 forest st", "1237894564", "789321", "100.00")
    print("customer info:\n")    
    print_info(customer0)
    print_info(customer1)
    print_info(customer2)




def print_info(customerinfo):
    print(f'\nname: {customerinfo.get_name()}\naddr: {customerinfo.get_addr()}\nphnnum: {customerinfo.get_phnnum()}')
    print(f'customer#: {customerinfo.get_cust_num()}\npaymentinfo: {customerinfo.get_purmnt()}\ncustomerinfo: {customerinfo.get_cust_num()} ')
    

if __name__ == "__main__":
     main()
