# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The Square is {self.n**2}")

    def cube(self):
        print(f"The cube is {self.n**3}")

    def square_root(self):

        print(f"The square root is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.square_root()

