class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

class Ceo(Manager):
    d = 4

class Owner(Ceo):
    e = 5




o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)


o = Ceo()
print(o.a, o.b, o.c, o.d)

o = Owner()
print(o.a, o.b, o.c, o.d, o.e)