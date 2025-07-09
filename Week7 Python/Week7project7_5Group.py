#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:26:32 2022

@author: skciller
"""

## 7.5 Exception handling in files and try, except blocks (Follow):  
'''
**Learning Objectives:**

    1. Load the numbers.txt text file by taking input from the user.
    2. Add several random numbers to the file as input from the user.
    3. Read in all the numbers in the file.
    4. Encapsulate both reads and writes in separate try exception blocks
    5. Find the average of all the numbers.
    
'''
def main():
    total = 0.0
    number = 0.0
    counter = 0
    
    filename = 'numbers.txt'
    
    list_of_numbers = []
    for i in range(4,-1,-1):
       list_of_numbers.append(int(input(f'I need {i+1} random numbers: ')))
    
    ''' Write to an existing file, add numbers  code sample:    
    infile = open(filename, 'r')  #read file
    lines = infile.readlines()
    infile.close()

    '''
    try:
        outfile = open(filename, 'w')  # output using write function
        for lon in list_of_numbers:
            outfile.write(str(lon)+"\n")

    except IOError:
        print('An error occurred while trying to write to the file.')
        error_flag = 1
    except ValueError:
        print('Non-numeric data found in the file')
        error_flag = 1
    except: 
        print('An error occurred')
        error_flag = 1
    else:
        print("File write succesful.")
        error_flag = 0
    finally:
        if error_flag == 1:
            print("An error occured, please fix it.")
        else:
            print("No errors occured, good job.")
        outfile.close()

                  
    ''' Open the file we wrote to 
    '''    
    
    try:
        infile = open(filename, 'r')

        for line in infile:
            counter = counter + 1
            number = float(line)
            total += number
        
        #infile.close()

        average = total / counter
        print (f'Average: {average}')

    except IOError:
        print('An error occurred while trying to read the file.')
        error_flag = 1
    except ValueError:
        print('Non-numeric data found in the file')
        error_flag = 1
    except: 
        print('An error occurred')
        error_flag = 1
    else:
        print("File loaded succesfully.")
        error_flag = 0
    finally:
        if error_flag == 1:
            print("An error occured, please fix it.")
        else:
            print("No errors occured, good job.")
        infile.close()
        
                     
if __name__ == '__main__':
    main()