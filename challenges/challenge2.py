# Day 2 : Create a program to calculate the area of a circle given its radius.

# This script takes a radius and calculates the area of a circle (A = pi r2)

#import math library
import math

def area_Circle(r):
    if r is None:
        return 'No input provided'
    
    try:
        r = float(r)
    except ValueError:
        return 'Invalid input. Please enter a numeric value.'
    
    # round function with a second param of the decimal place
    return round(math.pi * (r**2), 2)

#user input
def get_user_input():
    try:
        return int(input("Please input a radius:"))
    except ValueError:
        print('Please insert a numeric value')
        return None

if __name__ == "__main__":
    user_radius = get_user_input()
    result = area_Circle(user_radius)
    print(f'The area of a circle with {user_radius} is {result}')