# For Loops- iterates over a collection of data.
# While Loops- iterates and runs a condition so long as its true. 

# Best way to use for loop =
# Alarms - set a specific time that loops at specific intervals. 
# 5 am - M-F - S,S= no alarms

def alarmClock():
    dayOfWeek= input('What day is it ? ')
    militaryTime =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    # when the hour is >24 --> change the day.


    while dayOfWeek != 'sat': 
        for hour in militaryTime:
            if hour == 5:
                print('sound the alarm')       
            print(hour)
        dayOfWeek= input('What day is it ? ')
    if dayOfWeek != 'sat':
        print('No alarm today. Have a good weekend. ')

alarmClock()

# Best way to use a while loop = 



