# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.

class Vector:
    def __init__(self, l):
        self.l = l  # List representing the vector components

    def __len__(self):
        return len(self.l)  # Returns the number of components in the vector

# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))  # Output: 3
