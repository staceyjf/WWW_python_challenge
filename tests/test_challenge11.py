import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge11 import get_user_input_11, print_times_table

def test_print_times_table(capsys):
    # Test should return a console log of the inputted number
    print_times_table(12)
    captured = capsys.readouterr()

    # Setting up an example output to match against with correct indentation
    expected_output = '1 x 12 = 12\n2 x 12 = 24\n3 x 12 = 36\n4 x 12 = 48\n5 x 12 = 60\n6 x 12 = 72\n7 x 12 = 84\n8 x 12 = 96\n9 x 12 = 108\n10 x 12 = 120\n11 x 12 = 132\n12 x 12 = 144\n'

    # Compare the captured output with the expected output
    assert captured.out == expected_output

    #Test should return None if a negative number is used
    assert print_times_table(-5) == None

    #Test should return None if a string is inputed
    assert print_times_table(('hello')) == None

    #Test should return None if zero is inputted
    assert print_times_table(0) == None

def test_get_user_input_11(monkeypatch):
    # Test should return a positive number
    monkeypatch.setattr('builtins.input', lambda _: 2)
    assert get_user_input_11() == 2

    # Test should return a negative number
    monkeypatch.setattr('builtins.input', lambda _: -5)
    assert get_user_input_11() == -5

    # Test should return zero 
    monkeypatch.setattr('builtins.input', lambda _: 0)
    assert get_user_input_11() == 0

    # Test should return none for str
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert get_user_input_11() == None