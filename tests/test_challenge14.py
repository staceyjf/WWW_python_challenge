import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge14 import get_user_input_14, print_Fibonacci

def test_print_Fibonacci(capsys):
    # Test print out should match the expected output
    print_Fibonacci(6)
    captured = capsys.readouterr()
    expected_output = '[0, 1, 1, 2, 3, 5, 8]\n'     # Setting up an example output to match against
    assert captured.out == expected_output # Compare the captured output with the expected output

    # Test should return None if a negative number is given
    print_Fibonacci(-5)
    captured_with_string = capsys.readouterr()
    assert captured_with_string.out == "" 
    
    # Test should return zero if zero is inputted
    print_Fibonacci(0)
    captured_with_string = capsys.readouterr()
    assert captured_with_string.out == '[0]\n' 
    
    # Test should return one if 1 is inputted
    print_Fibonacci(1)
    captured_with_string = capsys.readouterr()
    assert captured_with_string.out == '[0, 1]\n' 
    
    # Test should return one if 2 is inputted
    print_Fibonacci(2)
    captured_with_string = capsys.readouterr()
    assert captured_with_string.out == '[0, 1, 1]\n'   

    # Test should return None if a string is inputted
    print_Fibonacci('hello')
    captured_with_string = capsys.readouterr()
    assert captured_with_string.out == ""  

def test_get_user_input_14(monkeypatch):
    # Test should return a positive number
    monkeypatch.setattr('builtins.input', lambda _: 2)
    assert get_user_input_14() == 2

    # Test should return a negative number
    monkeypatch.setattr('builtins.input', lambda _: -5)
    assert get_user_input_14() == -5

    # Test should return zero 
    monkeypatch.setattr('builtins.input', lambda _: 0)
    assert get_user_input_14() == 0

    # Test should return none for str
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert get_user_input_14() == None