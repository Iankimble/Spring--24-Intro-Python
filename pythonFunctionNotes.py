# Function- A set of instructions that 
# execute one task in a program.

# Functions have 2 parts:

# 1. function definition- the instruction on how
# the function works for the program. 

def goodAfternoon():
    print('good afternoon team! ')

# 2. function call- tells the program 
# to run/execute our function instructions.
    
goodAfternoon()

# Function Parameters and Arguments- external data
# passed into a function. 
# data type = strings, floats, boolean, etc. data base

# parameter- is PLACEHOLDER for incoming data in the function
# definition. 

def giftCard_add5(user_Giftcard):
    newBalance = user_Giftcard + 5
    print(f'your new gift card balance is {newBalance} dollars.')

#giftCard_add5(60)

def giftCard_Add10(user_Giftcard):
    newBalance= user_Giftcard + 10
    print(f'your new gift card balance is {newBalance} dollars.')

# giftCard_Add10(60)

() # ROUND brackets are for functions
[] # SQUARE barkets are for lists
{} # CURLY brackets are data, but can also be objects 
# ( objects are just a collection of data.)

def salary_120k():
    # write some instructions...
    print('here are 120k jobs...')

def jobSearch_bySalary(desiredSalary):
    print('show these result that are in this range...')
    print(f'here are jobs that pay {desiredSalary}')
    salary_120k()
    
jobSearch_bySalary('120,000')

