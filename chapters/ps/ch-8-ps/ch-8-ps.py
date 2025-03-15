# CHAPTER 8 – PRACTICE SET
# 1. Write a program using functions to find greatest of three numbers.
# 2. Write a python program using function to convert Celsius to Fahrenheit.
# 3. How do you prevent a python print() function to print a new line at the end.
# 4. Write a recursive function to calculate the sum of first n natural numbers.
# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
# 6. Write a python function which converts inches to cms.
# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.
# 8. Write a python function to print multiplication table of a given number.

# ---------------------------------------------------------------------------
##  01 ans

# def greatest(a , b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a = 2
# b = 9
# c = 3
# print(greatest(a, b, c))


# ---------------------------------------------------------------------------
##  02 ans

# def f_to_c(f):
#     return 5 * ((f - 32) / 9)


# f = int(input("Enter Temperature in F: "))
# c = f_to_c(f)
# print(f"{round(c, 2)} °C")


# ---------------------------------------------------------------------------
##  03 ans

# print("a")
# print("b")
# print("c", end="")
# print("d", end="")


# ---------------------------------------------------------------------------
##  04 ans

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(5))


# ---------------------------------------------------------------------------
##  05 ans

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)

# ---------------------------------------------------------------------------
##  06 ans

# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter value in inches: "))

# print(f"The Conversion valuse in Centimeter is: {inch_to_cms(n)} ")


# ---------------------------------------------------------------------------
##  07 ans

# def rem(l , word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
#     # for item in l:
#     #     l.remove(word)
#     #     return l

# l = ["Tanmoy", "banana", "cherry ", "apple" , "an"]

# print(rem(l, "an"))


# ---------------------------------------------------------------------------
##  08 ans

def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(5)




