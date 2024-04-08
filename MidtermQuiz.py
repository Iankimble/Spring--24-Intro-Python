# Midterm quiz. 
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.

'A funcction parameter is a placeholder for data in a function.'
'P - parameter - placeholder'

# def userName (name):
#    print(f'Hello, my name is {name}')

'An arguement is the actual data we pass into a function.'
'Argument- evidence- proof- data.'
# userName('Ian')

# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# Syntax error - Program grammar errors. Speaking to the computer in 
# a way it doesn't understand. 

# ~ Data ~ Type error - An error when a data 
# type is not being used properly. 

# Name error - This error appears when a variable or a function is not defined.
# Appears when we didn't give a variable of a function any values. 

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?

'datacasting or casting - changing data types'
#str() # I would use the str function. 

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?
int() # I would use the int function

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 
# A variable name cannot start with a number.
# A variable name can follow the pascal, camel, or snake caseing. A variable name cannot have spaces.
# A variable name cannot be a python keyword/ reserved word. 

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = , Assignment operator. this will assign a variable to a value. 
variable = 'value'
# == , Comparison operator. Will evaluate if two values are the same.
true = 2 == 2 # these are the same so these values are true
# !=, Comparision operator. WILL evaluate if two values are NOT the same. 
false = 3 !=2

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# keywords
# Function, speed is the arguement I need to pass
# Need to write in conditional statements
# Check if the user is going over these numbers:
# < 20 = gear 1, < 30= gear 2 , < 40=gear 3, < 70 = gear 1

def speed_detector(speed):
    if speed > 20 and speed < 30: 
        print('shift to gear 1.')
    elif speed >= 30 and speed < 40: 
        print('shift to gear 2.')
    elif speed >= 40 and speed < 70: 
        print('shift to gear 3.')
    elif speed >= 70:
        print('shift to gear 1.')
    else: 
        print('turn on the car.')

# speed_detector(40)

# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# keywords and clues: need 2 arguements(day of week and time of day),
# need to write a function. 
# need conditional statements- depending on day 
# and time-this is will be your meal

def mealPlan(dayOfWeek, timeOfDay):
    if dayOfWeek == 'mon' and timeOfDay=='morning':
        print('2 eggs and an apple') 
    elif dayOfWeek == 'mon' and timeOfDay =='afternoon':
        print('bbq grilled chicken and broccoli')
    if dayOfWeek == 'tue' and timeOfDay=='morning':
        print('oatmeal with strawberries and blueberries') 
    elif dayOfWeek == 'tue' and timeOfDay =='afternoon':
        print('baked chicken with kale')
    if dayOfWeek == 'wed' and timeOfDay=='morning':
        print('fruit salad') 
    elif dayOfWeek == 'wed' and timeOfDay =='afternoon':
        print('curry goat with rice and cabbage')
    if dayOfWeek == 'thur' and timeOfDay=='morning':
        print('pancakes and turkey sausage') 
    elif dayOfWeek == 'thur' and timeOfDay =='afternoon':
        print('eggplant pasta')

# mealPlan('tue','afternoon')

# monday morning= 2 eggs and an apple
# monday afternoon= bbq grilled chicken and broccoli

# tuesday morning= oatmeal with strawberries and blueberries
# tuesday afternoon= baked chicken with kale

# wednesday morning= fruit salad
# wednesday afternoon= curry goat with rice and cabbage

# thursday morning= pancakes and turkey sausage
# thursday afternoon= eggplant pasta

# friday morning= steak and eggs
# friday afternoon= cheesburger and fries

# saturday morning= oatmeal
# saturday night= baked chicken with string beans

# sunday morning = oatmeal
# sunday night = steak and spinach

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# keywords and clue: function with arguements,
# conditional logic for if something is true
# logical operators to compare 2 conditions. 
# 85 > and sat= true - honors
# 85 < and sat= true - good, but not honors
# 85 > and sat= false - good, but not honors
# 85 < and sat= false - try again

def honorsCheck(grade, sat):
    if grade >= 85 and sat:
        print('Congrats, you have made honors.') 
    elif grade < 85 and sat:
        print('Congrats on your SAT, however you did not make honors.')
    elif grade >= 85 and not(sat):
        print('Congrats on your grade, however you did not make honors.')
    elif grade < 85 and not(sat):
        print('Please try harder. Youll do better next year.')
    else: 
        print("need more info")
# honorsCheck(60, False)

# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

#key words and clues: function, 
# conditional logical to check for different temps
# 60 > = warm outside.
# 80 > = hot outside.
# 50 < = cold outside. 
# 50 > = not hot, not cold. 

def temperatureCheck():
    temp= int(input("what is the temperature outside? "))    
    if temp < 50:
        print('Its cold outside.')
    elif temp >= 50 and temp < 60:
        print("Its not hot, but also not cold.")
    elif temp >= 60 and temp <80:
       print("Its warm outside. ")
    elif temp >= 80:
       print("Its hot outside. ")

temperatureCheck()