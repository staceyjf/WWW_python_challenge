# Day 13 : Write a program to shuffle the elements of a list randomly.
import random 

#user input
def get_user_input_13():
    try:
        user_input = input('Enter a list:').strip()
        if user_input.startswith("[") and user_input.endswith("]"):
            return eval(user_input)
        else:
            print('Invalid input. Please enter a valid list.')
    except SyntaxError:
        print('Invalid input. Please enter a valid list.')
    return None

def shuffle(input_list):
    if not isinstance(input_list, list): #in the case of string or numbers
        return None
    
    shuffled_list = input_list.copy() #create a copy to avoid modifying the original
    random.shuffle(shuffled_list) #shuffles happens in-place
    return shuffled_list

if __name__ == "__main__":
    input_list = get_user_input_13()
    print(shuffle(input_list))