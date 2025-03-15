class Employee:
    language = "Python" # This a class attribute
    salary = 100000

    def __init__(self, name, language, salary): ## init dunder method which is automatically called when creating new object
         self.name = name
         self.language = language
         self.salary = salary
         print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")

    def greet1(self):
        print(f"Good Morning {self.name}")

    @staticmethod  # Decorator 
    def greet2():
        print(f"Good Night go to bed")

tanmoy = Employee("Tanmoy", "C" , 100)
# tanmoy.name = "Tanmoy" # This an instance/object attribute
# tanmoy.language = "C"
print(tanmoy.name, tanmoy.language, tanmoy.salary)

tanmoy.greet1()
tanmoy.getInfo()
tanmoy.greet2()
# Employee.getInfo(tanmoy)


# shuvo = Employee() # object