# Day 29: Create a function that generates a random number between a given range.

import random

def random_num_generator(user_input_1, user_input_2):
    try:
        highest_num = int(user_input_2) #convert str to num
        lowest_num = int(user_input_1)

        if user_input_1 > user_input_2:
            highest_num = int(user_input_1)
            lowest_num = int(user_input_2)

        result = random.randrange(lowest_num, highest_num)

        return result
    except TypeError: #handles if the wrong number of arg is given
        print('There is a missing input')
        return None

if __name__ == "__main__":
    user_input_1 = input('Enter your first number:')
    user_input_2 = input('Enter your second number:')
    print(random_num_generator(user_input_1, user_input_2))