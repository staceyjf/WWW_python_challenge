import sys
sys.path.append('C:\\Users\\stace\\OneDrive\\Documents\\Code\\WWW_python_challenge')

from challenges.challenge28 import remove_nth_el

# test cases 
def test_remove_nth_el():
    #Test should return a list with the nth element removed for ints
    assert remove_nth_el("[1, 2, 3, 4, 5]", "1") == [2, 3, 4, 5]

 # Test should return a list with the nth element removed for strings
    assert remove_nth_el('["cat", "mat", "rat", "sat"]', '4') == ["cat", "mat", "rat"]

    # Test should return None if no nth element is found
    assert remove_nth_el('["hello", "there", "rat", "sat"]', '5') is None