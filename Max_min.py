#The program finds the difference between the maximum and minimum values of an array
import random


def Max_Min():
    print('\nExercise 2 - Max - min')
    try:
        print('Enter the number of characters to be contained in the list = ')
        Size_list = int(input())
        print('Enter the minimum number to generate')
        min_value = int(input())
        print('Enter the maximum number to generate')
        max_value = int(input())
        List = []
    except Exception:
        print('You entered an invalid value')
        exit()



    for i in range(Size_list):
        List.append(random.uniform(min_value, max_value))

    List.sort()
    print(List)
    Result = List[-1]-List[0]
    print(round(Result, 3))