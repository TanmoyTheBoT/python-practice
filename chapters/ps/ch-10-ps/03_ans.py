# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Test:
    a = 4


o = Test()
print(o.a) # it printing class attribute because instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) ## it printing instance attribute because instance attribute is present

print(Test.a) # print class attribute 

# ans class attributes not change


