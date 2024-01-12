import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge2 import area_Circle, get_user_input

# test cases 
def test_area_Circle():
    #test with numbers as inputs
    assert area_Circle(5) == 78.54

    # Test with a radius of 0
    assert area_Circle(0) == 0

    # Test with no input
    assert area_Circle(None) == 'No input provided'

    # Test with a non-numeric input
    assert area_Circle('hello') == 'Invalid input. Please enter a numeric value.'

# using monkeypatch to simulate user input - feature to modify behaviour of the input()
def test_get_user_input(monkeypatch):
    # Test input function with numeric input
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_user_input() == 5

    # Test input function with non-numeric input
    # Set input to return a non-numeric value
    monkeypatch.setattr('builtins.input', lambda _: 'hello')
    assert get_user_input() == None

    # Test input function with no input
    monkeypatch.setattr('builtins.input', lambda _: '')
    assert get_user_input() == None
