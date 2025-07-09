##==== code Version3
import numpy as np

new_array = []
new_array2 = [] 

def time_sec(x):
    def __init__(self):
        self.x = x
    hrs, mins, secs = x.split(":")
    return float(hrs)*3600 + float(mins)*60 + float(secs)

ironman_data = np.genfromtxt('2019 Ironman World Championship Results.csv', 
                             delimiter = ',', dtype = 'str', skip_header=1)

numeric_only = ironman_data[:,[6,7,8,9,13,14]]
numeric_only = np.where(numeric_only=='', '0:0:0', numeric_only)
numeric_only = np.where(numeric_only=='DNS', '0:0:0', numeric_only)
numeric_only = np.where(numeric_only=='DNF', '0:0:0', numeric_only)
numeric_only = np.where(numeric_only=='DQ', '0:0:0', numeric_only)
numeric_only = np.array(numeric_only)
numeric_only2 = np.array(numeric_only)

#print(numeric_only)

for elements in numeric_only:
    #e10,e11,e12,e13,e14 = elements[10], elements[11], elements[12], elements[13], elements[14]
    e10,e11,e12,e13,e14,e15 = time_sec(elements[0]), time_sec(elements[1]), time_sec(elements[2]), time_sec(elements[3]), time_sec(elements[4]), time_sec(elements[5])
    new_array.append([e10,e11,e12,e13,e14,e15])

#print(np.shape(new_array))
#print(new_array)

## fix the usage of lambda function == FIXED!!!
for elements in numeric_only2:
    e10,e11,e12,e13,e14,e15 = elements[0], elements[1], elements[2], elements[3], elements[4], elements[5]
    calc_array = [e10,e11,e12,e13,e14,e15]
    result_array = list(map(lambda x:time_sec(x),calc_array))
    new_array2.append(result_array)

#print(np.shape(new_array2))
#fixed it !!  ensure size is same ... 

#confirmed
#print(new_array2)

#meanof0 = np.mean(result[:,0], axis=0) #prints first column only
meanof0 = np.mean(new_array2, axis=0)  #calc mean of all columns 
#==result.mean(axis=0)  same as above
print()
print(f' Mean of:\n{meanof0}\n')
medianof0 = np.median(new_array2, axis=0)  #calc mean of all columns 
print(f' Median of:\n{medianof0}\n')
stdof0 = np.std(new_array2, axis=0)    #calc for all columns
##result.std(axis=0)  same as above
print(f' Std:\n{stdof0}\n')
