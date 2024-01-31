# Day 20 : Write a function that takes a list of numbers and returns a new list containing only the even numbers.

import ast

#user input
def get_user_input_20():
    try:
        user_input = input('Enter your list:')
        user_list = ast.literal_eval(user_input) #better practice than eval()

        if isinstance(user_list, list) and len(user_list) != 0 and all(isinstance(element, (int, float)) for element in user_list):
            return user_list
        else:
            print('Invalid input.')
            return None
    except:
        print('Invalid')
        return None

def even_nums_only(user_input):
    if isinstance(user_input, list):
        numbers = [element for element in user_input if isinstance(element,int)] #create a list of just numbers
        even_nums = [num for num in numbers if num % 2 == 0] #create a list of just even numbers
        return even_nums
    else:
        print('Invalid input')
        return None
    
if __name__ == "__main__":
    user_input = get_user_input_20()
    print(even_nums_only(user_input))