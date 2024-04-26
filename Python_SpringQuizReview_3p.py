# What is a computer program?
# Digital INSTRUCTIONS for computers to execute.

# What is Syntax? 
# Computers language RULES. 

# example of a python function and its syntax (format rules)
def myFunction():
    print('here are some intstructions...')
# myFunction()

# example of a javascript function and its syntax(format rules)
#function myFunction(){
#    console.log('here are some instructions... ')
#}
# myFunction()

# What are Data types?
# The fundamental building blocks of a programming language. 
# Think of it as our programming languages alphabet. 
'Name' # string data type
10 # integer data type
1.00 # float data type
True # boolean data type
var= [] # list data type
# print(type(1))

# What is data casting?
# The process of changing a data type into another data.

# Ex. changing a str into an int. 
def multiply():
    # This data will be treated a string
    number = input('Enter a number to multiply: ') 
    # The int() function transforms a string into a integer. 
    result = int(number) * 3
    print(result)

# What are Python Operators? What do they do?
# operators perform actions on data. 

action_1 = 2 / 2 # we are doing division. 
# Division is apart of the  arthmatic family of operators

action_2 = 'Ian ' * 10 # we are doing multiplication
# Multiplication is apart of the arthmatic family of operators
# this is an exception. 
#print(action_2)

action_3 = '3oh#4o89hf#' == '3oh#4o89hf#' # we are comparing to pieces of data.
# this is the "is the same/equal" operator and is 
# in the comparison operator family.09

# = (One Equal Sign) - assignment operator, 
# == (Two Equal Signs) - comparison operators, same as/ equal to.
# != (Exclaimation Equal Sign) - comparision, not the same/ not equal.

# What is a function?
# A set of instructions that we can STORE AND SAVE for later, and CALL we need it.
# multiply()

# What are lists?
# A data type that lets us store collections of data inside of a variable. 

randomList =[ 'and',0,122, 12.2422, True, ['Before','after',10], action_1, multiply, ]
print(randomList)

# Why are lists important in Python?
# Lists help us store and save data. 
# Lists allows us to also organize data. 

goldT = [] 
silverT = []
bronzeT =  []

members = [goldT,silverT,bronzeT]

# What is a Loop? 
# A block of code that repeats

# What are For loops, and While loops, 
# and what is the difference between the two?

# For loop - iterating (repeating ) instructions over a collection of data.
# ex. of a for loop - Searching for someone's name on a social media site. 
 
# While loop - iterate (repeat) instructions so long as somthing is true.  
# ex. of a while loop - a video game where so long as the players health is not zero,
# let them keep playing. 
# ex. street lamps - so long as the time is not 5pm or 7am, keep the lamps off.  
