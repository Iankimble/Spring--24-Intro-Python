# For Loop - Is a loop that iteates over a collection of data.
# data can be lists [] and strings.

# While Loop - Is a block of code that repeats itself so long
# as a condition is true. 

# For Loop - grades; caluclating class GPA. 

# We need to add up all the grades and then divide 
# to get the average.

def gpa():
    listOfGrades = [100, 90, 70, 50, 80, 80, 70, 0, 0] 
    totalScore = 0 # add up all the grades and place in here.  
    for grade in listOfGrades:
        totalScore += grade 
        print(grade) 
        print(f'this is the total score: {totalScore}')
        numberOfGrades = len(listOfGrades)
        gpa = totalScore / numberOfGrades
        print(f'This is the class GPA: {gpa}')
# gpa()

# While Loop - merchandise; checking the quantity of an item. 

def baseballGlove_inventory():
    baseballGlove_sm = 0
    baseballGlove_sm_special_Edition= 3
    baseballGlove_md = 1
    baseballGlove_md_special_Edition= 3
    baseballGlove_lg = 0
    baseballGlove_total = baseballGlove_sm + baseballGlove_md + baseballGlove_lg
   
    while baseballGlove_total != 0:
        userCart = input('What size glove would you like to buy? ')
        if userCart == 'sm':
            baseballGlove_sm -= 1
            print(f'small baseball glove inventory: {baseballGlove_sm}')
            if baseballGlove_sm == 0:
                print('small gloves are out of stock.')
        if userCart == 'md':
            baseballGlove_md -= 1
            print(f'medium baseball glove inventory: {baseballGlove_md}')
            if baseballGlove_md == 0:
                print('medium gloves are out of stock.')
        if userCart == 'lg':
            baseballGlove_lg -= 1
            print(f'large baseball glove inventory: {baseballGlove_lg}')
            if baseballGlove_lg == 0:
                print('large gloves are out of stock.')
        else:
            print('We are completely out of stock. ')
            break

# baseballGlove_inventory()

# Create a loop that runs from 1-20, and 
# will print only when it lands
# on an even number

i = 0
while i < 20: # so long as this is true.
    i += 1
    if i % 2 == 0:
        print(f'this is even: {i}') 
        continue
    print(i)
























# While Loop - repeats a block of code instructions, so long
# as a condition is true. 

#i = 0 
# i = stands for iterator. It is the starting point for 
# a while loop
#while i == 0:
#    print(i)
# the result here is that i (or 0) will continue to print forever
# because the while condition is true. 

# For Loops - repeats a block of code instructions, up to 
# the number of items in a group. 

def ddg_game():
    groupOfKids =['duck','duck','duck','goose','duck','duck']
    # list of items
    for kid in groupOfKids:
    # for every item in this list; 
    # kid is the item groupOfKids is the list.
        if kid == 'goose':
            print('found the goose!')
            continue
        print(kid)
        # print each item; print each kid. 

# ddg_game()

def rpgGame_weaponSelect():
    inventory=['sword','gun','sheild','potion','grenade']
    print(inventory)
    print("__________________________________")
    userWeapon = input('What weapon would you like to use? ')
    for item in inventory:
        if item == userWeapon:
            inventory.remove(item)
            print(f"You have equipped the {userWeapon} to your fighter.")
            print("__________________________________")
    print('Here is your current inventory: ') 
    print(inventory)

# rpgGame_weaponSelect()

# def gtaCheatCodes():      
# gtaCheatCodes()


def twitterTextPost():
    tweets = ['Hello World','Going on a Trip']
    entry = input('Upload your post: ')
    tweets.append(entry)
    for items in tweets:
        print(items)
        newPost = input('would you like to add a new post? ')
        if newPost =='y':
            newEntry = input('please type in your new post: ')
            tweets.append(newEntry)
            print(tweets)
            
#twitterTextPost()










# FOR LOOP - A construct that will repeat a set of instructions 
# for a list/ group of data. 

def ddg():
    birdGame = ['duck','duck','goose','duck','duck']

    for bird in birdGame:
        if bird == 'goose':
            print(f"found the goose at index {birdGame.index('goose')}")
            continue
        # for loops will only run 
        # up to the number of items in a group
        print(bird) 

def fakeSpadesGame():
    spades= ['1','2','3','4','SJ','SQ','SK','CA']
    for card in spades:
        if card == 'SK':
            spades.remove('SK')
            print(spades)

def customerReturn():
    # when an reciept number is entered, 
    # remove from the items from customers credit card.
    userReturn = input('what would you like to return? ')

    reciept = ['tv','game','controller','movie']

    for item in reciept:
        if item == userReturn:
            reciept.remove(userReturn)
            print("You got your money back. Here is your new receipt...")
            print(reciept)   
            continueShopping=input('Would you like to continue shopping? ')
            if continueShopping == 'y':
                newItem = input('Please enter a new item: ')
                reciept.insert(0,newItem)
                print('Weve added your new item.')
                print(' Here is your new updated reciept...')
                print(reciept)
#customerReturn()

# while x == birdGame[0]: 
    # while loops will run forever 
    # so long as th e conditio is true.
    # print(x)