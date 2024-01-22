# Day 12 : Write a program to reverse a given string.

#user input
def get_user_input_12():
    try:
        user_input = input('Enter string:')
        if isinstance(user_input, str) and user_input != '': #input is not empty or a number
            return user_input
        else:
            return None
    except AttributeError:
        return None

def reverse_string(user_input):
    if isinstance(user_input, str) and user_input != '':
        chars_list = list(user_input) #like split for python
        chars_list.reverse() #reverses in-place so not need to assign to a variable
        result = ''.join(chars_list)
        return result
    else:
        return None
    
# use slicing
    # def reverse(str1):
    # str1 = str1[::-1] - reassign, starts at the end and moves backwards step by step
    # return str1

if __name__ == "__main__":
    user_input = get_user_input_12()
    print(reverse_string(user_input))