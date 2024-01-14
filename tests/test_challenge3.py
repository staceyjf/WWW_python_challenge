import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge3 import count_vowels, get_user_input

# test cases 
def test_count_vowels():
    #test a single string 
    assert count_vowels('hello') == 2

    #test multiple words in a string 
    assert count_vowels('hello world') == 3

    #test for no vowels
    assert count_vowels('123') == 0

    #test for no vowels
    assert count_vowels('') == 0

    #test for no-numerical input
    assert count_vowels(123) == 'Invalid input. Please enter a word.'

# Simulating user input
    # using monkeypatch to simulate user input - feature to modify behaviour of the input()
def test_get_user_input(monkeypatch):
    # Test input function with str input
    monkeypatch.setattr('builtins.input', lambda _: 'hello')
    assert get_user_input() == 'hello'

    #test for no vowels
    monkeypatch.setattr('builtins.input', lambda _: 'llll')
    assert get_user_input() == 'llll'

    # Test input function with a numeric input
    # Set input to return a numeric value
    monkeypatch.setattr('builtins.input', lambda _: '123')
    assert get_user_input() is None

    # Test input function with no input (empty line is returned which is represented by \n)
    monkeypatch.setattr('builtins.input', lambda _: '\n')
    assert get_user_input() == '\n'
