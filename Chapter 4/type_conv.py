# (1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into separate variables. Then, output those four values on a single line separated by a space. (Submit for 2 points). 

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy

# (2) Extend to also output in reverse. (Submit for 1 point, so 3 points total).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99

# (3) Extend to convert the integer to a character by using the 'chr()' function, and output that character. (Submit for 2 points, so 5 points total).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99
# 99 converted to a character is c

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
i = int(input('Enter integer (32 - 126):\n'))
f = float(input('Enter float:\n'))
c = str(input('Enter character:\n'))
s = str(input('Enter string:\n'))

print(i, f, c, s)
   
# FIXME (2): Output the four values in reverse
print(s, c, f, i)

# FIXME (3): Convert the integer to a characer, and output that character
char_value = chr(i)
print(i, 'converted to a character is ' + char_value)