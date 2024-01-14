import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge4 import get_user_input_4, sum_of_list

def test_sum_of_list():
    #test to sum elements one element
    assert sum_of_list([1]) == 1

    #test to sum elements more than one element
    assert sum_of_list([1,2,3]) == 6

    #test for no numbers
    assert sum_of_list(["1","2","3"]) == 0

    #test for mix
    assert sum_of_list(["hello",2,3]) == 5

def test_get_user_input_4(monkeypatch):
    # Test input function with one element
    monkeypatch.setattr('builtins.input', lambda _: [1])
    assert get_user_input_4() == [1]

    #test input function with more than one element
    monkeypatch.setattr('builtins.input', lambda _: [1,2,3])
    assert get_user_input_4() == [1,2,3]

    # Test input function with non-list type
    # Set input to return a numeric value
    monkeypatch.setattr('builtins.input', lambda _: '123')
    assert get_user_input_4() is None

    # Test input function with no input (empty line is returned which is represented by \n)
    monkeypatch.setattr('builtins.input', lambda _: '\n')
    assert get_user_input_4() == None