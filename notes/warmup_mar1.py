# Open up code spaces and create a new 
# python file called warmup_mar1.py and answer 
# the following questions.

# You have been hired as an engineer to develop a 
# gradebook system. The client would like to create 
# a function that uses conditional statements 
# that will allow teachers to enter a numerical grade,
# and then automatically generates a letter 
# grade for that number (for example a teacher 
# enters a 70, the program should output a C). 
# The numerical grade should be entered as an 
# argument. The client has provided you with 
# the following grade rubric. 

# A = 90 and up
# B = 80 and up
# C = 70 and up
# D = 60 and up
# F = 59 and below

# clues and keyword
# conditional statements IF/ ELSE/ ELIF.
# need to use arguement to pass in a number grade - Integer.
# need to print() a letter for the grade - String.
# need to use comparison operators (less than, greater than).
# we need to make a function. 

def gradeBook(studentGrade):
    if studentGrade >= 60 and studentGrade <= 69:
        print('This student has a D.')
    elif studentGrade >= 70 and studentGrade <= 79:
        print('This student has C.')
    elif studentGrade >= 80 and studentGrade <= 89:
        print('This student has a B.')
    elif studentGrade >= 90 and studentGrade <=100:
        print('Thie Student has A.')
    else:
        print('This student has an F.')

# gradeBook(102)

#if gymMember():

def survey():
    satisifaction_Score = input("how would you rate your experience from 1-5 ? ")
    if satisifaction_Score ==1:
        print("you said it was a 1, sorry for the poor experience. ")
    elif satisifaction_Score==2:
        print("you said it was a 2, sorry for the poor experience. ")
    elif satisifaction_Score==3:
        print("you said it was a 3, we'll do better next time. ")
    elif satisifaction_Score==4:
        print("you said it was a 4,great! We'll do better next time. ")
    elif satisifaction_Score==5:
        print("Excellent! Were glad you had a good experience. ")
    else: 
        print('Error, your response must be a number 1-5.')

membership_level =['bronze', 'silver','gold','platinum']
bronzeBenefits=['access to equipment', 'access to weights']
silverBenefits= ['everything in bronze','free locker']
goldBenefits = ['everything in silver','access to bring another guest']
platinumBenefits =['everything in gold','free water bottle', 'swimming pool']
gymLevel = input('what membership do you have? ')

if gymLevel == membership_level[0]:
    print('you are a bronze member, you have access to the following:')
    print(bronzeBenefits)
elif gyml
