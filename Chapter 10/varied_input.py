# Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

# Ex: If the input is:
# 15 20 0 5

# the output is:
# 10 20

##

user_input = input()
new_list = user_input.split()
my_list = new_list
my_total = 0

for i in my_list:
    my_total += int(i)
    
my_avg = int(my_total / len(my_list))

my_max = -999
for n in my_list:
    if int(n) > my_max:
        my_max = int(n)

print(my_avg, my_max)
