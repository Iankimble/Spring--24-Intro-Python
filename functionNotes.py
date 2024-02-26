# functions= sub-instructions
# inside of a program that only do one thing.

# functions have 2 parts
# 1. function definition-  tells the computer what
# the function does

def goodMorning():
    # function has one job/ instruction.
    print('good morning.') 

# 2. function call- tells the 
# computer to run that function.

goodMorning() # use it by writing (calling) its name.

# function parameters and arguments

# a function parameter is a PLACEHOLDER 
#for data inside of the  function DEFINITIION. 

def giftCard_add5_toBalance(user_Giftcard):
    newBalance = user_Giftcard + 5
    print(f'you now have {newBalance} dollars on gift card.')
   
def giftCard_Add10_toBalance(user_Giftcard):
    newBalance = user_Giftcard + 10
    print(f'you now have {newBalance} dollars on gift card.')

def giftCard_Add50_toBalance(user_Giftcard):
    newBalance = user_Giftcard + 50
    print(f'you now have {newBalance} dollars on gift card.')

def giftCard_AddCustom_toBalance(user_Giftcard):
    newBalance = user_Giftcard 
    print(f'you now have {newBalance} dollars on gift card.')

# function argument is the ACUTAL DATA you pass inside
# of your function CALL.
# Argument = facts = data
giftCard_Add50_toBalance(1)


