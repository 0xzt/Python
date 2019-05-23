# Write a function max_magnitude() with two integer input parameters that returns the largest magnitude value. Use the function in a program that takes two integer inputs, and outputs the largest magnitude value.

# Ex: If the inputs are:
# 5 7

# the function returns:
# 7

# Ex: If the inputs are:
# -8 -2

# the function returns:
# -8

# Note: The function does not just return the largest value, which for -8 -2 would be -2. Though not necessary, you may use the built-in absolute value function.

# Your program must define and call the following function:
# def max_magnitude(user_val1, user_val2)

import math

def max_magnitude(user_val1, user_val2):
    if abs(user_val1) > abs(user_val2):
        return user_val1
    else:
        return user_val2

if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    print(max_magnitude(user_val1, user_val2))
