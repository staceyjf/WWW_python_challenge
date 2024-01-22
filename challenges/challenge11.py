# Day 11 : Write a program to print the multiplication table of a given number.

#user input
def get_user_input_11():
    try:
        user_input = int(input('Enter a number:'))
        return user_input
    except ValueError:
        return None

def print_times_table(user_input):
    if user_input is not None and not isinstance(user_input, str):
        for num in range(1, 13):
            result = num * user_input
            print(f"{num} x {user_input} = {result}")
    else:
        return None

if __name__ == "__main__":
    user_input = get_user_input_11()
    print(print_times_table(user_input))