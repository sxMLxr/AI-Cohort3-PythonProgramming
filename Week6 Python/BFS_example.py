# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from queue import Queue
"""
adj_list = {
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"],
    }
"""

adj_list = {
    "0":["1","2"],
    "1":["0","2"],
    "2":["0","1","3","5"],
    "3":["2","4"],
    "4":["3"],
    "5":["2"]
}


#BFS code
visited = {}
level = {}  # distance dictionary
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1 #-inf
    
#print (visited)  testing the effectiveness of above code
#print (level)
#print (parent)

s= "0"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)
            
print(f'bfs_traversal_output: {bfs_traversal_output}')

## shortest distance of all nodes from source code
# print(level) for entire list
# print(level["G"]) for distance of G
print(f'shortest distance from level: 4  {level["4"]}')

# shortest path from any node from source node
v = "4"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(f'path: {path}')

print(f'parent: {parent}')