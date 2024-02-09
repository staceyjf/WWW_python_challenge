import sys
import pytest
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge30 import second_smallest_el


# test cases 
def test_second_smallest_el():
   #Test should return the second smallest element in a list of int
   assert second_smallest_el("1,2,3,4") == 2

   #Test should return the second smallest element in a list of floats
   assert second_smallest_el("1.1,1.2,1.3,1.4") == 1.2

   #Test should return None is input is blank
   assert second_smallest_el("") is None

   #Test should return None if list does not contain int or floats
   assert second_smallest_el('"hello", "there", "rat", "sat"') is None

    
