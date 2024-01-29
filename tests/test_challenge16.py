import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge16 import get_user_inputs_16, count_words

def test_count_words():
    # Test should return the count of words in a sentence
    assert count_words(['There are many many words', 'many']) == 2

    # Test should return  zero if the cases don't match
    assert count_words(['There are many many words', 'Many']) == 0

    # Test should return zero if there are no matching words
    assert count_words(['Hello there stranger', 'tomato']) == 0

    # Test should return 'None' if no inputs are given 
    assert count_words([]) == None

def test_get_user_input_16(monkeypatch):

    # Store simulated inputs in a list
    inputs = iter(['There are many many words', 'words'])
    # Monkeypatch input function to return values from the list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Test should return a list of two strings
    assert get_user_inputs_16() == ['There are many many words', 'words']

    # Test should return None if there is only one element entered
    inputs = iter(['hello world'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs, None))
    assert get_user_inputs_16() is None

    # Test should return None if the input sentence is not a string
    inputs = iter([222, 'cow'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_user_inputs_16() is None

    # Test should return None if the input word is not a string
    inputs = iter(['She said goodbye to the world', 1111])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_user_inputs_16() is None

    # Test input function with no input
    inputs = iter([])
    monkeypatch.setattr('builtins.input', lambda _: [])
    assert get_user_inputs_16() is None