# Variable
print("1. Variable")

a = 1 
b = 2
c = 8

name = "Tanmoy"
print(name)
print(a+b)


# Datatype
print("2. Datatype")


x = 1 # x  is an  integer variable
y = 2.222 # y is a floting point number variable
z = "Tanmoy" # Z is a  string variable
d = False # d is a boolean type variable
e = None # e is none type variable

'''
RULES FOR  CHOOSING AN  IDENTIFIER  
• A variable name can contain alphabets, digits, and underscores. 
• A variable name can only start with an alphabet and underscores. 
• A variable name can’t start with a digit. 
• No while space is allowed to be used inside a variable name. 
'''
print("3. Rule Variable")

_tanmoy = "Tanmoy"
# @_tanmoy = "With @ " is invalid

print(_tanmoy)

"""OPERATORS IN PYTHON  
Following are some common operators in python: 
1. Arithmetic operators: +, -, *, / etc. 
2. Assignment operators:  =, +=, -= etc. 
3. Comparison operators: ==, >, >=, <,  != etc. 
4. Logical operators: and, or, not."""

print("4. Operators")

# Arithmetic operators:

aa = 7
bb = 2
cc = aa + bb

print(cc)


# Assignment operators

aaa = 8-1 # assign 8-1 in aaa
print(aaa)
bbb = 6
bbb += 3 # Incremnt the value of bbb  by 3 and then assign it to bbb
bbb -= 3 # Decremnt the value of bbb  by 3 and then assign it to bbb

print(bbb)


# Comparison operators

ccc = 5<=5
ddd = 10!=10
eee = 5==5


print(ccc)
print(ddd)
print(eee)


# Logical operators

print("True table of 'or' operator:")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:",False or True)
print("False or False:",False or False)

print("True table of 'and' operator:")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:",False and True)
print("False and False:",False and False)

print("True table of 'not' operator:")
print("not True:", not True)
print("not False:", not False)

# TYPE() FUNCTION  AND  TYPECASTIN G.

print("5. Typecasting")

aaaaa = 31  
t=type(aaaaa) # class <int>
print(t)

bbbbb = 31.2  
t=type(bbbbb) # <class 'float'>
print(t)

ccccc = "Tanmoy"  
t=type(ccccc) # <class 'str'>
print(t)

ddddd = "21.1" # <class 'str'>
eeeee = float(ddddd) # type to be float / str to float
t=type(eeeee) # <class 'float'>
print(t)


print("6. Input")

# Input

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("Number a is: ",  a)
print("Number b is: ",  b)

print("Sum is ", a + b)







