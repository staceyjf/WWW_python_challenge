import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge9 import get_user_input_9, check_odd_or_even

# test cases 
def test_check_odd_or_even():
    # Test should return even for even numbers
    assert check_odd_or_even(2) == "Even"

    # Test should return odd for odd numbers
    assert check_odd_or_even(-5) == "Odd"

    # Test should even despite it being a negative number
    assert check_odd_or_even(-4) == "Even"

    # Test should return zero if the input is zero
    assert check_odd_or_even(0) == "Zero"

    # Test should return None if the input is not a number
    assert check_odd_or_even('hello') == "Invalid input"

def test_get_user_input_9(monkeypatch):
    # Test should return a positive number
    monkeypatch.setattr('builtins.input', lambda _: 2)
    assert get_user_input_9() == 2

    # Test should return a negative number
    monkeypatch.setattr('builtins.input', lambda _: -5)
    assert get_user_input_9() == -5

    # Test should return zero 
    monkeypatch.setattr('builtins.input', lambda _: 0)
    assert get_user_input_9() == 0

    # Test should return none for str
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert get_user_input_9() == None
