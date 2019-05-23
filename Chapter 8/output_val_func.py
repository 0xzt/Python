# Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follow. Then, get the last value from the input, and output all integers less than or equal to that value.

# Ex: If the input is:
# 5
# 50
# 60
# 140
# 200
# 75
# 100

# the output is:
# 50
# 60
# 75

# The 5 indicates that there are five integers in the list, namely 50, 60, 140, 200, and 75. The 100 indicates that the program should output all integers less than or equal to 100, so the program outputs 50, 60, and 75.

# Such functionality is common on sites like Amazon, where a user can filter results.

# Your code must define and call the following two functions:
# def get_user_values()
# def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

# Utilizing functions will help to make your main very clean and intuitive.

# Note: This is a lab from a previous chapter that now requires the use of functions.


def get_user_values():
    list_len = int(input())
    list1 = list()
    for n in range(0, list_len):
        list1.append(int(input()))
    max_val = int(input())
    return list1, max_val

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for n in user_values:
        if n <= upper_threshold:
            print(n)

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
    