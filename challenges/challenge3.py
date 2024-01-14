# Day 3 : Write a function to count the number of vowels in a given string

# This script takes a string and counts the number of vowels

def count_vowels(input_str):
    try:
        vowels = ["a","e","i","o","u"]
        result = sum(map(lambda x: (input_str.lower()).count(x), vowels))
        print(result)
        return result
    except:
        return 'Invalid input. Please enter a word.'

def get_user_input():
    try:
        user_input = input('Enter a word:')
        # catches the case if they add numbers as it won't be caught in the except block
        if user_input.isnumeric():
            print('Invalid input. Please enter a word.')
            return None
        else:
            return user_input
    except ValueError as e:
        print(e)
        return None
