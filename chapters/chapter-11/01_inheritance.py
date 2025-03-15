# CHAPTER 11 - INHERITANCE & MORE ON OOPS

class Employee:
    company = "ITC"
    name = "Default Name"
    salary = 10
    
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Info tech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Info tech"
    language = "C"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


# a = Employee()
b = Programmer()
b.show()
b.showLanguage()
# print(a.company, b.company)