#!/usr/bin/env python3
'''
Create a program that does the following:

1. Take the two lists provided and count the frequency of each word in each list.
2. Create a dictionary with the key equal to each unique word and count as the value.
3. Print off a list of words that are in both lists.
4. Print off a list of words that are in the first list and not the second.
5. Print off a list of words that are in the second list and not in the first.
'''
def histogram(s,show=0):
    d = dict()
    for c in s: 
        if c not in d: 
            d[c] = 1 #if none found -default to 1
        else:
            d[c] += 1 #count unique words if found
    if show == 0:
        print(d) #prints output of histogram
    return d

list1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
list2 = ['jack', 'be', 'nimble', 'jack', 'be', 'quick', 'jack', 'jumps', 'over', 'the', 'candlestick']
#instruction 1
#cleaned up the code and just wrote a function histogram(list, print results or not)
counts = dict()
histogram(list1) # use the function to count words for list1
histogram(list2) # use the function to count words for list2
#instruction 2 
counts = histogram(list1 + list2,1)  #opted to not show (print output))

set1 = set(list1)
set2 = set(list2)

#instruction 3, 4, 5 
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))