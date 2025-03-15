class Employee:
    language = "Python" # This a class attribute
    salary = 100000

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")

    def greet1(self):
        print(f"Good Morning {self.name}")

    @staticmethod  # Decorator 
    def greet2():
        print(f"Good Night go to bed")

tanmoy = Employee()
tanmoy.name = "Tanmoy" # This an instance/object attribute
# tanmoy.language = "C"
# print(tanmoy.name, tanmoy.language, tanmoy.salary)

tanmoy.greet1()
tanmoy.getInfo()
tanmoy.greet2()
# Employee.getInfo(tanmoy)