#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:35:24 2022

@author: skciller
"""

import pandas as pd
import matplotlib.pyplot as mp

 # our data 
data = [["Australia", 2500, 2021],["Bangladesh", 1000, 2021],["England", 2000, 2021],["India", 3000, 2021],["Srilanka", 1500, 2021]]

 # import data into Panda dataframe, define columns 
dataFrame = pd.DataFrame(data, columns=["Team","Rank_Points", "Year"])
 
 # plotting multiple columns in a bar Graph 
dataFrame.plot(x="Team", y=["Rank_Points","Year" ], kind="bar", figsize=(10, 9))
 
 # displaying bar graph
mp.show()


