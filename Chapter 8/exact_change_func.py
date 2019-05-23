# Write a program with total change amount as an integer input that outputs the change using the fewest coins, one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

# Ex: If the input is:
# 0 or less

# the output is:
# no change

# Ex: If the input is:
# 45

# the output is:
# 1 quarter
# 2 dimes

# Your program must define and call the following function. The function exact_change() should return num_dollars, num_quarters, num_dimes, num_nickels, and num_pennies.
# def exact_change(user_total)

# Note: This is a lab from a previous chapter that now requires the use of a function.


def exact_change(total):
    if total > 0:
        dollars = int(total / 100)
        total = total % 100
        
        quarters = int(total / 25)
        total = total % 25
        
        dimes = int(total / 10)
        total = total % 10
        
        nickels = int(total / 5)
        total = total % 5
        
        pennies = total
        
        return dollars, quarters, dimes, nickels, pennies
    else:
        return 0, 0, 0, 0, 0

if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print('no change')

    if num_dollars == 1:
        print('%d dollar' % (num_dollars))
    elif num_dollars > 0:
        print('%d dollars' % (num_dollars))
    
    if num_quarters == 1:
        print('%d quarter' % (num_quarters))
    elif num_quarters > 0:
        print('%d quarters' % (num_quarters))
    
    if num_dimes == 1:
        print('%d dime' % (num_dimes))
    elif num_dimes > 0:
        print('%d dimes' % (num_dimes))
    
    if num_nickels == 1:
        print('%d nickel' % (num_nickels))
    elif num_nickels > 0:
        print('%d nickels' % (num_nickels))
    
    if num_pennies == 1:
        print('%d penny' % (num_pennies))
    elif num_pennies > 0:
        print('%d pennies' % (num_pennies))