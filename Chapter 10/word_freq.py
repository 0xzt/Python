# Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

# Ex: If the input is:
# hey hi Mark hi mark

# the output is:
# hey 1
# hi 2
# Mark 1
# hi 2
# mark 1

##

def freq(str): 
    str = str.split()          
    str2 = []
    
    for i in str:
        #if i not in str2: // to check for duplicates in string
            str2.append(i)  
              
    for i in range(0, len(str2)): 
        print(str2[i], str.count(str2[i]))
  
def main(): 
    str = input()
    freq(str)                     
  
if __name__=="__main__": 
    main()