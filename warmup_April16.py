# Warm up Tuesday April 17th, 2024.
# create a python file called warmup_april_17.py
# this will be graded 

import random

# 1. In your own words, explain the difference between 
# an Python For Loop and a Python While Loop.

# FOR loop = iterates over sequence of items.  

# WHILE loop = repeatedly runs a set of instructions 
# so long as a condition is true. 

# 2. Create a loop that will iterate over a list of numbers.
# For evey number in your loop, it should multiply that number by 3. 

# Clues and keywords = loop; for loop to iterate over numbers.
# everytime or loop lands on a number- multiply by 3. 
# list of numbers

def numberLoop():
    numbersList = [1,2,3,4,5,6,7]
    for number in numbersList: # for every item in this list ...
        print(number *3) # multiply that item by 3...

# 3. Use the following code snippet below to create a guessing game 
# function. The code below will generate a random number for you. 
# You must write a loop that will ask the user to input their guess,
# if they guess incorrectly, the program will repeat itself and 
# ask the user to guess again. The program should 
# continue to ask them to guess until they've gotten it correctly.
# Once they guess the correct number the program will congratulate 
# them and the loop will stop. 

# generates a random number between 1 and 10

# clues
# we're using a while loop- program will repeat itself; If 
# the number is not the correct guess.
# we'll need to create a function to store it. 
# we'll use the input function to take the users guess.

def guessingGame():
    randomNumber = random.randint(1, 10)
    i = int(input('please guess a number:'))

    while i != randomNumber:
        print('Incorrect guess. Try again.')
        i = int(input('Please guess another number: '))
        if i == randomNumber:
            print('Congrats! Youve won the game.')
