#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 07:48:13 2022

@author: skciller
"""

class employee:
    def __init__(self, fname, lname, dept, bldg):
        self.Efname = fname
        self.Elname = lname
        self.Edept = dept
        self.Ebldg = bldg
        
    def set_dept(self, dept):
            self.Edept = dept
         
    def set_bldg(self, bldg):
            self.Ebldg = bldg
    
    def set_lname(self, lname):
            self.Elname = lname
        
    def get_fname(self):
            return self.Efname

    def get_lname(self):
            return self.Elname

    def get_dept(self):
            return self.Edept
        
    def get_bldg(self):
            return self.Ebldg

    
class payscale(employee):
    def __init__(self, fname, lname, dept, bldg, Payscale, Pbonus, Pcontrib):
        employee.__init__(self, fname, lname, dept, bldg)
        self.Payscale = Payscale
        self.Pbonus = Pbonus
        self.Pcontrib = Pcontrib
        
    def set_Payscale(self, Payscale):
            self.Payscale = Payscale
        
    def set_Pbonus(self, Pbonus):
            self.Pbonus = Pbonus
        
    def set_Pcontrib(self, Pcontrib):
            self.Pcontrib = Pcontrib
        
class deptattrib(employee):
    def __init__(self, fname, lname, dept, bldg, Doffice, Dphn, Droom):
        employee.__init__(self, fname, lname, dept, bldg)
        self.Doffice = Doffice
        self.Dphn = Dphn
        self.Droom = Droom
    
    def set_Doffice(self, Doffice):
            self.Doffice = Doffice
    
    def set_Dphn(self, Dphn):
            self.Dphn = Dphn
    
    def set_Droom(self, Droom):
            self.Droom = Droom
        
class privateinfo(employee):
    def __init__(self, fname, lname, dept, bldg, socEMP, bdayEMP, yearsEMP):
        employee.__init__(self, fname, lname, dept, bldg)
        self.socEMP = socEMP
        self.bdayEMP = bdayEMP
        self.yearsEMP = yearsEMP
    
    def set_socEMP(self, socEMP):
            self.socEMP = socEMP
    
    def set_bdayEMP(self, bdayEMP):
            self.bdayEMP = bdayEMP
    
    def set_yearsEMP(self, yearsEMP):
            self.yearsEMP = yearsEMP
        
    def get_socEMP(self):
            return self.socEMP

    def get_bdayEMP(self):
            return self.bdayEMP
            
    def get_yearsEMP(self):
            return self.yearsEMP

def main():
    staff = []
    
    lastn1 = "l1-name" 
    firstn1 = "f1-name"
    dept1 = "biology"
    bldg1 = 101
    employee1 = employee(firstn1, lastn1, dept1, bldg1)
    
    lastn2 = "l2-name"
    firstn2 = "f2-name"
    dept2 = "math"
    bldg2 = 102
    employee2 = employee(firstn2, lastn2, dept2, bldg2)
   
    lastn3 = "l3-name"
    firstn3 = "f3-name"
    dept3 = "language"
    bldg3 = 103
    employee3 = employee(firstn3, lastn3, dept3, bldg3)
    staff = [employee1,employee2,employee3]
    
    print("==employee list==")
    for i in range(len(staff)):
        print(staff[i].Efname, staff[i].Elname, staff[i].Edept, staff[i].Ebldg )
    
    print("\n==add some payscale info==")
    employee1P = payscale(firstn1, lastn1, dept1, bldg1, "Mgmt", "annually", "5%")
    employee2P = payscale(firstn2, lastn2, dept2, bldg2, "Sup", "annually", "5%")
    employee3P = payscale(firstn3, lastn3, dept3, bldg3, "employee", "annually", "5%")
    
    print("==add some dept info==")
    employee1D = deptattrib(firstn1, lastn1, dept1, bldg1, "2nd floor", "x1203", "rm: 205")
    employee2D = deptattrib(firstn2, lastn2, dept2, bldg2, "1st floor", "x1204", "rm: 105")
    employee3D = deptattrib(firstn3, lastn3, dept3, bldg3, "2nd floor", "x1205", "rm: 204")
    
    print("==add some private employee info==\n")
    employee1I = privateinfo(firstn1, lastn1, dept1, bldg1, "1234", "12121975","5 yrs")
    employee2I = privateinfo(firstn2, lastn2, dept2, bldg2, "7896", "01121992","4 yrs")
    employee3I = privateinfo(firstn3, lastn3, dept3, bldg3, "4561", "02021978","5 yrs")
    
    print(f"Employees Fname, Lname: SOC : years")
    print(employee1.get_fname(), employee1.get_lname(), employee1I.get_socEMP(), employee1I.get_yearsEMP())
    print(employee2.get_fname(), employee2I.get_lname(), employee2I.get_socEMP(), employee2I.get_yearsEMP())
    print(employee2.get_fname(), employee3I.get_lname(), employee3I.get_socEMP(), employee3I.get_yearsEMP())
        
    print(f"\nEmployee last name change")
    employee1.set_lname("l1-l2name")
    employee2.set_lname("l2-l1name")
    employee3.set_lname("l3-name Jr.")
          
    print(f'{employee1.get_lname()}, {employee1.get_fname()}')
    print(f'{employee2.get_lname()}, {employee2.get_fname()}')
    print(f'{employee3.get_lname()}, {employee3.get_fname()}')
    
main()