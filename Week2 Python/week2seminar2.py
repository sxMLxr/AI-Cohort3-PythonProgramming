# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:56:19 2022

Problem: Using the NC Lottery Cash 5 data, 
create a list, by play, of the average value
of the 5 balls. Graph the result.

Balls are numbered 1-43, choose 5 balls.

May 15, 2014 39 -> 41
Nov 4, 2018  41 -> 43

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

def calculate_average(data):
    """
    Calculate average ball value by play.

    Parameters
    ----------
    data : List of lists by ball

    Returns
    -------
    List - average ball values.

    """
    average = []
    
    for x in range(len(data[0])):
        avg = (data[0][x] + data[1][x] + data[2][x] + data[3][x] + data[4][x]) / 5
        average.append(avg)
        
    return average

def graph_average(data):
    """
    Line graph of supplied data.
    
    Parameters
    ----------
    data : List of floats

    Returns
    -------
    None.
    """
    plt.plot(data)
    return


filename = "C:/Users/jerobins/Downloads/NCEL-Cash5.csv"

lottery_data = import_lottery_data(filename)

ball_average = calculate_average(lottery_data)

graph_average(ball_average)
#graph_distribution(lottery_data)

#for i in range(5):
#    graph_distribution(lottery_data[i])

    
    