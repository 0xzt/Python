# Write a program that reads a list of integers into a list as long as the integers are greater than zero, then outputs the smallest and largest integers in the list.

# Ex: If the input is:
# 10
# 5
# 3
# 21
# 2
# -6

# the output is:
# 2 21

# You can assume that the list of integers will have at least 2 values.

user_num = int(input())
min_num = user_num
max_num = user_num

while user_num > 0:
    next_num = int(input())
    if next_num < 0:
        user_num = 0
        break
    elif next_num < min_num:
        min_num = next_num
    elif next_num > max_num:
        max_num = next_num

print('%d %d' % (min_num, max_num))