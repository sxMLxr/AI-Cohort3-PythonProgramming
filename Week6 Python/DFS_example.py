#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:28:53 2022

@author: skciller

for each node visited change color to white to gray, 
"verify" gray to black 
# create color dictionary to track this
calculate time taken for each node
#create trav_time dictionary
keep track of parent nodes 
# create parent dictionary

==== A
=== / \
== B<--C
= / \   \
 D   E-->F
"""


from queue import Queue

adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[],
}
         
color = {} # dictionary
parent = {} # dictionary
trav_time = {} # dictionary
dfs_traversal_output = [] # list

#initialize the above
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1] #assume if -1 not visited
    
#print(color) #confirm variables are initialized
#print(parent) #confirm variables are initialized
#print(trav_time) #confirm variables are initialized

time = 0
def dfs_util(u):  
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time+=1 #when we change color ensure we add to time
    
    for v in adj_list[u]:
        if color[v] == "W": # node not visited
            parent[v] = u   #assigne parent node and
            dfs_util(v)     #get child nodes (recursively)
    color[u] = "B"
    trav_time[u][1]= time
    time +=1
    
dfs_util("A")

print(f'DFS  T: {dfs_traversal_output}')
print(f'Parent: {parent}')
print(f'Trav T: {trav_time}')

for node in adj_list.keys():
    print(node, "->", trav_time[node])
    
    