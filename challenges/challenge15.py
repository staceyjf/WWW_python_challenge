# Day 15 : Create a program that checks if a year is a leap year.

# Assumptions about leap years - every year that can be 
# divided by 4
# NOT divided by 100
# divided by 400  

#user input
def get_user_input_15():
    try:
        user_input = input('Please enter a year: ')
        length_input = list(user_input) #convert to a list to check length
        if len(length_input) == 4:
            return int(user_input)
        else:
            print(f'Invalid input')
            return None
    except  ValueError as e:
        print(f'Invalid input - {e}')
        return None

# could also look to return True and False which means i can return the expression instead of the if /else

def leap_year(user_input):
    length_str = str(user_input) #convert back to a string to check
    length_list = list(length_str ) #convert to a list to check length
    if isinstance(user_input, int)and len(length_list) == 4 : # need to be a year and a number
            if user_input % 4 == 0 and (user_input % 100 != 0 or user_input % 400 == 0):
                return'Leap Year'
            else:
                return 'Not a Leap Year'
    else:
        print(f'Invalid input')
        return None

if __name__ == "__main__":
    user_input = get_user_input_15()
    print(leap_year(user_input))