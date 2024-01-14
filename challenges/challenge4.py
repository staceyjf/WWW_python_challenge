# Day 4 : Write a program to find the sum of all elements in a list.

# This script takes a list and adds the number of elements contained within
def sum_of_list(input_list):
    try:
        # using list comprehesion to convert elms to str and then convert them to numbers before summing them
        result = sum([int(num) for num in map(str, input_list) if num.isdigit()])
        return result
    # raises the error when a function gets the correct data type but incorrect value eg int("ab")
    except ValueError:
        return 0

#user input
def get_user_input_4():
    try:
        user_input = input("Please enter your list:")
        #check that its a list takes types as 2nd param
        if isinstance(user_input, list):
            return user_input
        else:
            print('Invalid input. Please enter list.')
            return None   
    except ValueError as e:
        print(e)
        return None