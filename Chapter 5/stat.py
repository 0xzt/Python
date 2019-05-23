# Given 3 floating-point numbers. Use a string formatting expression with conversion specifiers to output their average and their product as integers, then as floating-point numbers.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# Ex: If the input is:

# 10.3
# 20.4
# 5.0

# the output is:

# 11 1050
# 11.90 1050.60


num1 = float(input())
num2 = float(input())
num3 = float(input())

total_sum = num1 + num2 + num3
float_avg = total_sum / 3
float_mul = num1 * num2 * num3


print(str(int(float_avg)) +' '+ str(int(float_mul)))
print('%0.2f' % float_avg +' '+ '%0.2f' % float_mul)