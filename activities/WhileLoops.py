#i = 0 # variable being assigned the value zero.
# i = iterator. Our loops starting point. 
#while i <= 10: # so long as 0 is less than 5...
#  print(i) # print the variable
#  i += 1  # addding 1 to our variable

# While = so long as a condition is true, do this...

def airMax_inventorySystem():
  airMax = 5 # our iterator/ starting
  while airMax > 0:
    userCart= input('Would you like to buy these sneakers? ')
    if userCart == 'y':
      airMax -= 1 
      print(f'air max inventory : {airMax}')
    if airMax== 0:
      print('out of stock.')

def japanSavings():
  japan_Savings_Account = 0
  while japan_Savings_Account<= 10000: 
    user_Deposit = int(input('how much would you like to put away for your trip? '))
    japan_Savings_Account += user_Deposit
    print(f'You have {japan_Savings_Account} in your account.')
  print('Congrats, your on your way to Japan.')

japanSavings()








#inventory_hangers = 10
#while inventory_hangers > 1:
 # purchase=input('Would you like to buy a hanger? ')
  #if purchase == 'y':
   # inventory_hangers -=1     
    #print(f'hangers in inventory left: {inventory_hangers}')
#print("Out of stock: Order more hangers.")













#inventory = 'full'
#while inventory == 'full':
#  print('we are fully stocked.')

#inventory = 0
#while inventory < 4:
#    print('order more stock for store.')
 #   if inventory == 5:
  #      break # break will stop our loop
   # inventory +=1

#if inventory == 5:
 #   print('Store is now fully stocked.')


#gameScore = 0
#while gameScore < 21:
 #   print(f'keep playing the game. score is: {gameScore}')
  #  if gameScore >= 21:
   #     break
    #gameScore +=1

#if gameScore == 20:
 #   print('game point...')

#if gameScore >=21:
 #   print('game over.')