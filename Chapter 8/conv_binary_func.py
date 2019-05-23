# Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary. For an integer x, the algorithm is:

# As long as x is greater than 0
#    Output x % 2 (remainder is either 0 or 1)
#    x = x / 2
# Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function to reverse the string.

# Ex: If the input is:
# 6

# the output is:
# 110

# Your program must define and call the following two functions. The function integer_to_reverse_binary() should return a string of 1's and 0's representing the integer in binary (in reverse). The function reverse_string() should return a string representing the input string in reverse.
# def integer_to_reverse_binary(integer_value)
# def reverse_string(input_string)

# Note: This is a lab from a previous chapter that now requires the use of a function.


def integer_to_reverse_binary(integer_value):
    str1 = str()
    while integer_value > 0:
        num_val = integer_value % 2
        str1 = str(str1) + str(num_val)
        integer_value = integer_value // 2
    return str1

def reverse_string(input_string):
    backwards = "".join(reversed(input_string))
    return backwards

if __name__ == '__main__':
    user_int = int(input())
    print(reverse_string(integer_to_reverse_binary(user_int)))
