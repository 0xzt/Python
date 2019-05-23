# Write a program whose inputs are three integers, and whose output is the largest of the three values.

# Ex: If the input is:

# 7
# 15
# 3
# the output is:

# 15

a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print(largest)