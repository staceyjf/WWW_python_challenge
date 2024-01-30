import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge17 import get_user_input_17,capitalize_words

def test_capitalize_words():
    #Test should return a string with a captialised first char for a sentence 
    assert capitalize_words("it's a cat world") == "It's A Cat World" 

    #Test should return a string with a captialised first char
    assert capitalize_words('hello') == 'Hello'

    #Test should return None if a int is given
    assert capitalize_words(7) == None

    #Test should return None if no input is given
    assert capitalize_words('') == None

def test_get_user_input_17(monkeypatch):
    # Test should return a string from a string input
    monkeypatch.setattr('builtins.input', lambda _: 'hello')
    assert get_user_input_17() == 'hello'

    # Test should return None from a string input
    monkeypatch.setattr('builtins.input', lambda _: 1)
    assert get_user_input_17() == None

    # Test should return None from no input
    monkeypatch.setattr('builtins.input', lambda _: '')
    assert get_user_input_17() == None