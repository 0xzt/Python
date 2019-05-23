# Note: When accuracy is essential, floats are not used to represent currency due to rounding and accumulation errors. Python provides several primitives specifically developed to implement financial applications. However, these topics are beyond the scope of this lab.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('%0.2f' % your_value)

# (1) Prompt the user to input a food item name, price, and quantity. Output an itemized receipt. (Submit for 2 points) 

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00
# (2) Extend the program to prompt the user for a second item. Output an itemized receipt. (Submit for 2 points, so 4 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00


# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# 4 ice cream @ $2.50 = $10.00
# Total cost: $20.00
# (3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost. Output the total cost, the cost of gratuity, and the grand total. To output the % symbol, enter %%. (Submit for 3 points, so 7 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00


# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# 4 ice cream @ $2.50 = $10.00
# Total cost: $20.00

# 15% gratuity: $3.00
# Total with tip: $23.00


first_item_name = str(input('Enter food item name:\n'))

# FIXME (1): Finish reading item price and quantity, then output a receipt
grand_total = 0

first_item_price = float(input('Enter item price:\n'))
first_item_qty = int(input('Enter item quantity:\n'))

total_item_cost = float(first_item_price * first_item_qty)

print('\nRECEIPT')
print('%d %s @ $%.2f = $%.2f' % (first_item_qty, first_item_name, first_item_price, total_item_cost))

grand_total += total_item_cost
print('Total cost: $%.2f\n' % grand_total)

# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
second_item_name = str(input('\nEnter second food item name:\n'))
second_item_price = float(input('Enter item price:\n'))
second_item_qty = int(input('Enter item quantity:\n'))

grand_total += second_item_price * second_item_qty

my_receipt = [(first_item_qty, first_item_name, first_item_price), (second_item_qty, second_item_name, second_item_price)]

print('\nRECEIPT')
for a, b, c in my_receipt:
    print('%d %s @ $%.2f = $%.2f' % (a, b, c, (float(a * c))))

print('Total cost: $%.2f' % grand_total)

# FIXME (3): Add a gratuity and total with tip to the second receipt
percent = '15%'
gratuity = grand_total * .15
new_grand_total = grand_total + gratuity
print('\n%s gratuity: $%.2f' % (percent, gratuity))
print('Total with tip: $%.2f' % new_grand_total)