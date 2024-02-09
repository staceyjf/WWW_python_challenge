# Day 30: Create a function that finds the second smallest element in a list.

def second_smallest_el(user_input):
    try:
        #split string into a list by ','
        user_list = user_input.split(",")
        # the list comprehenstion takes the chars in each element to see if they are a digit or a '.' to indicate a float
        user_list_num = list(map(lambda x: float(x), [x for x in user_list if all(char.isdigit() or char == '.' for char in x)])) 
        #convert to list from map object
        smallest = min(user_list_num)
        user_list_num.remove(smallest)
        second_smallest =  min(user_list_num)
        return second_smallest

    except ValueError: 
        print('You incorrectly entered your elements') #included strings or ended with ,
        return None
    except TypeError: #correct type but invalid value
        print('You have provided no arguments')
        return None

if __name__ == "__main__":
    user_input = input('Enter your list of els separated by ,:')
    print(second_smallest_el(user_input))