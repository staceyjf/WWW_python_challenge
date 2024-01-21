# Day 8 : Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it

import re

def count_case(input_str):
    if isinstance(input_str, str):
        upper_count = len(re.findall("[A-Z]", input_str))
        lower_count = len(re.findall("[a-z]", input_str))
        return {'Uppercase': upper_count, 'Lowercase': lower_count}
    else:
        return "Invalid input"

#user input
def get_user_input_8():
    try:
        user_input = input("Please enter string")
        if isinstance(user_input,str):
            return user_input
        else:
            return None
    except ValueError as e:
        print(e)
        return None