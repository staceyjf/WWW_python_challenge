# Day 7 : Write a program to check if a number is positive, negative, or zero.

def get_num_classfication(n):
    if not isinstance(n,int): #if its not a num
        return "Invalid input"
    elif n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:
        return "Negative"
     
#user input
def get_user_input_7():
    try:
        user_input = int(input("Please input a radius:"))
        if isinstance(user_input,int):
            return user_input
        else:
            return None
    except ValueError as e:
        print(e)
        return None