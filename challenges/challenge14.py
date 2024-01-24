# Day 14 : Write a program to print the first n numbers of a Fibonacci sequence.

#Fibonacci sequence
#0, 1, 1, 2, 3, 5, 8, 13,

#Fibonacci number
#0, 1, 2, 3, 4, 5, 6, 7

#user input
def get_user_input_14():
    try:
        user_input = int(input('Enter your Fibonacci number:'))
        return user_input
    except ValueError:
        return None

def print_Fibonacci(n):
    result = []
    # count = 0

    if n is None or isinstance(n, str) or n < 0:
        return None
   
    # while count <= n:
    #     if count == 0:
    #         result.append(0)
    #     elif count == 1:
    #         result.append(1)
    #     else:
    #         next_num = result[count - 1] + result[count - 2]
    #         result.append(next_num)  # Update result with the new Fibonacci number

    #     count += 1

    # print(result)
    # return result

    for i in range(n + 1):
        if i == 0:
              result.append(0)
        elif i == 1:
            result.append(1)
        else:
            next_num = result[i - 1] + result[i - 2]
            result.append(next_num)  # Update result with the new Fibonacci number

    print(result)
    return result
    
if __name__ == "__main__":
    user_input = get_user_input_14()
    print(print_Fibonacci(user_input))