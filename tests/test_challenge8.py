import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge8 import get_user_input_8, count_case

# test cases 
def test_count_case():
    # Test should return the count of upper and lowercase letters
    assert count_case('Hello') == {'Uppercase': 1, 'Lowercase': 4}

    # Test should return zero if there are no uppercase words alongside the lowercase count
    assert count_case('cat') == {'Uppercase': 0, 'Lowercase': 3}

     # Test should return zero if there are no lowercase words alongside the uppercase count
    assert count_case('THERE') == {'Uppercase': 5, 'Lowercase': 0}

    # Test should return None if the input is not a string
    assert count_case(1234) == "Invalid input"

def test_get_user_input_8(monkeypatch):
    # Test should return matched string 
    monkeypatch.setattr('builtins.input', lambda _: 'Hello')
    assert get_user_input_8() == 'Hello'

    #Test should return str with lowercase included
    monkeypatch.setattr('builtins.input', lambda _: 'hello')
    assert get_user_input_8() == 'hello'

    # Test should return none if input is not a string
    monkeypatch.setattr('builtins.input', lambda _: 123)
    assert get_user_input_8() is None

    # Test should return if there is no input (empty line is returned which is represented by \n)
    monkeypatch.setattr('builtins.input', lambda _: '\n')
    assert get_user_input_8() == '\n'
