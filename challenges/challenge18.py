# Day 18 : Create a program to find the largest among three numbers.

#user input
def get_user_inputs_18():
    try:
        input_1 = input('Enter your first number:')
        input_2 = input('Enter your second number:')
        input_3 = input('Enter your third number:')
        user_input = [float(input_1), float(input_2), float(input_3)]

        if len(user_input) == 3:
            return user_input
        else:
            print('Invalid input')
            return None
    except: #captures typeErrors (operation applied to inappropriate type) and ValueError (trying to convert input to int)
        return None

def find_biggest_num(user_input):
    if all(isinstance(element, (int, float)) for element in user_input) and len(user_input) == 3: 
        # is a list contains numbers and not empty
        return max(user_input)
    else:
        return None
    
if __name__ == "__main__":
    user_input = get_user_inputs_18()
    print(find_biggest_num(user_input))