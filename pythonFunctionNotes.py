# Function- A set of instructions that 
# execute one task in a program.

# Functions have 2 parts:

# 1. function definition- the instruction on how
# the function works for the program. 

def goodAfternoon():
    print('good afternoon team! ')

# 2. function call- tells the program 
# to run/execute our function instructions.
    
#goodAfternoon()

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
    
#jobSearch_bySalary('120,000')





# Create a function that will inform a user 
# if the weather is hot or cold based on a argument 
# passed into it. In your function, if the temperature 
# is over 75.00 return to the user it is hot outside 
# and if it is below 70 it is cold. If it is neither
# above 75 but not below 70 return a message saying
# the weather is perfect. 
def weather_system(temp):
    if temp > 75:
        print('it is hot outside.')
    elif temp <70:
        print('it is cold outside.')
    else:
        print('the weather is perfect.')  
weather_system(76)





#def weather_info(temperature):
 #   if temperature> 75.00:
  #      return 






#def weatherSystem(hot, cold):
 #   if weather = cold: 
  #      print('the weather outside is cold.')
   # if weather >= 75:
    #    print('it is hot outside.')

#weatherSystem()

#def weather(hot,cold)
 #   if temp >= 75
  #  (print it is hot outside):
