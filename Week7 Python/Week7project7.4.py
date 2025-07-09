#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:47:05 2022

@author: skciller
"""

# add comments to the code

import csv

class Athlete:
    def __init__(self, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__team = team
        self.__noc = noc
        self.__games = games
        self.__year = year
        self.__season = season
        self.__city = city
        self.__sport = sport
        self.__event = event
        self.__medal = medal
        
        
    def get_age(self):
        try:
            if int(self.__age) > 0:
                return int(self.__age)
        except:
            pass
            return 0
        
    def get_weight(self):
        try:
            if int(self.__weight) > 0:
                return int(self.__weight)
        except:
            pass
            return 0    
    
    def get_height(self):
        try:
            if int(self.__height) > 0:
                return int(self.__height)
        except:
            pass
            return 0    
        

athlete_list = []
#athlete_weight = []
athlete_height = []
age_total = 0
weight_total = 0
height_total = 0

with open('athlete_events_short.csv', 'r', newline='') as athletes:
    reader = csv.reader(athletes)  
    
    header = next(reader)
    
    for line in reader:
        new_athlete = Athlete(line[1], line[2], line[3], line[4], line[5], line[6], 
            line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
        if line[3] != "NA":
            athlt_height = line[3]
        athlete_height.append(athlt_height)
        athlete_list.append(new_athlete)
        
for athlete in athlete_list:
    age_total += athlete.get_age()
    weight_total += athlete.get_weight()
    height_total += athlete.get_height()

        
print(" Average age in years for all olympians = ", age_total/len(athlete_list))
print(" Average weight for all olympians = ", weight_total/len(athlete_list))
print(" Average height for all olympians = ", height_total/len(athlete_list))
print(" Max height of all olypians = ", max(athlete_height), "cm")