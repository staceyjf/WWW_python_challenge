import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge18 import get_user_inputs_18, find_biggest_num

# test cases 
def test_find_biggest_num():
    #Test should return the biggest number from three numbers
    assert find_biggest_num([1,22,3]) == 22

    #Test should return the biggest number including floats
    assert find_biggest_num([1,22,22.3]) == 22.3

    # Test should return None if less than three numbers are given
    assert find_biggest_num([4,2]) == None

    # Test with a non-numeric input
    assert find_biggest_num(['hello', 2, 3]) == None

# using monkeypatch to simulate user input - feature to modify behaviour of the input()
def test_get_user_inputs_18(monkeypatch):
    # Store simulated inputs in a list
    inputs = iter(["1","22","3"])
    # Monkeypatch input function to return values from the list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Test should return a list of three numbers
    assert get_user_inputs_18() == [1,22,3]

    # Test should return None if there is only one element entered
    inputs = iter(["4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs, None))
    assert get_user_inputs_18() is None

    # Test should return None if non-numerical datatypes have been included
    inputs = iter(["222", 'cow', "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_user_inputs_18() is None

    # Test input function with no input
    inputs = iter([])
    monkeypatch.setattr('builtins.input', lambda _: [])
    assert get_user_inputs_18() is None
