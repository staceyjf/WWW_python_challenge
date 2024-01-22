# Day 10 : Write a program to remove duplicates from a list.

#does not preserve the order due to using set
# def remove_dups(input_list):
#     print(input_list)
#     result = set(input_list)
#     print(list(result))
#     return list(result)

def remove_dups(input_list):
    duplicate = set()
    result = []
    for item in input_list:
        if item not in duplicate:
            duplicate.add(item) #creating a reference point to match against
            result.append(item)
    return result

#user input
def get_user_input_10():
    user_input = input('Enter a list:')
    try:
        #checking to see if it is a string representation of a list
        if isinstance(eval(user_input), list):
            return eval(user_input)
        else:
            print('Invalid entry. Please input a list')
            return None
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    input_list = get_user_input_10()
    print(remove_dups(input_list))