# Day 25: Create a program to concatenate two lists.

import ast

def concat_two_lists(list_1, list_2):
    user_list_1 = ast.literal_eval(list_1)
    user_list_2 = ast.literal_eval(list_2)
    user_list_1.extend(user_list_2)
    return user_list_1

if __name__ == "__main__":
    user_input_1 = input('Enter your first list:')
    user_input_2 = input('Enter your second list:')
    print(concat_two_lists(user_input_1, user_input_2))