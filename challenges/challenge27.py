# Day 27: Create a program that sorts a list of strings alphabetically.

import ast

def sort_list_alphabetically(list_1):
    user_list = ast.literal_eval(list_1) #convert string into list
    user_list.sort() #convert back into list
    return user_list #sorts in place so return None

if __name__ == "__main__":
    user_input_1 = input('Enter your list:')
    print(sort_list_alphabetically(user_input_1))