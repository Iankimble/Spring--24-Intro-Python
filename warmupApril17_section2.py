# Warm up Tuesday April 17th, 2024.
# create a python file called warmup_april_17.py
# this will be graded 

import random

# 1. In your own words, explain the difference between 
# an Python For Loop and a Python While Loop.

# While loop - A special function that will repeat 
# instructions so long as the condition is true.

# For Loop - A special function used to 
# iterate over a sequence (group of data)

# 2. Create a loop that will iterate over a list of numbers.
# For evey number in your loop, it should multiply that number by 3. 

# Clue:
# We need to make a list with numbers in it.
# Iteratre over the numbers = for loop
# We need to multiply by 3

def numberList():
    numberList = [1,22,30,4555,56,610,10.293,7]
    for number in numberList:
        print(number * 3) 

# 3. Use the following code snippet below to create a guessing game 
# function. The code below will generate a random number for you. 
# You must write a loop that will ask the user to input their guess,
# if they guess incorrectly, the program will repeat itself and 
# ask the user to guess again. The program should 
# continue to ask them to guess until they've gotten it correctly.
# Once they guess the correct number the program will congratulate 
# them and the loop will stop. 
        
# generates a random number between 1 and 10
randomNumber = random.randint(1, 10) 
print(f'random number is now: {randomNumber}')
userInput = int(input('enter your guess: '))
while userInput != randomNumber:
    print('Incorrect guess. Try again: ') 
    userInput = int(input('Re-enter your guess: '))
    if userInput == randomNumber:
        print('Congrats! youve guessed correctly.')
        print('Ending loop.')

# While - so long as this is true...
# condition - if the user gets the answer wrong.
# = ask them to enter an answer again.
# if they get it right, congrats them and end loop. 

