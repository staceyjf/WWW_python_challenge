import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge15 import get_user_input_15, leap_year

def test_leap_year():
    # Test should return 'Leap Year' if the input is dividable by 4 and 400 but not by 100
    assert leap_year(2000) == 'Leap Year'

    # Test should return 'Not a Leap Year' if the input date is not a leap year
    assert leap_year(2003) == 'Not a Leap Year'

    # Test should return 'Not a Leap Year' if it is dividable by 100  
    assert leap_year(1800) == 'Not a Leap Year'

    # Test should return 'None' if a string is entered
    assert leap_year('hello') == None

    # Test should return 'None' if a year is not is entered
    assert leap_year(198) == None

def test_get_user_input_15(monkeypatch):
    # Test should return a positive number - moved to strings as these are default data types for inputs
    monkeypatch.setattr('builtins.input', lambda _: '1983')
    assert get_user_input_15() == 1983

    # Test should return none for str
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert get_user_input_15() == None

    # Test should return None for a number shorter than 4
    monkeypatch.setattr('builtins.input', lambda _: '201')
    assert get_user_input_15() == None

    # Test should return None for Zero
    monkeypatch.setattr('builtins.input', lambda _: '0')
    assert get_user_input_15() == None