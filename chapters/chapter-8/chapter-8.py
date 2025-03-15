# CHAPTER 8 – FUNCTIONS & RECURSIONS

# ---------------------------------------------------------------------------

## 01 functions

# a = int(input("Enter A Number: "))
# b = int(input("Enter A Number: "))
# c = int(input("Enter A Number: "))

# average = ((a + b + c)/3)
# print(average)


# a = int(input("Enter A Number: "))
# b = int(input("Enter A Number: "))
# c = int(input("Enter A Number: "))

# average = ((a + b + c)/3)
# print(average)

## Function Defination

# def avg():
#     a = int(input("Enter A Number: "))
#     b = int(input("Enter A Number: "))
#     c = int(input("Enter A Number: "))
#     average = ((a + b + c)/3)
#     print(average)



# avg() # Function Call
# print(f"Your Numbers Avarage function done thanks you")
# avg()
# avg()
# avg()

# ---------------------------------------------------------------------------

# Quick Quiz: Write a program to greet a user with “Good day” using functions.

# def goodDay():
#     print("Good Day")

# goodDay()


# ---------------------------------------------------------------------------

## 03 function with argument

# def goodDay(name, ending):
#     print("Good Day " + name)
#     print(ending)
#     return "Done"


# goodDay("Tanmoy", "Thank you")
# goodDay("Rayhan", "Thank you")
# a = goodDay("Sani", "Tnx")
# print(a)

# ---------------------------------------------------------------------------
## 04 Default argument


# def goodDay(name, ending="Thank You"):
#     print(f"Good Day {name}")
#     print(ending)


# goodDay("Tanmoy", "Tnx")
# goodDay("Oanmoy")

# ---------------------------------------------------------------------------
## 05 RECURSION

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1

    return n * factorial(n-1)

n = int(input("Enter A Number: "))
print(f"Factorial of this is number is: {factorial(n)}")




