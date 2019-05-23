# Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

# Ex: If the input is:
# April
# 11

# the output is:
# spring

# In addition, check if the string and int are valid (an actual month and day).

# Ex: If the input is:
# Blue
# 65

# the output is:
# invalid 

# The dates for each season are:
# spring: March 20 - June 20
# summer: June 21 - September 21
# autumn: September 22 - December 20
# winter: December 21 - March 19


month = input()
day = int(input())

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
elif month in ('October', 'November', 'December'):
	season = 'autumn'
elif month != ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'):
    season = 'invalid'
	
if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
	if (month == 'September') and (day > 30):
	    season = 'invalid'
elif (month == 'December') and (day > 20):
	season = 'winter'	
elif (day > 32):
    season = 'invalid'
elif (day < 0):
    season = 'invalid'
    
print(season)