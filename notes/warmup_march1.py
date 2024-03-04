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
# the following grade rubric: 

# A = 90 and up
# B = 80 and up
# C = 70 and up
# D = 60 and up
# F = 59 and below

# Keywords and Clues

# Generate a letter grade from a number = Enter a number 
# and then send out a letter.

# We need to use Conditional statements (IF/ ELSE/ ELIF).

# We need to write a function that has a parameter.

# We need to enter number score as an argument. 

grades = [60,70,80,90]

def gradeBook_Amari(gradeScore):
    if gradeScore >= grades[3]:
        print('this student has an A')        
    elif gradeScore >= grades[2]:
        print('this student has a B')        
    elif gradeScore >= grades[1]:
        print('this student has a C')        
    elif gradeScore >= grades[0]:
        print('this student has a D')  
    else:
        print('this student has a F. ') 

#gradeBook_Amari(59)

def gradeBook_Jaden(gradeScore):
    if gradeScore >= 90:
        print('this student has an A')        
    elif gradeScore >= 80:
        print('this student has a B')        
    elif gradeScore >= 70: 
       print('this student has a C')        
    elif gradeScore >= 60:
       print('this student has a D')  
    else:
       print('this student has a F. ') 

#gradeBook_Jaden(19)

def gradeBook_Ian(gradeScore):
    if gradeScore >= 90:
        print('this student has an A')        
    elif gradeScore >= 80 and gradeScore <= 89:
        print('this student has a B')        
    elif gradeScore >= 70 and gradeScore <= 79: 
       print('this student has a C')        
    elif gradeScore >= 60 and gradeScore <= 69:
       print('this student has a D')
    elif gradeScore >= 1 and gradeScore <= 59:   
        print('this student has a F. ') 
    else:
        print('Error: Cannot enter zero as a grade.') 

gradeBook_Ian(1)