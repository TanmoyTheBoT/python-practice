from functools import reduce
# Map Example
l = [1, 2, 3, 4, 5]
sqr = lambda x: x**2

sqrList = map(sqr, l)
print(list(sqrList))

# Filter Example

def odd(n):
    if (n % 2 != 0):
        return True
    return False
onlyOdd = filter(odd, l)
print(list(onlyOdd))


# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))
