import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge7 import get_user_input_7, get_num_classfication

# test cases 
def test_get_num_classfication():
    #test should return true if the input is positive
    assert get_num_classfication(5) == "Positive"

    # Test should return false if the input is negative
    assert get_num_classfication(-5) == "Negative"

    # Test should return zero if the input is zero
    assert get_num_classfication(0) == "Zero"

    # Test should return None if the input is not a number
    assert get_num_classfication('hello') == "Invalid input"

def test_get_user_input_7(monkeypatch):
    # Test should return a positive number
    monkeypatch.setattr('builtins.input', lambda _: 5)
    assert get_user_input_7() == 5

    # Test should return a negative number
    monkeypatch.setattr('builtins.input', lambda _: -5)
    assert get_user_input_7() == -5

    # Test should return zero 
    monkeypatch.setattr('builtins.input', lambda _: 0)
    assert get_user_input_7() == 0

    # Test should return none for str
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert get_user_input_7() == None
