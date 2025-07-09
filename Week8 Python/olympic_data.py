#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:25:39 2022

@author: skciller
""" 
import pandas as pd

def Athletes(self, name, sex, age, height, weight, team, NOC, games, year, season, city, sport, event, medal):
    
    def __init__(self):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__team = team
        self.__NOC = NOC
        self.__games = games
        self.__year =  year
        self.__season = season
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

    def get_all(self):
        return 'self.__name,self.__sex,self.__age,' \
                'self.__height,self.__weight,self.__team,self.__NOC,self.__games,' \
                'self.__year, self.__season, self.__sport, self.__event, self.__medal'



df = pd.read_csv('../Week7 Python/athlete_events_short.csv', skiprows=0, index_col=0)
reader = df.head()

'''
    ## multiple ways to read columns
#print(df.head(0))
#print(reader.columns)

    ##print all to output
#print(reader)

    ##read data single line
#print(df.head(1))

    ##print a column
#print(df['Name'])
#print multiple columns  
#print(df[['Name','Height','Weight','Medal']])

    ##print a row      #iterate through rows using df
#print(df.iloc[1])     # for index, row in df.iterrows():
#print(df.iloc[4:6])   #    print(index,row['Name'])

    #print a specific value
#print(df.iloc[4:6,0])

    ##list only variables of your choosing
#print(df.loc[df['Event']== "Speed Skating Women's 500 metres"])

    ## using describe to get stats
#print(df.describe())

    ## sort values by name
# df.sort_values('Name') 
# or df.sort_values('Name', ascending=True)
# or df.sort_values('Name', ascending=False)
# or by multiple rows 
    #print(df.sort_values(['Age','Name', 'Games']))
# sort first row ascending, and second decending
    #df.sort_values(['Age','Name', 'Games'], ascending=[1,0,0]).head(5))
# sort first row ascending, and second decending and print out the first 5 rows
#new_df = df.sort_values(['Age','Name', 'Games', 'Year'], ascending=[1,0,0,0]).head(5)

#save to csv, or excel 
    #df.to_csv('modified', index=False)  #save without index row
    #df.to_csv('modified', index=False, sep='\t')  #save without index row
    #df.to_excel('modified', index=False)  #save without index row
    
### FILTER DATA ###
    # by two column variables
    #example: df.loc[ () & () ]
#df.loc[(df['Season'] == "Summer") & (df['Year'] == "1988")]
    
        #search with starts with #df[df.index.str.startswith('h', na=False)]
    #new_df = df.loc[(df['Season'] == "Summer") & (df['Year'] == 2008) & (df['Event'].str.startswith('A', na=False))]
        #search with ENDS WITH 
        #df[df.index.str.endswith('k', na=False)]
    #print(new_df)

## remove index of our output
    #Ex: new_df = df.loc[(df['Season'] == "Summer") & (df['Year'] == 2008) & (df['Event'].str.startswith('A', na=False))]
    # new_df .reset_index(drop = true, inplace=True) or
    ## new_df = new_df.reset_index(drop=True)
    # new_df

#change values for some conditions
    #df.loc[df['Sex']=='M', ['Sex']]= 'Human M'
    #df.head(10)

### Aggregate Statistics groupby function
#new_df = df.groupby(['Name','Season','Year','City']).mean().sort_values('Year', ascending=True)
#new_df = df.groupby(['Name','Season','Year']).mean().sort_values('Year', ascending=True)
#new_df = df.groupby(['Sport','Name','Season','Year']).mean().sort_values('Sport',ascending=True)
#df.groupby().mean()  ####mean is the average
##df.groupby().sum()
##df.groupby().count()
###df.groupby(['FEILD1','FEILD2']).count()['FEILD']

## create new dataframe and add df.columns 
##perform groupby

new_df = pd.DataFrame(columns=df.columns)
    for df in pd.read_csv('file', chunksize=5):
        results = df.groupby(['Season']).count()
        
        new_df = pd.concat([new_df, results])
'''
meanofw = df.groupby(['Weight']).mean()
#grab mean of weight of 47
print(f'Means of Persons age 47:\n{meanofw.loc[47,:]}')
#print(meanofw2)

AVERAGEofw = df['Weight'].sum()/df['Weight'].count()
meanofWght = df['Weight'].mean()
Sumofw = df['Weight'].sum()
maxage = df["Age"].max()
minage = df["Age"].min()
aveage = df['Age'].mean()

print(meanofw)
print(Sumofw, AVERAGEofw, maxage, minage, aveage, )

