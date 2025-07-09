"""
2.4 Local and Global variables (Group):

Write a program that will do the following:

    Generate a random number.
    The user will then input a number.
    The program will then tell the user if they are too high or too low.
    The user is prompted again, and the user enters a new number.
    This process repeats until the user guesses the correct number.
    The user can exit by guessing 0.
    Think modularly and use global and local variables.

"""
import random as rn

def number_guess(guess):
    global rand
    
    if guess > rand:
        print("Your guess is too high")
    elif guess < rand:
        print("Your guess is too low")
    else:
        print("nice work, the number was:",rand)
    

#instruction 1
rand = rn.randint(1,50)

def main():
#instruction 2
    while True:
        givemenumber = int(input("Guess what number im thinking of: ENTER 0 to end"))

        if givemenumber == 0 or givemenumber == rand:
            number_guess(givemenumber)
            break
        else:
            number_guess(givemenumber)

main()