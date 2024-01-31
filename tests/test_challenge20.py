import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge20 import get_user_input_20, even_nums_only

# test cases 
def test_even_nums_only():
    #Test should return a list of even postive int
    assert even_nums_only([1,2,3,4,5]) == [2,4]

    #Test should exlude floats and return int even numbers
    assert even_nums_only([1.2, 2.4, 3.9, 4, 5]) == [4]

    # Test should return a list of even int that include negative numbers
    assert even_nums_only([-2,2,3,4,6,-8]) == [-2,2,4,6,-8]

    # Test with a non-numeric input
    assert even_nums_only('hello') == None

def test_get_user_input_20(monkeypatch):
    # Test should return a list of Int
    monkeypatch.setattr('builtins.input', lambda _: "[1, 2, 3, 4, 5]")
    assert get_user_input_20() == [1,2,3,4,5]

    # Test should return a list including floats
    monkeypatch.setattr('builtins.input', lambda _: "[1.2, 2.4, 3.9, 4, 5]")
    assert get_user_input_20() == [1.2, 2.4, 3.9, 4, 5] 

    # Test should return None if a non-numerical datatype have been included
    monkeypatch.setattr('builtins.input', lambda _: "['hello', 4, 5]")
    assert get_user_input_20() == None

    # Test should return None if the list is empty
    monkeypatch.setattr('builtins.input', lambda _: "[]")
    assert get_user_input_20() == None
