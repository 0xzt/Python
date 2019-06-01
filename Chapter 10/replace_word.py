# Write a program that replaces words in a sentence. The input begins with word replacement pairs (original and replacement). The next line of input is the sentence where any word on the original list is replaced.

# Ex: If the input is:
# automobile car   manufacturer maker   children kids
# The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.

# the output is:
# The car maker recommends car seats for kids if the car doesn't already have one. 
# You can assume the original words are unique.

##

user_input = input()
new_list = user_input.split()
my_list = new_list

other_input = input()
nuevo_list = other_input.split()
mio_list = nuevo_list

for x in my_list[::2]:
    mio_list = [n.replace(x,my_list[(my_list.index(x) + 1)]) for n in mio_list]

strbl = ''
for n in mio_list[:-1]:
    strbl += n + ' '

strbl += mio_list[-1]

print(strbl)