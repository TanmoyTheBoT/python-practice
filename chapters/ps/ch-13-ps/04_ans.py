# 4. Write a program to filter a list of numbers which are divisible by 5.
l = [1, 5, 10, 22, 90, 3, 9]

def filter5(n):
    if (n%5 ==0):
        return True
    return False
f = list(filter(filter5, l))
print(f)


