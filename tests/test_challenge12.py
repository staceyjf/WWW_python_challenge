import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge12 import get_user_input_12, reverse_string

def test_reverse_string():
    #Test should return a string with the chars reversed
    assert reverse_string('hello') == 'olleh'

    #Test should return a string with chars reversed for multiple words
    assert reverse_string("cat world") == "dlrow tac" 

    #Test should return None if a int is given
    assert reverse_string(2) == None

    #Test should return None if no input is given
    assert reverse_string('') == None

def test_get_user_input_12(monkeypatch):
    # Test should return a string from a string input
    monkeypatch.setattr('builtins.input', lambda _: 'hello')
    assert get_user_input_12() == 'hello'

    # Test should return None from a string input
    monkeypatch.setattr('builtins.input', lambda _: 1)
    assert get_user_input_12() == None

    # Test should return None from no input
    monkeypatch.setattr('builtins.input', lambda _: '')
    assert get_user_input_12() == None