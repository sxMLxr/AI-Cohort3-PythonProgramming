#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:26:32 2022

@author: skciller
"""

## 7.5 Exception handling in files and try, except blocks (Follow):  
'''
**Learning Objectives:**

    1. Understand how to catch errors in file handling.
    2. Understand how to deal with errors in file handling.
    3. Understand why it is necessary to handle file issues.
    
    # add comments to the code
'''
def main():
    total = 0.0
    number = 0.0
    counter = 0
    
    filename = 'numbers.txt'
    
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