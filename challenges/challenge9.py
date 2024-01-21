# Day 9 : Write a program to check if a number is even or odd.

def check_odd_or_even(n):
    if isinstance(n, str):
        return "Invalid input"
    elif n == 0:
        return 'Zero'
    elif n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
     
#user input
def get_user_input_9():
    try:
        user_input = int(input("Please enter a number"))
        if isinstance(user_input,int):
            return user_input
        else:
            return None
    except ValueError as e:
        print(e)
        return None