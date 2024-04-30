# Read the following prompt and answer the 3 questions

# Prompt

# You have been tasked as an engineer to develop a program that controls the lights in a small home.
# When the users uses the lighting control app that you are developing, they will have the ability to 
# turn lights on and off in the entire house. They can turn lights on and off based on the room in the home 
# individually or all the lights in the home at the same time. 
# there are 3 bedrooms, 1 kitchen, 2 bathrooms, a living room, a dining room, and a basement that all
# have lights and can all be manipulated with by using this app. 

# Questions

# 1. Based on the prompt you just read, what is the main goal(s) of the app that you are creating?
# What is the primary objective of your app? Please write your response using complete a complete sentence.

# Main goal(s):
# A. Making an app that can control the lights in the house,
# B. Having features that can control individual lights 
# by room or all the lights in the home simultaniously. 

# 2. What type of research would you need to do to help you develop this app? And are there 
# any questions that you can think of that could give you more context/ information
# that can help you develop this program that wasn't included ? 
# Please write your response in at least 4 complete sentences. 

# I would start my research with looking into smart home apps that already exist. 
# I would also need to research and understand how lights in a home are controlled.
# Next, I want to identify if there are any specific features that 
# I need to consider, as well as the type of hardware this program 
# will be running on.

# Additional Questions
# How large/ small are the rooms?
# How many people can use the app in one house hold? Do users 
# need to be authenticated (password)?
# can you have multiple home accounts?

# 3. Breakdown step- by- step how you would create this program in Python? Your steps do not have
# to be written in code and it does not have to use python keywords- rather your steps 
# should be explained in a way where an engineer can take the information and understand
# what they need to do.  Please be sure to write your steps in complete sentences. 

# Steps:
# 0. Draw/ sketch out what the app will like when in use. 
# 1. We need buttons and commands for each room in the house to turn the lights on and off. 
# 2. We need a way to represent each room in the house (list).
# 3. We need a function to turn lights on and off and tells us the state of the room. 
# off (parameters that will take the state of the room and room name).
# 4. Use logic for turning lights on and off based on user input. 

# Clue/ Keywords
# List Datatype : rooms in the house.
# Input : turning lights on and off.
# Function to wrap our code in. 
# Variable-datatype/ function for each room in house. 

def lightControl():
    house = ['unreachable','bedroom 1','bedroom 2','bedroom 3','kitchen','livingRoom','dinnergRoom','bathroom1','bathroom2','bathroom']
    print(house)
    print('Welcome to the Light Control App')
    print('_______________________')
    userAction = int(input('What would you like to do: press 1 for specific room, press 2 for all rooms: '))
    if userAction == 1:
        print('_______________________')
        print('Bedroom 1 = press 1')
        print('Bedroom 2 = press 2')
        print('Bedroom 3 = press 3')
        userRoom = int(input('Which Room would you like to control? '))
        print(f'Changing lights in the {house[userRoom]}')
        print(f'the {house[userRoom]} is on...')
        userAction = input('would you like to the light status in another room? press y for yes and n for no.')
    elif userAction == 2:
        print('Would you like to TURN ON or SHUT OFF all the lights? ')    

lightControl()
