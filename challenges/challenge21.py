# Day 21 : Create a program to remove a specific element from a set.

#user input
def get_user_input_21():
    try:
        user_input_1 = input('Enter your set (separate each element with a comma): ')
        user_input_2 = input('Enter the element you want to remove: ')

        # Split the input string by commas and convert each element to its appropriate type
        user_set = set()
        for element in user_input_1.split(','):
            element = element.strip()  # Strip leading and trailing spaces
            try:
                # Try to convert to int
                user_set.add(int(element))
            except ValueError:
                # Otherwise, convert to string
                user_set.add(element)
       
       # If string is a number, convert to int
        try:
            user_el = int(user_input_2)
        except ValueError:
            user_el = user_input_2

        if len(user_set) != 0 and user_el:
            return user_set, user_el
        else:
            print('Invalid input.')
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None

def remove_el_from_list(user_input):
    user_input[0].remove(user_input[1])
    print(user_input[0])
    return user_input[0]
    
if __name__ == "__main__":
    user_input = get_user_input_21()
    print(remove_el_from_list(user_input))