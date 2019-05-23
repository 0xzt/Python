# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

# Ex: If the input is:
# 0, (or less than 0)

# the output is:
# no change 

# Ex: If the input is:
# 45

#the output is:
# 1 quarter
# 2 dimes 

total = int(input())

if total <= 0:
    print('no change')

if total > 0:
  dollars = int(total // 100)
  total = total % 100
   
  if dollars == 1:
    print('%d dollar' % (dollars))
  elif dollars > 0:
    print('%d dollars' % (dollars))

if total > 0:
  quarters = int(total // 25)
  total = total % 25
   
  if quarters == 1:
    print('%d quarter' % (quarters))
  elif quarters > 0:
    print('%d quarters' % (quarters))

if total > 0:
  dimes = int(total // 10)
  total = total % 10
   
  if dimes == 1:
    print('%d dime' % (dimes))
  elif dimes > 0:
    print('%d dimes' % (dimes))
    
if total > 0:
  nickels = int(total // 5)
  total = total % 5
   
  if nickels == 1:
    print('%d nickel' % (nickels))
  elif nickels > 0:
    print('%d nickels' % (nickels))
    
if total > 0:
  pennies = int(total // 1)
  total = total % 1
   
  if pennies == 1:
    print('%d penny' % (pennies))
  elif pennies > 0:
    print('%d pennies' % (pennies))
