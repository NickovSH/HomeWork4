#The median is a numeric value that divides a sorted array of numbers into major and minor halves. In a sorted
#array with an odd number of elements, the median is the number in the middle of the array. For an array with an even
# number of elements where there is not one element exactly in the middle, the median is the average of the two numbers
# in the middle of the array. In this problem, you are given a non-empty array of natural numbers. You need to find the
# median of the given array.
import random

def Median():
    print('\nExercise 4 - Median')

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
        List.append(random.randrange(min_value, max_value))

    List.sort()

    if Size_list % 2 == 0:
        Median = (List[int(Size_list/2-1)]+List[int(Size_list/2)])/2
        print('1')
    else:
        Median = List[round(Size_list/2)]
        print('2')

    print('List = ', List)
    print('Median = ', Median)