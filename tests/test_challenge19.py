import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge19 import get_user_input_19, calculate_factorial

# test cases 
def test_calculate_factorial():
    #Test should return the factorial of a number
    assert calculate_factorial(4) == 24

    #Test should return None if a non-int is used
    assert calculate_factorial(6.2) == None

    # Test should return None if a negative int is used
    assert calculate_factorial(-5) == None

    # Test with a non-numeric input
    assert calculate_factorial('hello') == None

def test_get_user_input_19(monkeypatch):
    # Test should return a single digit
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert get_user_input_19() == 2

    # Test should return None if a float is used
    monkeypatch.setattr('builtins.input', lambda _: "2.2")
    assert get_user_input_19() == None

    # Test should return None if a non-numerical datatype have been included
    monkeypatch.setattr('builtins.input', lambda _: "Hello")
    assert get_user_input_19() == None

    # Test input function with no input
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert get_user_input_19() == None
