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
'A parameter is a placeholder for data that goes inside of the function definition.'
'P= Parameter, P= Placeholder'

'A arguement is the actual data we pass into a function call.'
'Arguements= evidence, proof, actual data.'

# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# Syntax error - 
'A sytanx error occurs when the coding rules of' 
'python are not being followed properly'

# ~data~ Type error - 
'A type error occurs when data '
'types arent being used properly. '

# Name error - 
'A name error occurs when a variable does' 
'not exist or has not been defined.'

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?
'I would use the str()'
str(100) # '100'

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?
int(20) # 20

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 

# A. A variable must start with a letter or 
# the underscore character. A variable cannot start with a number.

# B. A variable name can only contain Alpha-numeric characters.

# C. A variable name is case senstive. 

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = , assignment operator. Assigns a value to a  variable.

# == , Comparison operator. Compares and check
# if values are the same/ equal. Including if its true. 
    
# !=, comparison operator. Compares and checks
# if values are NOT the same/NOT equal. Including if it is false


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

# Keyword 
# Comparison operator, Pass speed as arguement, create a function

def speedDetection(userSpeed):
    if userSpeed > 20 and userSpeed < 30:
        print('Shift to gear 1.')
    elif userSpeed > 31 and userSpeed < 40:
        print('Shift to gear 2.')
    elif userSpeed > 41 and userSpeed <70:
        print('Shift to gear 3.')
    elif userSpeed > 71:
        print('Shift to gear 1.')

speedDetection(74)

# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

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

#Keywords: function, 2 arguements, conditional statements.

def mealPlan(day,time): 
    if day == 'monday' and time =='morning':
        print('2 eggs and an apple')
    if day == 'monday' and time =='afternoon':
        print('bbq grilled chicken and broccoli')
    if day == 'tuesday' and time =='morning':
        print('oatmeal with strawberries and blueberries')
    if day == 'tuesday' and time =='afternoon':
        print('baked chicken with kale')
    if day == 'wednesday' and time =='morning':
        print()
    if day == 'wednesday' and time =='afternoon':
        print()
    if day == 'thursday' and time =='morning':
        print()
    if day == 'thursday' and time =='afternoon':
        print()
    if day == 'friday' and time =='morning':
        print()
    if day == 'friday' and time =='afternoon':
        print()

mealPlan('tuesday','morning')

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

def check_honors(overall_grade, sat_pass):
    if overall_grade > 85 and sat_pass:
        print('Congrats! You have made academic honors.')
    elif overall_grade > 85 and not(sat_pass):
        print('Congrats! You scored above 85%, however you did not make honors.')
    elif overall_grade < 85 and not(sat_pass):
        print('Please continue studying and try again next semester.')
    elif overall_grade < 85 or sat_pass:
        print('Congrats! you passed the SAT, however you did not make honors.')

check_honors(50, False)

# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

def checkTemperature(temperature):
    if temperature > 60 and temperature < 79:
        print('its warm outside.')
    elif temperature > 80:
        print("its hot outside.")
    elif temperature < 50:
        print("its cold outside.")
    elif temperature > 51 and temperature < 61:
        print('its not hot, but also not cold.')

checkTemperature(89)
