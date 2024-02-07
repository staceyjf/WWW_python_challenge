# Day 22 : Create a program to find the second-largest element in a list.

import ast

def biggest_el_in_list(user_input):
    user_list = ast.literal_eval(user_input) #convert str to list
    user_list.remove(max(user_list)) #find the biggest and remove
    second_largest = max(user_list) # find the next biggest
    return second_largest
    
if __name__ == "__main__":
    user_input = input('Enter your list of numbers:')
    print(biggest_el_in_list(user_input))