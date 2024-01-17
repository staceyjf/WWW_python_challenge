import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge5 import get_user_input_5, get_min_max_values

def test_get_min_max_values():
    #test with two nums to see min and max
    assert get_min_max_values([1,2]) == [1,2]

    #test with more than two nums to see min and max
    assert get_min_max_values([1,2,3,4,5]) == [1,5]

    #test for only one number
    assert get_min_max_values([1]) == [1,1]

    #test for no numbers
    assert get_min_max_values(["hello","there","world"]) == None

    #test for mixed datatypes
    assert get_min_max_values(["hello",2,3]) == [2,3]

def test_get_user_input_5(monkeypatch):
    # Test input function with two nums
    monkeypatch.setattr('builtins.input', lambda _: [1,2])
    assert get_user_input_5() == [1,2]

    #test input function with more than two nums 
    monkeypatch.setattr('builtins.input', lambda _: [1,2,3,4,5])
    assert get_user_input_5() == [1,2,3,4,5]

    # Test which includes str and numbers
    monkeypatch.setattr('builtins.input', lambda _: ["hello",2,3])
    assert get_user_input_5() == ["hello",2,3]

    # Test input function with non-list type
    monkeypatch.setattr('builtins.input', lambda _: '123')
    assert get_user_input_5() is None

    # Test input function with no input (empty line is returned which is represented by \n)
    monkeypatch.setattr('builtins.input', lambda _: '\n')
    assert get_user_input_5() == None