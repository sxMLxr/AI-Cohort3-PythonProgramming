# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E','F'), ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G'), ('Q', 'D')])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size = 50)
nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
nx.draw_networkx_labels(G, pos)
plt.show()

print("Downstream Edges of 'B' (just example)-->")
print(list(nx.dfs_edges(G,'B')))

print(list(nx.dfs_parent))
