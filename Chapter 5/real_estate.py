# Sites like Zillow get input about house prices from a database and provide nice summaries for readers. Write a program with two inputs, current price and last month's price (both integers). Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage computed as (current_price * 0.045) / 12.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# Ex: If the input is:

# 200000 
# 210000

# the output is:

# This house is $200000. The change is $-10000 since last month. 
# The estimated monthly mortgage is $750.00.

# Note: Getting the precise spacing, punctuation, and newlines exactly right is a key point of this assignment. Such precision is an important part of programming.

currentPrice = int(input())
lastMonthsPrice = int(input())
mortgage = float(currentPrice * 0.045)/12

print('This house is $',currentPrice,'.', ' The change is $',(currentPrice-lastMonthsPrice), ' since last month.', sep = '')
print('The estimated monthly mortgage is $',('%0.2f'%mortgage),'.', sep = '')