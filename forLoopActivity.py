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
            
twitterTextPost()










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