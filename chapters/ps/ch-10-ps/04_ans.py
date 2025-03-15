# 4. Add a static method in problem 2, to greet the user with hello.


class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The Square is {self.n**2}")

    def cube(self):
        print(f"The cube is {self.n**3}")

    def square_root(self):

        print(f"The square root is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello! Thanks for Using this")

    

a = Calculator(4)
a.square()
a.cube()
a.square_root()
a.hello()

