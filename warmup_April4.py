
# SMART definition
# A While Loop is a control construct that will run a 
# block of code repeatedly, so long as 
# the condition is True. 

# Short definition
# A While loop is a function that 
# will run a block of code repeatedly, 
# so long as the condition .is true

def messageFunction():
    msg = 'hello' # variabe called msg, being assigned 
    # the string value 'hello'

    while msg =='hello': # (So long as this is true) --  
        # msg is equal to hello
        print(msg) # Repeat this
    #    msg = input('please enter a message: ')
    #    if msg == 'goodbye':
     #       print("the loop has stopped! Congrats")
        break
#messageFunction()

def driveThru_orderSystem():
    print('WENDYS MENU')
    print('#1 - chesseburger: $10.00')
    print('#2 - fries: $5.00')
    print('#3 - chicken: $10.00')
    print('#4 - milkshake: $4.00')
    foodItem= ['cheeseburger','fries','chicken','milkshake']
    foodPrice =[10.00, 5.00, 10.00, 4.00]
    orderList =[]
    orderPrice =0
    
    welcomeOrder = int(input('Welcome to Wendys, what would you like? '))
    orderComplete = False
 
    if welcomeOrder == 1:
        orderList.append(foodItem[0])
        orderPrice = foodPrice[0]
       
    elif welcomeOrder ==2:
        orderList.append(foodItem[1])
        orderPrice = foodPrice[1] 
    elif welcomeOrder ==3:
        orderList.append(foodItem[2])
        orderPrice = foodPrice[2]
    elif welcomeOrder ==4:
        orderList.append(foodItem[3])
        orderPrice = foodPrice[3]
    
    print(f'here is your order {orderList}')
    print(f'here is your total: ${orderPrice}')

    while orderComplete == False: 
        customerOrder = input('would you like to add somthing else? ')
        if customerOrder == 'y':
            newOrder = int(input('What would you like? '))
            if newOrder == 1:
                orderList.append(foodItem[0])
                orderPrice += foodPrice[0]
            elif newOrder ==2:
                orderList.append(foodItem[1])
                orderPrice += foodPrice[1] 
            elif newOrder ==3:
                orderList.append(foodItem[2])
                orderPrice += foodPrice[2]
            elif newOrder ==4:
                orderList.append(foodItem[3])
                orderPrice += foodPrice[3]                 
        elif customerOrder == 'n':
            print(f'here is the food that you ordered: {orderList}') 
            print(f'here is your total: ${orderPrice}, pull up to the next window.')
            break

#driveThru_orderSystem()















# go over the inventory example
# go over the bank example
# do a uber eats example of adding things to a cart and ordering the food.


# break when we get to a 25 users.
# break logic for creating an error message.
# continue if the value in a string is a different color. 


def numberIncrement():
    i = 0 # iterator= starting point for our loop. 
 
    # keyword, all while means is: 
    # 'so long as this condition is true'.
    while i < 3:
        print('Welcome to Python.') # print this on a loop 3x.
        i += 1 
        print(f'i is now: {i}')



def messageFunction():
    dailyMsg = input("Please enter whether it is morning or afternoon: ")

    while dailyMsg == 'morning':
        print('Good Morning.')
        print('waiting...3 - reading code line for line')
        print('waiting...2 - reading code line for line')
        print('waiting...1 -  reading code line for line')
        dailyMsg = input("what time of day is it now: ")
    if dailyMsg == 'afternoon':
        print('Good Afternoon.')
        print("________________")
        print('Ending Loop.')



def passwordCheck():
    userPassword = int(input('Please enter a password: '))
    correctPassword = 1234
    attempt = 0
    while userPassword != correctPassword and attempt < 3:
        print('incorrect password. Please Try again. ')
        attempt +=1
        print(f'number of attempts: {attempt}')
        if attempt > 4:
            print('Exceeded attempts. try again in 5 minutes.')
        userPassword = int(input('Please enter a password: '))
    if userPassword == correctPassword:
        print('password correct. You may veiw the site.')

passwordCheck()