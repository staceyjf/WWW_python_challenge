# Day 5 : Write a program to find the maximum and minimum values in a list.

# This script takes a list and identifies the min and max values within it
def get_min_max_values(input_list):
    try:
        #if el in input list, is not an instance of a string, add el to num_list
        num_list = [el for el in input_list if not isinstance(el, str) ] 
        result = [min(num_list), max(num_list)]
        return result
    # if no numbers
    except ValueError as e:
        print(e)
        return None


#user input
def get_user_input_5():
    user_input = input('Enter a list to find the min and max values within it')
    try:
        #checking to see if it is a list
        if isinstance(user_input,list):
            return user_input
        else:
            print('Invalid entry. Please input a list')
            return None
    except ValueError as e:
        print(e)
        return None
