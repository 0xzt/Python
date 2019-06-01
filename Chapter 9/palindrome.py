# A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

# Ex: If the input is:
# bob

# the output is:
# bob is a palindrome

# Ex: If the input is:
# bobby

# the output is:
# bobby is not a palindrome

# Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

##

def reverse(x):
    return x[::-1]
  
def palindrome(y): 
    rev = reverse(y)
    if y.replace(' ', '') == rev.replace(' ', ''):
        return True
    else:
        return False
  
s = input()
ans = palindrome(s)
  
if ans == 1: 
    print(s + ' is a palindrome') 
else: 
    print(s + ' is not a palindrome') 