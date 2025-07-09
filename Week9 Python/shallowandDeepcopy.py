#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 07:55:58 2022

@author: skciller
"""

import copy
import numpy as np


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def PrintTree(self): 
        #left 
        if self.left:
            self.left.PrintTree()
        print( self.data ,end=" "),  #corrected formatting added space to print single line
        #right
        if self.right:
            self.right.PrintTree()
           
    def addnode(self, ldata, rdata):
        if self.data:
            if ldata:
                if self.left is None:
                    self.left = Node(data)
                    #find first node, root
                else:
                    self.left.addnode(data)
            elif rdata:
                if self.right is None:
                    self.right = Node(data)
                    #find first node, root
                else:
                    self.right.addnode(data)
            else:
                self.data = data

    def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
         return res



#add nodes with requirement child should be two times value of parent
#next numeral should be root *n

getroot = int(input('I need a root number to begin with: '))
getdepth = int(input('Tree depth (3 is a good start):  '))

root = Node(getroot)
#RootNumber = root.PrintTree()

data = np.arange(getroot,getroot*(getdepth+3),getroot)
print(data, end=" ")

data1 = data.copy()
data2 = data.copy()
data2 *= 2
data3 = data.copy()
data3 *= 4
print()
print(data2, end="\n")
print(data3, end="\n")


#clean data find duplicates and remove
#need afunction to do the follow
root = Node(1)
root.addnode(2,3)

"""
root = Node(int(data1[0]))
root.addnode(int(data1[1]))
root.addnode(int(data1[2]))
"""

#reset root to 0
root = Node(1)

root.PrintTree()
print(root.inorderTraversal(root))        