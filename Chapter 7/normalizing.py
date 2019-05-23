# When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This can be done by normalizing to values between 0 and 1, or throwing away outliers.
# Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follow. Then, adjust each integer in the list by subtracting the smallest value from all the integers.

# Ex: If the input is:
# 5
# 30
# 50
# 10
# 70
# 65

# the output is:
# 20
# 40
# 0
# 60
# 55

# The 5 indicates that there are five integers in the list, namely 30, 50, 10, 70, and 65. The smallest value in the list is 10, so the program subtracts 10 from all integers in the list.


my_list = list()

max_m = int(input())

for n in range (0, max_m):
    my_list.append(int(input()))

min_num = my_list[0]

for n in my_list:
    if n < min_num:
        min_num = n

for n in my_list:
    t_num = n - min_num
    print(t_num)
    