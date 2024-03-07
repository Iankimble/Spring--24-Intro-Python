# Async Assignment March 3rd, 2024. 

# Complete and solve the following prompts.
# Make sure to write down the clues and keywords you found.
# (Make sure to include your clues and keywords to recieve full credit)

# Commit and sync your work before the end of class. 
# This will count toward your class activity grade. 

# Prompt #1- Elevator Conditional Function Execercise.

# You have been hired by a architeture firm to assist 
# with developing their elevator system. They have asked 
# you to develop a function that will accept a user's input. 
# your program should ask the user to enter a floor number. 
# When an user enters a number they will be sent to a specific 
# floor in the building. If the user enters a floor number that does not
# exist, your program should inform the user that the floor they entered
# does not exist and to enter another number and to try agin.

# The architects have given you the following 
# lists of floors for their building:

# M = 'lobby'
# B = 'basement'
# R = 'rooftop'
# 1 = 'gym'
# 2 = 'restuarant'
# 3 = 'workspace'
# 4 = 'living quarters'

# keywords
# Functions- Instructions that only run when called.  
# Input()- lets your program accept data from the user. 
# string data type-
# variables- 
# Conditionals (if/ else/ elif)- allows us to run specific instructions based on
# specific conditions. 
# Elevator should take in floor number and send user to that floor. 

def elevatorProgram():
    floor = input('what floor would you like to go to? ')
    if floor == 'm':
        print('taking you to lobby.')
    elif floor =='b':
        print('you are going to the basement.')
    elif floor =='r':
        print('you are going to the rooftop.')
    elif floor =='1':
        print('you are going to the gym.')
    elif floor =='2':
        print('you are going to the restaurant.')
    elif floor == '3':
        print('you are going to the workspace.')
    elif floor =='4':
        print('you are going to the living quarters.')
    else:
        print("error: this floor number doesnt not exist. Try again.")

#elevatorProgram()

#___________________________________________________________

# Prompt # 2- Amusement Park Conditional Function

# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# keywords
# check for age hieght
# comparision operators less than, greater than- check for age and height. 
# we need to write a function
# we need parameters - height and age. 
# we need an error if data entered incorrectly.

def check_roller_coaster_eligibilty(age, height):
    if age >= 14 and height >= 5.2:
        print("You can get on roller coaster # 1. ")
    elif age >= 14 and height < 5.2:
        print("You can get on roller coaster # 2. ") 
    elif age < 14 and height < 5.2:
        print('You can ride roller coaseter # 3.')
    else:
        print('error; please try again. the information you provided may not be correct.') 

check_roller_coaster_eligibilty(5.9,10)


# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 

