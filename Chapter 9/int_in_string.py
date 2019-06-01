# Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input, and outputs yes if every character is a digit 0-9.

# Ex: If the input is:
# 1995

# the output is:
# yes

# Ex: If the input is:
# 42,000

# or any string with a non-integer character, the output is:

# no

##

def isNumber(s) : 
      
    for i in range(len(s)) : 
        if s[i].isdigit() != True : 
            return False
  
    return True
  
if __name__ == "__main__" : 
    str  = input()
  
    if isNumber(str) : 
        print("yes") 
  
    else : 
        print("no") 