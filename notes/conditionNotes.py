# Conditional Statement = Is a construct that evaluates
# different code conditions and outputs specific outcomes. 

'Evaluate specific conditions' 
'and will output specific outcomes'

# the IF/ ELSE keywords are functions that have 
# been abstracted to make it easier for 
# engineers to use logic. 







#def passwordCheck(userPassWord):
#    password ='123'
#    if userPassWord == password: 
    # if keyword - specificies the condition we want to evaluate.
#        print("password correct. Welcome to the site.")
        # the code above is our outcome for 
        # the condition we want to check.
#    else:
    # else keyword - specifies the outcome to
    # run if intended condition isn't met.    
    # exit / default = if nothing is met, run this. 
#        print('password is incorrect. Please try again.')

# passwordCheck(1122)

# stoveIsHot= 0

# if stoveIsHot== True:
#    print('you got burnt.')
# else:
#    print('dont touch the stove its hot')




# What is the difference between a function
# argument and a function parameter?

# parameters- placeholders for data inside
# of a function definition

# arguments-  are real data pass into a function


# Create a document called conditionalActivity_Feb28.py 
# and complete the following prompt. 

#You have been 
# hired as an engineer to develop a passcode system for 
# the companies entrance system. The company would
# like to have a system in place that will check
# the passcode entered by users at the door, 
# and if the code matches the code in the program, 
# the user may enter, but if it does not match, 
# their credentials will be rejected. The client 
# has provided you with the passcode that users 
# must use to enter.
# Passcode that must be used: “get_this_money”

# clues
# user need to enter a passcode
# -> passcode ="get_this_money"

# compare the passcode from the system with 
# the passcode from user (Comparision operator)

# if passcode matches= access granted
# if it doesnt = access denied
#myVariable= 'contain data'
#def myFunction():
    # contain instructions

def entrancePasscode():
    actualPassCode = 'get_this_money'
   # userCode = input('Please enter user code. ')

    if 10+10 == 9+11:
        print('Access Granted.')
    else:
        print('Access Denied.')

# entrancePasscode()

def lunchOrder():
    userChoice=input('what would you like for lunch? ')
    userSides =''
    if userChoice == 'cheese burger':
        print('heres your cheese burger')
        if userSides == 'fries':
            print('heres your fires.')
    
    elif userChoice == 'grilled cheese':
        print('heres your grilled cheese')
    
    elif userChoice == 'salad':
        print("heres your salad.")
    
    elif userChoice == 'lasagna':
        print('here is some lasagna')
    
    else:
        print('heres are some chicken nuggets.')
   
lunchOrder()