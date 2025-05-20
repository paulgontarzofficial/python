#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple todaY() method from the date class
today = date.today()
# print("Today is",today)



# print out the date's individual components
# print("Date components",today.day,today.month,today.year)

# # retrieve today's weekday (0=Monday, 6=Sunday)
# print("Today is",today.weekday)  

print("Today's weekday number is",today.weekday())

## DATETIME OBJECTS
# Get today's date from the datetime class
current_today = datetime.now()
print("The current date and time is",current_today)

# Get the current time
t = datetime.time(datetime.now()) 
print("The current time is", t)