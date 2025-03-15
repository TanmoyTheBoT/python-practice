# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:
    salary = 100
    increment = 10
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment =  ((salary/self.salary) -1)*100 
    

a = Employee()

print(a.salaryAfterIncrement)
print(a.increment)
a.salaryAfterIncrement = 110

print(round(a.increment, 2))

    


