# A “jiffy” is the scientific name for 1/100th of a second. Given an input number of seconds, output the number of "jiffies."

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# Ex: If the input is:
# 15

# the output is:
# 1500.00

# Your program must define and call the following function:
# def seconds_to_jiffies(user_seconds)

def seconds_to_jiffies(user_seconds):
    jiffy = float(user_seconds) * 100.0
    return jiffy
    
if __name__ == '__main__':
    val = float(input())
    jiffies = seconds_to_jiffies(val)
    print('%0.2f' % jiffies)