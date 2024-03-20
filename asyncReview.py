
import random

# Async work Monday March 18th, 2024.

#1. Create a function that will count the number of characters
#  in a string that is passed in by a user. 
# The string value can be passed in either as 
# a paramter or by using the input function.
 
# You must be write down and explain how your program 
# works in complete sentences in order to get full credit. 

# keywords
# string, function, input, parameter

# what is the objective: function that count the number of 
# characters in a string.

def letterCount_Arg(word):
    print(len(word)) 

# letterCount_Arg('Ian')

def letterCount_input(): 
    word = input("type in a string")
    print(len(word)) 

# letterCount_input()

# 2. Use your notes, W3schools, and what we
# have learned in class to develop
# a simple rock, paper, scissors game. 
# Your game should allow the user to enter a letter
# that will represent the values rock, paper,
# and scissors (ex. r = rock, p = paper, s= scissors).

# EXTREMELY IMPORTANT NOTE
# at the top of you page write import random
# use the random.randrange(1,3) function to
# develop your random value logic
# for your rock, paper, scissor game. 

# Please describe the steps you took, 
# or if you weren't able to complete this activity,
# the steps you would've taken to solve 
# this problem in complete sentences. 
# This must be completed in order to get full credit.  

message = 'this is a comment.' 

'im writing some text.' 

# = assignment operator
# == comparison operator; checking if the values are the same. 

def winner_Amari(playerMove, computerMove):
    if  playerMove == computerMove:
        print("tie")
    elif playerMove == 'rock' and computerMove == 'paper':
        print('winner is computer.')
    elif playerMove == 'paper' and computerMove =='scissor':
        print('computer wins.')
    elif playerMove == 'scissor' and computerMove =='rock':
        print('computer wins.')
    else: 
        print('Please check your Function. There may be a condition missing.')

# winner_Amari('paper','scissor')
        
# OBJECTIVE: Create a rock,paper, scissor game where the
# computer randomly selects a value and compares it to the 
# user value.
        















gameValues= ['rock','paper','scissors']
randomValue = random.randrange(1,4)
# (randomValue)

def rpsGame():
    userValue = input("Please enter a value: r, p, or s: ")
    randomValue = random.randrange(1,4)
    
    if randomValue == 1:
        print('Computer Selected Rock')
        print(F'User selected {userValue}')
        if userValue == 'r':
            print('Tie game')
        elif userValue == 'p':
            print('user wins, paper beats rock.')
        elif userValue=='s':
            print('computer wins, rock beats paper.')
    
    if randomValue == 2:
        print('Computer Selected Paper')
        print(F'User selected {userValue}')
        if userValue == 'r':
            print('computer wins, paper beats rock.')
        elif userValue == 'p':
            print('tie game.')
        elif userValue=='s':
            print('user wins, scissors beats paper.')
    
    if randomValue == 3:
        print('Computer Selected Scissors')
        print(F'User selected {userValue}')
        if userValue == 'r':
            print('user wins, rock beats scissors.')
        elif userValue == 'p':
            print('computer wins, paper beats scissors.')
        elif userValue=='s':
            print('tie game.')

# rpsGame()