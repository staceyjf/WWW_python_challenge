# Day 19 : Write a function to calculate the factorial of a number.

# Factorials
# Must be positive
# Must be Int
# 0! is 1

# can use import Math math.factorial()

#user input
def get_user_input_19():
    try:
        user_input = input('Enter your number:')
        if user_input.isdigit() and user_input != '': #input is a whole number and not empty
            return int(user_input)
        else:
            return None
    except:
        return None

def calculate_factorial(user_input):
    if isinstance(user_input, int) and user_input > 0:
        total = 1
        for number in range(2,user_input + 1):
            print(number)
            total *= number
        return total
    elif user_input == 0 or  user_input == 1:
        return 1
    else:
        print('Invalid input')
        return None

if __name__ == "__main__":
    user_input = get_user_input_19()
    print(calculate_factorial(user_input))