# (1) Prompt the user for a string that contains two strings separated by a comma. (1 pt)
# (2) Report an error if the input string does not contain a comma. Continue to prompt until a valid string is entered. Note: If the input contains a comma, then assume that the input also contains two strings. (2 pts) 
# (3) Using string splitting, extract the two words from the input string and then remove any spaces. Output the two words. (2 pts) 
# (4) Using a loop, extend the program to handle multiple lines of input. Continue until the user enters q to quit. (2 pts) 

# Ex:

# Enter input string:
# Jill, Allen
# First word: Jill
# Second word: Allen

# Enter input string:
# Golden , Monkey
# First word: Golden
# Second word: Monkey

# Enter input string:
# Washington,DC
# First word: Washington
# Second word: DC

# Enter input string:
# q

## 

while True:
        myStr=input('Enter input string:')
        print("\n".rstrip("\n"))
        if(myStr!='q'):          
            myStr=myStr.replace(' ', '')
            if ',' in myStr:
                
                myStr=myStr.split(',')
            
                print ('First word: ' + myStr[0])
                print ('Second word: ' + myStr[1])
                print("\n".rstrip("\n"))
            else:
                print('Error: No comma in string.\n')
        else:
          break