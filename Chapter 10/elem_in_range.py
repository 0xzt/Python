# Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).

# Ex: If the input is:
# 25 51 0 200 33
# 0 50

# the output is:
# 25 0 33 

# The bounds are 0-50, so 51 and 200 are out of range and thus not output.

# For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.

##

user_input = input()
new_list = user_input.split()
my_list = new_list

more_input = input()
range_list = more_input.split()
ranges = range_list

int_list = ''

for n in my_list:
    if (int(n) >= int(ranges[0])) and (int(n) <= int(ranges[1])):
        int_list += n + ' '

print(int_list, end='')