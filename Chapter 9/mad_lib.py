# Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.

# Write a program that takes a string and integer as input, and outputs a sentence using those items as below. The program repeats until the input string is quit.

# Ex: If the input is:
# apples 5
# shoes 2
# quit 0

# the output is:
# Eating 5 apples a day keeps the doctor away.
# Eating 2 shoes a day keeps the doctor away.

# Note: This is a lab from a previous chapter that now requires the use of a loop.

##

my_string = input()
libs = my_string.split()

while libs.count('quit') == 0:
    print('Eating {1} {0} a day keeps the doctor away.'.format(libs[0], libs[1]))
    libs.clear()
    my_str = input()
    libs = my_str.split()