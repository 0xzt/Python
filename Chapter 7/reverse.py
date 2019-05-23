# Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Quit", "quit", or "q" for the line of text.

# Ex: If the input is:
# Hello there
# Hey
# quit

# then the output is:
# ereht olleH
# yeH

text = input()

while text != 'q' and text != 'quit' and text != 'Quit':
    print(text[::-1])
    text=input()
