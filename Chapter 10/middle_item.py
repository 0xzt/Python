# Given a sorted list of integers, output the middle integer. Assume the number of integers is always odd.

# Ex: If the input is:
# 2 3 4 8 11

# the output is:
# 4

# The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".

# Hint: First read the data into a list. Then, based on the list's size, find the middle item.

##

user_input = input()
new_list = user_input.split()
my_list = new_list
my_list.sort(key=int)

if len (my_list) > 10:
    print('Too many inputs')
else:
    print(my_list[len(my_list) // 2])
