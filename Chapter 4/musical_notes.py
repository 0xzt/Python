# On a piano, a key has a frequency, say f0. Each higher key (black or white) has a frequency of f0 * rn, where n is the distance (number of keys) from that key, and r is 2(1/12). Given an initial key frequency, output that frequency and the next 4 higher key frequencies.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f %0.2f %0.2f %0.2f %0.2f' % (your_value1, your_value2, your_value3, your_value4, your_value5))

# Ex: If the input is:

# 440
# (which is the A key near the middle of a piano keyboard), the output is:

# 440.00 466.16 493.88 523.25 554.37
# Note: Use one statement to compute r = 2(1/12) using the pow function (remember to import the math module). Then use that r in subsequent statements that use the formula fn = f0 * rn with n being 1, 2, 3, and finally 4.

import math

initialKey = float(input())
#frequency = initialKey * math.pow(r, n)
n = 4
r = 2**1/12

key_1 = (initialKey)
key_2 = (key_1 * math.pow(2, 1/12))
key_3 = (key_2 * math.pow(2, 1/12))
key_4 = (key_3 * math.pow(2, 1/12))
key_5 = (key_4 * math.pow(2, 1/12))


print('%0.2f %0.2f %0.2f %0.2f %0.2f' % (key_1, key_2, key_3, key_4, key_5))