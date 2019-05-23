# One lap around a standard high-school running track is exactly 0.25 miles. Write a program that takes a number of miles as input, and outputs the number of laps.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# Ex: If the input is:
# 1.5

# the output is:
# 6.00

# Ex: If the input is:
# 2.2

# the output is:
# 8.80

# Your program must define and call the following function:
# def miles_to_laps(user_miles)


def miles_to_laps(miles):
    laps = miles / 0.25
    return laps
    
if __name__ == '__main__':
    miles = float(input())
    laps = miles / 0.25
    print('%0.2f' % laps)
