# What is a computer program?
# Digital instructions for computers to execute - Instructions

# What is Syntax?
# the rules of a programming language. 
# ex. Spanish is language that has 
# certain vocab rules that aren't in other languages

# An example of syntax (how to write) a function using python. 
def myFunction():
    print('This is an example of a function in Python.')
    print(type(10))

myFunction()

# An example of syntax(how to write) a function in JavaScript.
# function myFunction(){
#    console.log('This is an example of a function in JavaScript.')
# }

# What is a data type in Python? 
# A data is a piece information that the computer understands to
# fundamental; datas are our alphabet for a programming language.

# Examples of data types; string, float, integer

# What is data casting? 
# data casting is the process of changing a data type. 

# ex. We use the int() function to change the string value into an integer
def multiplyNumbers():
    number = input('Please enter a number and this program will multipy it by 4: ')
    result = int(number) * 4
    print(f'here is the result: {result}')

# What are operators in Python?
# operators allow us to perform actions on data. Actions can be things such
# as doing math, comparing infromation (data), or assigning information (data).

action_1 = 2 + 2 
# the answer is 4, and we are doing addition on these two data types
# this is an arithmatic operator (addtion)

action_2 ='Ian'
action_3 ='Kimble'
# this is going to have the value of 'Ian'. We are assigning 
# this string  data to a variable 
# This is the assignment operator
# anytime there is 1 (ONE) equal sign, means we are assigning a value. 

action_4 = 2 == 2
# This is going to be true, becasue the number 2 is the SAME as the other
# other number 2. 
# This is the comparison operator.
# whenever there are 2(TWO) equal signs, it means we are comparing if 
# the data/ information is the SAME

# What is a list? 
# A list is a collection of data. 
# A list can store different data types. 
# When we want to create a list we use square brackets []

randomList = ['cheese',10, 10.292, True, ['ian','kimble'], myFunction,{}]
#print(randomList)

# Why do we use lists?
# We use lists to save,store, and retrieve information. We also use lists to keep data in order. 

# What is a function?
# Instrunctions (program) that we can SAVE for later and CALL when we need it. 

# What are function arguments and parameters? 
# What is the difference between them?

# A function parameter is a PLACEHOLDER for data.
# We pass this data inside the function definition. 
#(The part where we write def)
# remember P- for parameter, P- for placeholder. 

# A function arguement is the ACTUAL data we pass into the function call.
# remember A for argument, A for Actual/ Real data. 

def addition(number):
    result = number + 100
    print(result)
addition(100)

# What is a Conditional Statement?
# A conditional statement is a construct that allows developers to make decesision in code. 

# example:

def isItRaining(rain):
    if rain == True:
        print('It is raining today.')
    else:
        print('It is not raining today.')

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