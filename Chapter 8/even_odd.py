# Write a program that reads a list of integers, and outputs whether the list contains all even numbers, odd numbers, or neither. The input begins with an integer indicating the number of integers that follow.

# Ex: If the input is:
# 5
# 2
# 4
# 6
# 8
# 10

# the output is:
# all even

# Ex: If the input is:
# 5
# 1
# 3
# 5
# 7
# 9

# the output is:
# all odd

# Ex: If the input is:
# 5
# 1
# 2
# 3
# 4
# 5

# the output is:
# not even or odd

# Your program must define and call the following two functions. is_list_even() returns true if all integers in the list are even and false otherwise. is_list_odd() returns true if all integers in the list are odd and false otherwise.
# def is_list_even(my_list)
# def is_list_odd(my_list)

def is_list_even(my_list):
    has_even = False
    has_odd = False
    for n in my_list:
        if n % 2 == 0:
            has_even = True
        else:
            has_odd = True
    if (has_even == True) and (has_odd == False):
        return True
    else:
        return False

def is_list_odd(my_list):
    has_even = False
    has_odd = False
    for n in my_list:
        if n % 2 == 0:
            has_even = True
        else:
            has_odd = True
    if (has_even == False) and (has_odd == True):
        return True
    else:
        return False
        

if __name__ == '__main__':
    u_list = list()
    list_len = int(input())

    for n in range(0, list_len):
        u_list.append(int(input()))
    
    if (is_list_even(u_list) == True) and (is_list_odd(u_list) == False):
        print('all even')
    elif (is_list_even(u_list) == False) and (is_list_odd(u_list) == True):
        print('all odd')
    else:
        print('not even or odd')