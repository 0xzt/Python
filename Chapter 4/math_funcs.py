# Given three floating-point numbers x, y, and z, output the square root of x, the absolute value of (y minus z) , and the factorial of (the ceiling of z).

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f %0.2f %0.2f' % (your_value1, your_value2, your_value3))

# Ex: If the input is:

# 5.0
# 6.5
# 3.2
# Then the output is:

# 2.24 3.30 24.00


import math
x = float(input())
y = float(input())
z = float(input())

print('%0.2f' % math.sqrt(x), '%0.2f' % math.fabs(y-z), '%0.2f' % math.factorial(math.ceil(z)))