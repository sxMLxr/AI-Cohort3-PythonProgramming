import numpy as np

ironman_data = np.genfromtxt('2019 Ironman World Championship Results.csv', 
                             delimiter = ',', dtype = 'str', skip_header=1)

numeric_data = ironman_data[:, [6, 7, 8, 9, 10, 11, 12, 13, 14]]

numeric_data = np.where(numeric_data=='', '0:0:0', numeric_data)
numeric_data = np.where(numeric_data=='DNF', '0:0:0', numeric_data)
numeric_data = np.where(numeric_data=='DNS', '0:0:0', numeric_data)
numeric_data = np.where(numeric_data=='DQ', '0:0:0', numeric_data)

def ironman_times(times):
    #t = times.split(':')
    #if t[0] == '':
    #    seconds = 0
    #else:
    if len(times) > 2:
        hrs, mins, secs = times.split(':')
        return float(hrs)*3600 + float(mins)*60 + float(secs)
    else:
        return 

    #seconds = 3600 * int(t[0]) + 60 * int(t[1]) + int(t[2])
    #return seconds
    
    

vfunc = np.vectorize(ironman_times)
new_array = vfunc(numeric_data)

print (new_array)

mean = np.mean(new_array, axis=0)
print(f'Mean times are: {mean}')


