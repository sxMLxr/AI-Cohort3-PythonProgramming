# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:56:19 2022

Problem: Using the NC Lottery Cash 5 data, 
what is the distribution of winning numbers by ball? 
Graph the result (5 graphs).

Balls are numbered 1-43, choose 5 balls.

@author: jerobins
"""

import matplotlib.pyplot as plt

def import_lottery_data(filename):
    """
    Read the NC Lottery Cash 5 data file

    Parameters
    ----------
    filename : CSV
        RAW lottery data from website.

    Returns
    -------
    data - lottery data

    """
    data = []
    for i in range(5):
        data.append([])
    # data = [[],[],[],[],[]]
    
    with open(filename,'r') as fp:
        column_headers = fp.readline()
        
        for line in fp:
            # break up our CSV file
            entry_list = line.split(',')
            
            # don't go too far
            if len(entry_list) < 7:
                break
            
            for i in range(5):
                data[i].append(int(entry_list[i+1].strip('"')))
            
    return data

def graph_distribution(data):
    """
    Graph the number distribution by ball

    Parameters
    ----------
    data : list
        List of numbers in the set [1-43].

    Returns
    -------
    None.

    """
    plt.hist(data, bins=43, stacked=True)
    return

filename = "C:/Users/jerobins/Downloads/NCEL-Cash5.csv"

lottery_data = import_lottery_data(filename)
graph_distribution(lottery_data)

#for i in range(5):
#    graph_distribution(lottery_data[i])

    
    