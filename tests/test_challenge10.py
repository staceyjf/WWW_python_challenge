import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge10 import get_user_input_10, remove_dups

def test_remove_dups():
    #Test should return a list containing numbers without duplicates 
    assert remove_dups([1,1]) == [1]

    #Test should return a list containing strings without duplicates 
    assert remove_dups(["hello", "hello", "there"]) == ["hello", "there"]

    #Test should return a mixed datatype list with duplication
    assert remove_dups(["cat",2,2,2,2]) == ["cat",2]

    #Test should return empty if the supplied list is empty
    assert remove_dups([]) == []


def test_get_user_input_10(monkeypatch):
    # Test should return numbers in a list
    monkeypatch.setattr('builtins.input', lambda _: '[1, 1]')
    assert get_user_input_10() == [1, 1]

    # Test should return mixed datatype list
    monkeypatch.setattr('builtins.input', lambda _: '["cat", 2, 2, 2, 2]')
    assert get_user_input_10() == ["cat", 2, 2, 2, 2]

    # Test should return None if the input is not a list (string)
    monkeypatch.setattr('builtins.input', lambda _: "I'm not a list")
    assert get_user_input_10() == None

    # Test should return None if the input is not a list (int)
    monkeypatch.setattr('builtins.input', lambda _: '123')
    assert get_user_input_10() == None

    # Test input function with no input (empty line is returned which is represented by \n)
    monkeypatch.setattr('builtins.input', lambda _: '\n')
    assert get_user_input_10() == None