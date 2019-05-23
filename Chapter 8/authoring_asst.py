# (1) Prompt the user to enter a string of their choosing. Store the text in a string. Output the string. (1 pt) 

# Ex:

# Enter a sample text:
# we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

# You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

# (2) Implement a print_menu() function, which has a string as a parameter, outputs a menu of user options for analyzing/editing the string, and returns the user's entered menu option and the sample text string (which can be edited inside the print_menu() function). Each option is represented by a single character.

# If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement the Quit menu option before implementing other options. Call print_menu() in the main section of your code. Continue to call print_menu() until the user enters q to Quit. (3 pts) 

# Ex:

# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit

# Choose an option:

# (3) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string parameter and returns the number of characters in the string, excluding all whitespace. Call get_num_of_non_WS_characters() in the print_menu() function. (4 pts) 

# Ex:

# Number of non-whitespace characters: 181

# (4) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns the number of words in the string. Hint: Words end when a space is reached except for the last word in a sentence. Call get_num_of_words() in the print_menu() function. (3 pts) 

# Ex:

# Number of words: 35

# (5) Implement the fix_capilization() function. fix_capilization() has a string parameter and returns an updated string, where lowercase letters at the beginning of sentences are replaced with uppercase letters. fix_capilization() also returns the number of letters that have been capitalized. Call fix_capilization() in the print_menu() function, and then output the number of letters capitalized and the edited string. Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty string and use string concatenation to make edits to the string. (3 pts) 

# Ex:

# Number of letters capitalized: 3
# Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!

# (6) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword argument parameters exclamation_count and semicolon_count. replace_punctuation() updates the string by replacing each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,). replace_punctuation() also counts the number of times each character is replaced and outputs those counts. Lastly, replace_punctuation() returns the updated string. Call replace_exclamation() in the print_menu() function, and then output the edited string. (3 pts) 

# Ex:

# Punctuation replaced
# exclamation\_count: 1
# semicolon\_count: 2
# Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.

# (7) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by replacing all sequences of 2 or more spaces with a single space. shorten_space() returns the string. Call shorten_space() in the print_menu() function, and then output the edited string. Hint: Look up and use Python function .isspace(). (3 pt) 

# Ex:

# Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes, more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!


import re

def get_num_of_non_WS_characters(usr_str):
    no_white_sp = usr_str.replace(' ', '')
    return len(no_white_sp)

def get_num_of_words(usr_str):
    my_list = list(usr_str.split())
    return len(my_list)

def fix_capilization(usr_str):
    new_str = str()
    new_list = list(re.split(r'(?<=\.) ', usr_str))
    for n in new_list:
        mod_str = n.lstrip()
        new_str += mod_str.capitalize()
        new_str += ' '
    return new_str

def replace_punctuation(usr_str, exclamation_count=0, semicolon_count=0):
    som_str = str()
    for n in usr_str:
        if n == '!':
            som_str += '.'
            exclamation_count += 1
        elif n == ';':
            som_str += ','
            semicolon_count += 1
        else:
            som_str += n
    print('\nexclamation\_count: %d' % exclamation_count)
    print('semicolon\_count: %d' % semicolon_count)
    return som_str

def shorten_space(usr_str):
    return " ".join(usr_str.split())

def print_menu(usr_str):
    menu_op = ' '
    while menu_op != 'q':
        print('\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Fix capitalization\nr - Replace punctuation\ns - Shorten spaces\nq - Quit')
        menu_op = str(input('\nChoose an option:\n'))

        if menu_op == 'c':
            c_var = get_num_of_non_WS_characters(usr_str)
            print('\nNumber of non-whitespace characters: %d' % c_var)
        if menu_op == 'w':
            w_var = get_num_of_words(usr_str)
            print('\nNumber of words: %d' % w_var)
        if menu_op == 'f':
            f_var = fix_capilization(usr_str)
            print('\nEdited text: %s' % f_var)
        if menu_op == 'r':
            r_var = replace_punctuation(usr_str)
            print('Edited text: %s' % r_var)
        if menu_op == 's':
            s_var = shorten_space(usr_str)
            print('\nEdited text: %s' % s_var)
        # return menu_op, usr_str

if __name__ == '__main__':
    my_text = str(input('Enter a sample text:\n'))
    print('\nYou entered: %s' % my_text)
    print_menu(my_text)