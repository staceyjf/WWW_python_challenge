# Day 28: Create a program that removes the nth element from a list.

import ast

def remove_nth_el(user_input_1, user_input_2):
    try:
        user_list = ast.literal_eval(user_input_1) #convert string into list
        user_nth = int(user_input_2) #convert string into int
        if 1 <= user_nth <= len(user_list): # if its a valid index
            user_list.pop(user_nth-1) #convert user number to index
            return user_list
        else:
            print('Number is out of index range')
            return None
    except:
        print('Invalid input')
        return None

if __name__ == "__main__":
    user_input_1 = input('Enter your list:')
    user_input_2 = input('Enter a value for nth:')
    print(remove_nth_el(user_input_1, user_input_2))