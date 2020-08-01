# -*- coding:utf-8 -*-

__author__ = "Atituset"


def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot: less.append(x)
        else: greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([9, 8, 4, 5, 32, 64, 2, 1, 0, 10, 19, 27]))
