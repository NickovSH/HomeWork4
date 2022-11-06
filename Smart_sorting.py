#The program sorts the numbers originally in a tuple of them, sorting based on absolute values in ascending order.
# For example, the sequence (-20, -5, 10, 15) would be sorted as follows (-5, 10, 15, -20).
import random

def Absolute_Sort():
    print('\nExercise 3 - Smart sorting')

    try:
        print('Enter the number of characters to be contained in the tuple = ')
        Size_tuple = int(input())
        print('Enter the minimum number to generate')
        min_value = int(input())
        print('Enter the maximum number to generate')
        max_value = int(input())
    except Exception:
        print('You entered an invalid value')
        exit()

    Tuple = tuple(round(random.uniform(min_value, max_value), 3) for i in range(Size_tuple))
    print('Generated tuple ', Tuple)

    #Вызывается сортировка по анонимной функции лямбда, которая сравнивает модули
    Tuple = tuple(sorted(Tuple, key=lambda x:(abs(x), x)))
    print('Absolute tuple sort ', Tuple)