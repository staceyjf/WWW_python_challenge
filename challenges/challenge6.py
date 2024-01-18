# Day 6 : Write a program to count the occurrences of a specific character in a string.

# This script counts counts the specific 
def get_char_count(user_input):
    try:
        # extracted strs from the tuple
        word =  user_input[0]
        char = user_input[1]
        return word.count(char)
    except:
        return None

#user input
def get_user_inputs_6():
    user_input_string = input('Enter a word')
    user_input_char = input('Enter a character which will be used to count the occurrences')
    try:
        #checking to see if it is a list
        if isinstance(user_input_string,str) and isinstance(user_input_char,str) :
            return (user_input_string, user_input_char)   
        else:
            print('Invalid entry. You have entered something other than a word')
            return None
    except ValueError as e:
        print(e)
        return None
