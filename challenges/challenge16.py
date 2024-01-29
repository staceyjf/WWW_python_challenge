# Day 16 : Write a function that counts the frequency of each word in a sentence.

#user input
def get_user_inputs_16():
    try:
        user_input_sentence = input('Please enter sentence: ')
        user_input_word = input('Please enter word: ')
        if (user_input_sentence is not None and user_input_word is not None) and (isinstance(user_input_sentence, str) and isinstance(user_input_word, str)):
            return [user_input_sentence, user_input_word]
        else:
            print('Invalid input')
            return None
    except  ValueError as e:
        print(f'Invalid input - {e}')
        return None

def count_words(user_input): #returned as a list
    if len(user_input) > 0:
        return user_input[0].count(user_input[1])
    else:
        print('Invalid input')
        return None

if __name__ == "__main__":
    user_input = get_user_inputs_16()
    print(count_words(user_input))