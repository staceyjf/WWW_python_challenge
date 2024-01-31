# Day 19 : Write a function to calculate the factorial of a number.

#user input
def get_user_input_19():
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
    user_input = get_user_input_19()
    print(capitalize_words(user_input))