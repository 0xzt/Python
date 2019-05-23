# (1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)

# Enter favorite color:
# yellow                                                                                                                                                         
# Enter pet's name:
# Daisy                                                                                                                                                
# Enter a number:
# 6
# You entered: yellow Daisy 6

# (2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).

# Enter favorite color:
# yellow                                                                                                                                                         
# Enter pet's name:
# Daisy                                                                                                                                                   
# Enter a number:
# 6
# You entered: yellow Daisy 6

# First password: yellow_Daisy
# Second password: 6yellow6

# (3) Output the length of each password (the number of characters in the strings). (Submit for 2 points, so 5 points total).

# Enter favorite color:
# yellow                                                                                                                                                         
# Enter pet's name:
# Daisy                                                                                                                                                   
# Enter a number:
# 6
# You entered: yellow Daisy 6

# First password: yellow_Daisy
# Second password: 6yellow6

# Number of characters in yellow_Daisy: 12
# Number of characters in 6yellow6: 8


# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pets_name = input('Enter pet\'s name:\n')
a_number = int(input('Enter a number:\n'))

print('You entered:', favorite_color, pets_name, a_number)


# FIXME (2): Output two password options
password1 = favorite_color
print('\nFirst password: %s_%s' % (favorite_color, pets_name))
print('Second password: %d%s%d' % (a_number, favorite_color, a_number))

# FIXME (3): Output the length of the two password options.
# Output all the values on a single line.

pass1 = favorite_color + '_' + pets_name
pass2 = str(a_number) + favorite_color + str(a_number)

p_len1 = len(pass1)
p_len2 = len(pass2)

print('\nNumber of characters in %s: %d' % (pass1, p_len1))
print('Number of characters in %s: %d' % (pass2, p_len2))