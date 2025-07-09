#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:50:22 2022

@author: skciller
"""

import numpy as np
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
        
    def build_tree(self, depth):
        '''
        Will fill out the tree to specified depth.
        
        Left child will be a deep copy, with the parent + 2
        Right child will be a shallow copy, and will be parent * 2
        Prints the tree at each iteration to show how it evolves.
        '''
        que = [self.root]
        level = 0
        print(f'Iteration {level}\n{self}\n')
            
        while level < depth and que:
            node = que.pop(0)
            
            left_value = node.value.copy()
            right_value = node.value.view()
            
            left_value += 2
            node.left = TreeNode(left_value)
            que.append(node.left)
            
            right_value *= 2
            node.right = TreeNode(right_value)
            que.append(node.right)
            
            level += 1
            print(f'Iteration {level}\n{self}\n')
            
    def __str__(self):
        '''
        Use BFS traversal to serialize tree level by level
        '''
        levels = []
        que = [self.root]
        while que:
            level = []
            for _ in range(len(que)):
                node = que.pop(0)
                level.append(list(node.value))
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            levels.append(str(level))
        return '\n'.join(levels)

t = Tree(np.array([1, 2, 3]))
t.build_tree(3)
print(f'Final tree\n{t}')
'''
Results (showing the tree's evolution):

Iteration 0
[[1, 2, 3]]

Iteration 1
[[2, 4, 6]]
[[3, 4, 5], [2, 4, 6]]

Iteration 2
[[2, 4, 6]]
[[6, 8, 10], [2, 4, 6]]
[[5, 6, 7], [6, 8, 10]]

Iteration 3
[[4, 8, 12]]
[[6, 8, 10], [4, 8, 12]]
[[5, 6, 7], [6, 8, 10], [4, 6, 8], [4, 8, 12]]

Final tree
[[4, 8, 12]]
[[6, 8, 10], [4, 8, 12]]
[[5, 6, 7], [6, 8, 10], [4, 6, 8], [4, 8, 12]]
''' 