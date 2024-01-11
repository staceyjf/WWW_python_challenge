# Day 1 : Create a program that swaps the values of two variables.

# This script takes two variable values as input
# and displays the input values for those variables.

def swap_variables(a,b):
    return b,a

a = input('Input your first variable:')
b = input('Input your second variable:')

result = swap_variables(a,b)

print('this is the result of swap_variables', result)

#test 
def test_swap_variables():
    # Test for numbers
    assert swap_variables(1, 2) == (2, 1)
    # Test for strings
    assert swap_variables("hello", "world") == ("world", "hello")
