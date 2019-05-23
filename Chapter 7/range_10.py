# Write a program whose input is two integers. Output the first integer and subsequent increments of 10 as long as the value is less than or equal to the second integer.

# Ex: If the input is:
# -15 30

# the output is:
# -15 -5 5 15 25

# Ex: If the second integer is less than the first as in:
# 20 5

# the output is:
# Second integer can't be less than the first.

# For coding simplicity, output a space after every integer, including the last.


num1 = int(input())
num2 = int(input())

if num1 <= num2:
    for i in range(num1, num2 + 1,10):
        print(i, end = ' ')
    print()
else:
    print('Second integer can\'t be less than the first.')