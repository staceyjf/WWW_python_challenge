import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge13 import get_user_input_13, shuffle

def test_shuffle():
    # Test should return a random order for the list
    original_list = [1, 2, 3, 4, 7, 8]
    shuffled_list = shuffle(original_list[:])  # Make a copy before shuffling
    assert shuffled_list != original_list

    # Test should return a random order with mixed datatypes
    original_list = ["hello", "there", 2, 4]
    shuffled_list = shuffle(original_list[:])  # Make a copy before shuffling
    assert shuffled_list != original_list

    # Test should return empty if the supplied list is empty
    assert shuffle([]) == []

    # Test should return None if a string is supplied
    assert shuffle('hello') == None

    # Test should return None if a number is supplied
    assert shuffle(2) == None


def test_get_user_input_13(monkeypatch):
    # Test should return numbers in a list
    monkeypatch.setattr('builtins.input', lambda _: '[1, 1]')
    assert get_user_input_13() == [1, 1]

    # Test should return mixed datatype list
    monkeypatch.setattr('builtins.input', lambda _: '["cat", 2, 2, 2, 2]')
    assert get_user_input_13() == ["cat", 2, 2, 2, 2]

    # Test should return None if the input is a string
    monkeypatch.setattr('builtins.input', lambda _: "I'm not a list")
    assert get_user_input_13() == None

    # Test should return None if the input is a number
    monkeypatch.setattr('builtins.input', lambda _: '123')
    assert get_user_input_13() == None

    # Test input function with no input 
    monkeypatch.setattr('builtins.input', lambda _: '')
    assert get_user_input_13() == None