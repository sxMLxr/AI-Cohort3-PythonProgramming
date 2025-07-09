#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:44:33 2022

@author: skciller

Write a program that will do the following:

1. Create an employee class.
2. The employee class should have attributes name and employee ID
3. Create at least three employee objects.
4. Push the objects into a queue and stack.
5. Remove the employees from the stack and queue until both are empty.
6. Print the orders of both employee objects. 

"""

class employee:

    def __init__(self, name, empID):
        self.__name = name
        self.__empID = empID

    def get_name(self):

        print(f'{self.__name} {self.__empID}')

def main():    

    queue = []

    id_1 = employee("jack", "id_135745")

    id_2 = employee("jill", "id_745654")

    id_3 = employee("john", "id_456745")

    queue.append(id_1)
    queue.append(id_2)
    queue.append(id_3)

    print("Initial queue")
    queue[0].get_name()
    queue[1].get_name()
    queue[2].get_name()


    print("\nElements dequeued from queue")


    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print("\nQueue after removing elements")
    print(queue)
    
    
if __name__ == "__main__":
    main()