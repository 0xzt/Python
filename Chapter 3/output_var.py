# A variable like usernum can store a value like an integer. Extend the given program to print usernum values as indicated. (Submit for 2 points).

# (1) Output the user's input. 
# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# Enter integer:
# 4
# You entered: 4

# (2) Extend to output the input squared and cubed. *Hint: Compute squared as usernum * usernum.* (Submit for 2 points, so 4 points total).

# Enter integer:
# 4
# You entered: 4
# 4 squared is 16 
# And 4 cubed is 64 !! 

# (3) Extend to get a second user input into user_num2. Output sum and product. (Submit for 1 point, so 5 points total).

# Enter integer:
# 4
# You entered: 4
# 4 squared is 16 
# And 4 cubed is 64 !!
# Enter another integer:
# 5
# 4 + 5 is 9
# 4 * 5 is 20

userNum = int(input('Enter integer:\n'))
print("You entered:", userNum)
print(userNum, "squared is", userNum*userNum)
print("And", userNum, "cubed is", userNum*userNum*userNum, "!!")
userNum2 = int(input('Enter another integer:\n'))
print('4 + 5 is 9')
print('4 * 5 is 20')