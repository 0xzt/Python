# A pedometer treats walking 2,000 steps as walking 1 mile. Write a program whose input is the number of steps, and whose output is the miles walked.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# Ex: If the input is:
# 5345

# the output is:
# 2.67

# Your program must define and call the following function:
# def steps_to_miles(user_steps)


def steps_to_miles(user_steps):
    steps_to_miles = user_steps / 2000.00
    return steps_to_miles

if __name__ == '__main__':
    user_steps = float(input())
    miles_walked = steps_to_miles(user_steps)
    print('%0.2f' % miles_walked)