# Day 23: Write a program that checks if a key exists in a dictionary.

import ast

def check_for_key(user_dic, user_key):
    dic_to_check = ast.literal_eval(user_dic)

    if user_key in dic_to_check.keys(): #convert the keys to a list and check if the user_key is in the list
        print('Yes it is')
        return True
    else:
        print('No it is not')
        return False

if __name__ == "__main__":
    user_dic = input('Enter dictionary:')
    user_key = input('Enter key to check:')
    print(check_for_key(user_dic, user_key))