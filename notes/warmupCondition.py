# 1. In your own words, describe what python conditional 
# statements are (IF / ELSE); more specifically, 
# try to describe how they work. 

'Conditional statements allow programs to behave'
'differently depending on conditions.'
 
'A way to make decisions in code.'

'Evaluates a condition and runs'
'a code block if the condition is True.'
'if its not true, it will default to the else block.'

#if 10+1 > 10+9:
# if 11 is greater than 19... do this... 
#    print('great! true.')
#else:
# otherwise do this...
#    print('something went wrong... false')


# 2. Create a function that takes in user 
# data and uses a conditional statement (if/ else) 
# to determine if a user has reached a games 
# high score. Your function should ask the 
# user what their score is. If the user score 
# is above 3,000, they have achieved the high 
# score, but if it is below 3,000, they have not.

# clues/ key words
# 1. We need to use conditional statements (IF/ ELSE).
# 2. We need to write a function. x
# 3. We need to ask the user what their score is. x
# 4. IF user score is above 3000 = they got the high score.
# 5. ELSE if user score is not = sorry you didnt get the high score.  

def check_highScore():
    userScore= int(input('What is your current score? '))
    if userScore > 3000: 
        print('Congrats! You got the high score!')
    else:
        print("Sorry. You didnt get the high score. Try again.")
# check_highScore() 

month = int(input("what month is it? "))
seasons =[1,2,3,4,5,6,7,8,9,10,11,12]

if month >= seasons[0] and month <= seasons[2]:
    print("The season is winter.")
elif month > seasons[2] and month <= seasons[6]:
    print("the season is Spring")
elif month > seasons[6] and month < seasons[9]:
    print("the season is Summer")
elif month >= seasons[8] and month <=seasons[11]:
    print('the season is Fall')
else:
    print("something went wrong. check your code.")


