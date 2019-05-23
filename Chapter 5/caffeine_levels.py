# A half-life is the amount of time it takes for a substance or entity to fall to half its original value. Caffeine has a half-life of about 6 hours in humans. Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, and 18 hours. Use a string formatting expression with conversion specifiers to output the caffeine amount as floating-point numbers.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# Ex: If the input is:

# 100
# the output is:

# After 6 hours: 50.00 mg
# After 12 hours: 25.00 mg
# After 18 hours: 12.50 mg
# Note: A cup of coffee has about 100 mg. A soda has about 40 mg. An "energy" drink (a misnomer) has between 100 mg and 200 mg.

caffeine_mg = float(input())
halflife = .50
caffeine = caffeine_mg * halflife

hour6 = 'After 6 hours: ' + '%0.2f' % caffeine
hour12 = 'After 12 hours: ' + '%0.2f' % (caffeine / 2)
hour18 = 'After 18 hours: ' + '%0.2f' % (caffeine / 4)


print(hour6 + ' mg')
print(hour12 + ' mg')
print(hour18 + ' mg')