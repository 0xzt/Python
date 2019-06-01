# Many documents use a specific format for a person's name. Write a program whose input is: firstName middleName lastName, and whose output is: lastName, firstName middleInitial.

# Ex: If the input is:
# Pat Silly Doe

# the output is:
# Doe, Pat S.

# If the input has the form firstName lastName, the output is lastName, firstName.

# Ex: If the input is:
# Julia Clark

# the output is:
# Clark, Julia

##

full_name = input()

f_name = full_name.split(' ')

if len(f_name) == 3:
    first_name = f_name[0]
    middle_init = f_name[1][0]
    last_name = f_name[2]
    
    print('{2}, {0} {1}.'.format(first_name, middle_init, last_name))
else:
    first_name = f_name[0]
    last_name = f_name[1]
    
    print('{1}, {0}'.format(first_name, last_name))