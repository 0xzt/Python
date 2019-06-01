# Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

# Ex: If the input is:
# 10 -7 4 39 -6 12 2

# the output is:
# 2 4 10 12 39

##

my_list = input()
new_list = my_list.split()

for i in new_list:
    if int(i) < 0:
        new_list.remove(i)  

new_list.sort(key=int)
        
[print(i, end=' ') for i in new_list]
