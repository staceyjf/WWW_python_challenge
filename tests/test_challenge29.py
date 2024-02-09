import sys
import pytest
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge29 import random_num_generator


# test cases 
def test_random_num_generator(monkeypatch):
   #Test should return a random number from a range of positive numbers
   result = random_num_generator("0", "5") 
   assert 0 <= result <= 5  # Ensure the result is within the specified range

   #Test should return a random number from a range of negative numbers
   result = random_num_generator("-4", "0") 
   assert -4 <= result <= 0  # Ensure the result is within the specified range

   #Test should return a random number even when the order of inputs has the highest first
   result = random_num_generator("8", "0") 
   assert 0 <= result <= 8  # Ensure the result is within the specified range

   #Test should return None if only one input is given
   monkeypatch.setattr('builtins.input', lambda _: "1") # Mock user input to define range
   #check that the function raises a TypeError (calling a function with the wrong number or type of arguments)
   with pytest.raises(TypeError): 
    random_num_generator() 
