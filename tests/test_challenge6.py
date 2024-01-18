import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge6 import get_user_inputs_6, get_char_count

def test_get_char_count():
    #test should return the number of instances of the char in the word
    assert get_char_count(('hello word', 'l')) == 2

    #test should return zero if only input_word is provided
    assert get_char_count(('hello word')) == 0

    #test should return none if input_word is a num
    assert get_char_count((2, 'l')) == None

    #test should return none if input_char is a num
    assert get_char_count(('hello', 1)) == None

def test_get_user_inputs_6(monkeypatch):
    # Test should return a tuple of two strings
    # Store simulated inputs in a list
    inputs = iter(['hello', 'l'])
    # Monkeypatch input function to return values from the list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Test should return a tuple of two strings
    assert get_user_inputs_6() == ('hello', 'l')

    # Test should return None if there is only one element in the tuple
    #/n simulates enter
    monkeypatch.setattr('builtins.input', lambda _: ['hello world'])
    assert get_user_inputs_6() is None

    # Test should return None if the input word is not a string
    inputs = iter([2,'l'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_user_inputs_6() is None

    # Test should return None if the input char is not a string
    inputs = iter(['hello',2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_user_inputs_6() is None

    # Test input function with no input (empty line is returned which is represented by \n)
    inputs = iter([])
    monkeypatch.setattr('builtins.input', lambda _: [])
    assert get_user_inputs_6() is None