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

# A: The main goal of this application is to allow 
# users to control all the lights in their home. 

# 2. What type of research would you need to do to help you develop this app? And are there 
# any questions that you can think of that could give you more context/ information
# that can help you develop this program that wasn't included ? 
# Please write your response in at least 4 complete sentences. 

# My research process would begin with looking into apps that
# exist that do similar things,  such as smart home apps.
# As I go deeper into researching already existing apps,
# I'll look into how these apps connect to the physical lights.
# I'll also look into the develop process of pre-existing smart home apps to see
# if their is a design process that I can replicate in mine. 

# 3. Breakdown step- by- step how you would create this program in Python? Your steps do not have
# to be written in code and it does not have to use python keywords- rather your steps 
# should be explained in a way where an engineer can take the information and understand
# what they need to do.  Please be sure to write your steps in complete sentences. 

# iterator / iterative - means to repeat

# Steps: 
# step #1. Conduct research into pre-existing smart applications, 
# to get better understanding of how these types of apps work.

# step #2. I would do a basic diagram of how I would like my app to work. 
# These sketehes would show how the app looks and works. 

# Coding steps. 
# step #3A. From my drawings, I would analyze and write down what happens when 
# a user hits a button.
# step #3B. Show a button for each light in the house 
# (br1, br2, ktch, lvng rm...)
# step #3C. Each button should show the room light status; 
# whether its on or off. 
# step #3D. When a user hits the button by name, 
# the light in that room should switch.

# Clues and Keywords 
# - Conditional Statements
# - Function
# - Boolean
# - Input 
# - String Data Type
#  - Loop 

def lightControls():
    livingRoom = False
    dinningRoom =  False
    kitchen = False
    basement = False
    bedroom1 = False
    bedroom2 = False
    bedroom3 = False
    house =[livingRoom,dinningRoom,kitchen,basement,bedroom1,bedroom2,bedroom3]
    print(f'here is your list value: {len(house)}')

    unserInput = int(input('please enter a room key: 0 is living room, 1 is dinning room...'))
    
    #for room in house:
    if  unserInput == house[unserInput]:
        print('switching light...')
        house[unserInput] = True
    print(house)
              
lightControls()
