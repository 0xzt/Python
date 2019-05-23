# Driving is expensive. Write a program with a car's miles/gallon and gas dollars/gallon (both floats) as input, and output the gas cost for 10 miles, 50 miles, and 400 miles.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f %0.2f %0.2f' % (your_value1, your_value2, your_value3))

# Ex: If the input is:

# 20.0
# 3.1599
# Then the output is:

# 1.58 7.90 63.20
# Note: Real per-mile cost would also include maintenance and depreciation.

#---- 

# car miles per gallon
# gas dollar per gallon (both floats)
# cost 10,50,400 miles

milesPerGallon = float(input())
dollarsPerGallon = float(input())

miles_10 = (10 / milesPerGallon) * dollarsPerGallon
miles_50 = (50 / milesPerGallon) * dollarsPerGallon
miles_400 = (400 / milesPerGallon) * dollarsPerGallon

print('%0.2f %0.2f %0.2f' % (miles_10, miles_50, miles_400))