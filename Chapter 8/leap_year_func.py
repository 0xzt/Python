# A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth takes longer to rotate around the sun. To account for the difference in time, every 4 years, a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The requirements for a given year to be a leap year are:
# 1) The year must be divisible by 4
# 2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400
# Some example leap years are 1600, 1712, and 2016.

# Write a program that takes in a year and determines whether that year is a leap year.

# Ex: If the input is:
# 1712

# the output is:
# 1712 is a leap year. 

# Ex: If the input is:
# 1913

# the output is:
# 1913 is not a leap year.

# Your program must define and call the following function. The function should return true if the input year is a leap year and false otherwise.
# def is_leap_year(user_year)

# Note: This is a lab from a previous chapter that now requires the use of a function.


def is_leap_year(user_year):
    if ((user_year % 100) == 0) and ((user_year % 400) == 0):
        leap_flag = True
    elif ((user_year % 100) != 0) and ((user_year % 4) == 0):
        leap_flag = True
    else:
        leap_flag = False

    return leap_flag

if __name__ == '__main__':
    int1 = int(input())
    year_flag = is_leap_year(int1)
    if year_flag == True:
        print('%d is a leap year.' % int1)
    else:
        print('%d is not a leap year.' % int1)