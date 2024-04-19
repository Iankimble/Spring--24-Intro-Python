# Create a new python document called weekendActivity_April_12.py and complete the 
# following questions. 

# This activity must be submitted no later than Sunday April 14th, by 11:59pm to be
# accepted. 

# 1. In your own words, describe the difference between a FOR LOOP and a WHILE LOOP

# 2. Why is it important to have programs be able to repeat themselves? If necessary, 
# do research to assist with your answer- Please do not copy/paste a response, but rather
# express your answer IN YOUR OWN WORDS using complete sentences. 

# automate tedious, repetative processes. 
# shopping 
# game 

# 3A. Use W3schools to learn about the range() function. Describe how what the range
# function is and how it works.  

# the range function allows us to iterate 
# through numbers with a starting point and an end point

# x = range(1,100)
# for n in x:
  #print(n)

#3B. Then, create a loop using the range function that will only 
# print multiples of 3 between 1 and 30. 
#multiples3 = range(5,11,5)
#for number in multiples3:
#  print(number)

# 4. Create a function that uses a loop to go over the 
# alphabet and prints every 5th letter. 

alaphabet_main = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_saed = ['a','f','k','p','u','z']
numberList = range(0,100)
def alphabetListLoop_Conditional(alphabet):
  for letter in range(0,len(alphabet),5):
    print(f'number of letters in alphabet: {len(alphabet)}')
    print(alphabet[letter])

alphabetListLoop_Conditional(numberList)
 
# Clues/ Keywords
# We can wrap this inside of a function (optional)
# For Loop - we are going over/ iterarting over a list/ group; the alphabet (26) 
# We need a list that contains the letters in the alphabet. 
# We need to print the every 5th letter in the alphabet list. 
# hint: We'll need to use the range function to solve this. 






# Write down clues, keywords, and breakdown and explain 
# how you would approach this problem 
# in order to get full credit. 








