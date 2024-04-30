def message():
    msg = 'hello' 
    # variable being assigned string w/ the value of hello.
    # msg=
    while msg == 'hello':
    # while --> so long as this is true
    # variable msg is the same as hello (hello is the same as hello)
        print(msg) # print this out so long as the statement above is true
        msg = input('type a new message: ')
        if msg =='goodbye':
            print('ending loop.')
#message()

def counter():
    i = 0 # iterator; a starting point for a loop/ can be any data type. 
    while i < 4: # while = so long as this condition is true...
        print('cheese puffs.') # do this *(our instructions)...
        i += 1
        print(i)
    if i == 10:
        print('loop has stopped.')
        print(i)

def isSheMarried():
    womanLastName = 'Smith'
    manLastName = 'jackson'
    while womanLastName == 'Smith':
        print('this woman is not married.')
        print('instructions going in order')
        print('fake instruction 1')
        print('fake instruction 2')
        womanLastName = input('whats your last name? ')      
    if womanLastName =='jackson':
        print('this is a married woman.')
# isSheMarried()

def passCode():
    correctCode = 1234
    userInput= int(input('Please enter a passcode: '))

    while userInput != correctCode: 
        print('attempt incorrect. Please try again. ')
        userInput=int(input('please enter correct code:'))
    if userInput == correctCode:
        print('correct, access granted.')

# passCode()
























# Create a function that will ask the user to enter a date to 
# check if it is user’s birthday. The function should have 
# the correct birth date stored as a variable. 
# The user should be prompted to enter the month and date. 
# If the day they entered is incorrect, print a message 
# informing them it is incorrect and re-ask them to enter 
# the correct birthday. If the user enters the correct birth date,
#  your function should congratulate them and stop the loop.  

# Keywords / Clues:
# Variable, Function, If/Else (Conditionals),
# Loop, take in user data
# print

# Context:
# Re-ask user if they enter the incorrect B-day
# Ask the user to enter a birthday, 
# if they enter the correct date: congratulate them and end the loop
# if they get it wrong: repeat loop

def checkBday():
    month=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    day=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
    bday = [month[1],day[1]]
    print(f'birthdate is {bday}')
    
    userInput=[]

    userInput_Month = int(input('Please enter the correct Bday Month: '))
    userInput_Day = int(input('Please enter the correct Bday Date: '))   

    while userInput != bday:
        userInput.append(userInput_Month)
        userInput.append(userInput_Day)
        userInput.clear()
        print(f'number stored in userInput: {userInput}')
    if userInput == bday:
       print('congrats! Happy Bday!')

#checkBday()