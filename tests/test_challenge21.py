import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge21 import get_user_input_21, remove_el_from_list

# test cases 
def test_remove_el_from_list():
    #Test should remove an element from a set of ints
    assert remove_el_from_list(({1, 2, 3, 4, 5}, 5)) == {1, 2, 3, 4}

    #Test should remove an element from a set of strings
    assert remove_el_from_list(({"cat", "mat", "rat", "sat"}, "sat")) == {"cat", "mat", "rat"}

def test_get_user_input_21(monkeypatch):
    # Test should return a tuple with a set of strings and a string
    inputs = iter(["hello, tiny, people", "hello"])
    # Monkeypatch input function to return values from the list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Test should return a tuple with a set and a str
    assert get_user_input_21() == ({"hello", "tiny", "people"}, "hello")

    # Test should return a tuple with a set of ints and an int 
    inputs = iter(["12,4,5", "4"])
    # Monkeypatch input function to return values from the list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Test should return a tuple with a set and an int
    assert get_user_input_21() == ({12,4,5}, 4)

    # Test should remove duplicates and return a tuple and element
    inputs = iter(["12,4,4,5", "4"])
    # Monkeypatch input function to return values from the list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Test should remove the duplicate and return a tuple with a set and an int 
    assert get_user_input_21() == ({12,4,5}, 4)

    # Test input function with no input
    inputs = iter([])
    monkeypatch.setattr('builtins.input', lambda _: [])
    assert get_user_input_21() is None
