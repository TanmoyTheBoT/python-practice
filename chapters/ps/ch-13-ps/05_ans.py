# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
from functools import reduce
l = [1, 5, 10, 22, 90, 3, 9, 99, 100, 4789]

def maximum(a,b):
    if (a>b):
        return a
    return b
print(reduce(maximum, l))




