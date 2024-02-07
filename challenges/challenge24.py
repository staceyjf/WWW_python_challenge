# Day 24: Write a program to remove vowels from a given string.


def check_for_key(user_input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in user_input: #get the chars  
        if char not in vowels: #check if they are in vowels list
            result += char #concatenate the chars
    return result

if __name__ == "__main__":
    user_input = input('Enter a string:')
    print(check_for_key(user_input))