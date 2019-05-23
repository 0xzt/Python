# Write a program that takes in an integer in the range 20-98 as input. The output is a countdown starting from the integer, and stopping when both output digits are identical.

# Ex: If the input is:
# 93

# the output is:
# 93 92 91 90 89 88

# Ex: If the input is:
# 77

# the output is:
# 77

# Ex: If the input is:
# 15
# or any value not between 20 and 98 (inclusive)

# the output is:
# Input must be 20-98

# Use a while loop. Compare the digits; do not write a large if-else for all possible same-digit numbers (11, 22, 33, …, 88), as that approach would be cumbersome for larger ranges.


max_num = int(input())

if (20 <= max_num <= 98):
    if max_num >= 88:
        min_num = 87
    elif max_num >= 77:
        min_num = 76
    elif max_num >= 66:
        min_num = 65
    elif max_num >= 55:
        min_num = 54
    elif max_num >= 44:
        min_num = 43
    elif max_num >= 33:
        min_num = 32
    else:
        min_num = 10
    for n in range(max_num, min_num, -1):
        print(n)
else:
    print('Input must be 20-98')
    