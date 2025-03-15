# CHAPTER 10 - OBJECT ORIENTED PROGRAMMING


class Employee:
    language = "Python" # This a class attribute
    salary = 100000



tanmoy = Employee()
tanmoy.name = "Tanmoy" # This an instance/object attribute
print(tanmoy.name, tanmoy.language, tanmoy.salary)

shuvo = Employee()
shuvo.name = "Shuvo D."
print(shuvo.name, shuvo.language, shuvo.salary)

# here name is /object attribute and salary and language are class attribute as they directly belong to the class 
 