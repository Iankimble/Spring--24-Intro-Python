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
# input() - pass data into a program.
# function - instructions; only runs when called.
# conditional - IF/ ELSE / ELIF
# elevator program/ system - user puts in floor data and goes to that floor; 
# if the floor doesnt exist, give an error (wrong floor/ try again)
# floors numbers -already got floor number above. 

def elevatorSytem():
    userFloor = input('Which floor would you like to go to? ')
    if userFloor == 'm':
        print("You are going to the Loby. ")
    elif userFloor =='b':
        print("You are going to the Basement. ")
    elif userFloor =='r':
        print("You are going to the Rooftop. ")
    elif userFloor == '1':
        print('You are going to the Gym. ' )
    elif userFloor == '2':
        print('You are going to the Restaurant. ' )
    elif userFloor == '3':
        print('You are going to the Workspace. ' )
    elif userFloor == '4':
        print('You are going to the Living Quarters. ' )
    else:
        print('Error: Sorry that floor doesnt exist. Try again. ')

#elevatorSytem()

#___________________________________________________________

# Prompt # 2- Amusement Park Conditional Function

# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# keywords 
# X parameter - data is passed inside of the function def. X
# X function - our instructions need to be wrapped in a function. X
# conditional statements ( if/ else/ elif).
# comparison operators - check if age and height. 
# match with our program requirements.
# integer datatype - age and float datatype for height.

def Rollercoaster(height, age):
    if height >= 5.2 and age >= 14: 
        print("You may get on roller coaster # 1. ")
    elif height >= 5.2 and age <14:
        print("You may get on roller coaster # 3.")
    elif height < 5.2 and age >= 14:
        print("You may get on roller coaster # 2.")
    elif height < 5.2 and age < 14:
        print("You may get on roller coaster # 3")
    else:
        print("Error: you may have typed something incorrectly. Try again.")

Rollercoaster(5.2,13)

# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 
