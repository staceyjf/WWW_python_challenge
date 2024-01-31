# Day 20 : Write a function that takes a list of numbers and returns a new list containing only the even numbers.

#user input
def get_user_input_20():
    try:
        user_input = input('Enter your string:')
        if isinstance(user_input, str) and user_input != '': #input is not empty or a number
            return user_input
        else:
            return None
    except AttributeError:
        return None

def capitalize_words(user_input):
    if isinstance(user_input, str) and user_input != '': #not empty and a string
        result = ''
        for word in user_input.split():
            x = word.capitalize()
            result += x + ' '
        return result.rstrip()
    else:
        return None
    
if __name__ == "__main__":
    user_input = get_user_input_20()
    print(capitalize_words(user_input))