#The program finds the sums of even elements of the list,
#sums them up and multiplies the sum by the last element of the list
import random


def Sum_Even():
    print('\nExercise 1 - Last with even')

    print('Enter the number of characters to be contained in the list = ')
    Size_list = int(input())
    List = []
    k = 0

    for i in range(Size_list):
        List.append(random.randrange(50))
        if i % 2 == 0:
            k = k + List[i]

    Result = k * List[-1]

    print('List = ', List)
    print('Result = ', Result)