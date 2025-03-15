# 1. Write a python program to add two numbers. 
# 2. Write a python program to find remainder when a number is divided by z. 
# 3. Check the type of variable assigned using input () function. 
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than 
# ‘b’ or not. Take a = 34 and b = 80 
# 5. Write a python program to find an average of two numbers entered by the user. 
# 6. Write a python program to calculate the square of a number entered by the user.

# ---------------------------------------------------------------------------

# 1 Answer

a = 7
b = 2 
print(a + b)

# ---------------------------------------------------------------------------

# 2 Answer

a = 14
b = 5 

print("Remainder When is Devided by B is", a % b) # bhag ses

# ---------------------------------------------------------------------------

# 3 Answer

a = input("Enter A Value of a: ")
print(type(a))

# ---------------------------------------------------------------------------

# 4 Answer

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("Is A greater than B?", a > b)

# ---------------------------------------------------------------------------

# 5 Answer

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("The average of these two number is", (a+b)/2)

# ---------------------------------------------------------------------------
# 6 Answer

a = int(input("Enter Your Number: "))
print("The Squre of the number is", a*a)
print("The Squre of the number is", a**2)


