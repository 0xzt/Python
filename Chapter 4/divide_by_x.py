# Write a program using integers usernum and x as input, and output usernum divided by x four times.

# Ex: If the input is:

# 2000
# 2
# Then the output is:

# 1000 500 250 125
# Note: In Python 3, integer division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).


userNum = int(input())
x = int(input())

userNum = userNum // x
print(userNum, end=' ')
userNum = userNum // x
print(userNum, end=' ')
userNum = userNum // x
print(userNum, end=' ')
userNum = userNum // x
print(userNum)