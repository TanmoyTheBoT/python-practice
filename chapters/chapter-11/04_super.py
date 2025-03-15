class Employee:
    def __init__(self):
        super().__init__()
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
       super().__init__()
       print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

class Ceo(Manager):
     
     def __init__(self):
         super().__init__()
         print("Constructor of CEO")
     d = 4

class Owner(Ceo):
     def __init__(self):
         super().__init__()
         print("Constructor of Owner")
     e = 5




# o = Employee()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)


# o = Ceo()
# print(o.a, o.b, o.c, o.d)

o = Owner()
print(o.a, o.b, o.c, o.d, o.e)