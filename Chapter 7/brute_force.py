# Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients of two linear equations with variables x and y, use brute force to find an integer solution for x and y in the range -10 to 10.

# Ex: If the input is:
# 8
# 7
# 38
# 3
# -5
# -1

# Then the output is:
# 3 2

# Use this brute force approach:

# For every value of x from -10 to 10
#    For every value of y from -10 to 10
#      Check if the current x and y satisfy both equations. If so, output the solution, and finish.

# Ex: If no solution is found, output:
# No solution

# You can assume the two equations have no more than one solution.
# Note: Elegant mathematical techniques exist to solve such linear equations. However, for other kinds of equations or situations, brute force can be handy.


#ax + by = c
a = int(input())
b = int(input())
c = int(input())

#dx + ey = f
d = int(input())
e = int(input())
f = int(input())

flag = False

for x in range(-10,10):
    for y in range(-10,10):
        if ((a*x)+(b*y)==c) and ((d*x)+(e*y)==f):
            print(x,y)
            flag = True
        
if flag == False:
    print('No solution')