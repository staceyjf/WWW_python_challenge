# Day 26: Create a program that uses a lambda function to square each element of a list.

import ast

def square_each_el(list_1):
    user_list = ast.literal_eval(list_1) #convert string into list
    result = map(lambda el: el**2, user_list) # for each el in user_list, i will square it
    return list(result) #convert back into list

if __name__ == "__main__":
    user_input_1 = input('Enter your list:')
    print(square_each_el(user_input_1))