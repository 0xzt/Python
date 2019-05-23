# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, the 405 services the 5, and the 290 services the 90.

# Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

# Ex: If the input is:
# 90

# the output is:
# The 90 is primary, going east/west.

# Ex: If the input is:
# 290

# the output is:
# The 290 is auxiliary, serving the 90, going east/west.

# Ex: If the input is:
# 0

# the output is:
# 0 is not a valid interstate highway number. 


num = int(input())

if num in range (1,99):
   if num % 2 == 0:
      print('The ', num, ' is primary, going east/west.', sep = ''.format(num))
   else:
      print('The ', num, ' is primary, going north/south.', sep = ''.format(num))
elif num in range (100,999):
   if num % 2 == 0:
      print('The ' , num, ' is auxiliary, serving the ', num % 100, ',', ' going east/west.', sep = ''.format(num))
   else:
      print('The ' , num, ' is auxiliary, serving the ', num % 100, ',', ' going north/south.', sep = ''.format(num))
else:
    print(num,' is not a valid interstate highway number.', sep = ''.format(num))
