# CHAPTER 5 – DICTIONARY & SETS

## 1 dict

# d = {} # empty dictionary
# print(type(d))

# marks = {
#    "Tanmoy": 100,
#    "Rayhan": 90,
#    "Sani": 45 
# }

# print(marks , type(marks))

# print(marks["Tanmoy"])

## 2 dict methhods

# marks = {
#    "Tanmoy": 100,
#    "Rayhan": 90,
#    "Sani": 45 
# }

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Tanmoy": 99, "Harry": 99})
# print(marks)
# print(len(marks))


# print(marks.get("Tanmoy2")) # print None
# print(marks["Tanmoy2"]) # retuns an eroers


## 03 sets 

# s = {1 , 3, 5 , 10, 15, 5 , 2 , 7, 9 , 100 , 90}

# e = set() # empty set
# print(type(e)) 

# print(s)

## 04 sets methods  

# s = {1 , 3, 5 , 10, 15, 5 , 2 , 7, 9 , 100 , 90 , "Tanmoy"}

# print(s ,type(s))
# print(len(s))
# s.remove(1)
# print(s ,type(s))

## 05  sets union intersection

s1 =  {1, 45, 4, 7 , 9 , 10}
s2 =  {10, 2, 6, 7 , 5 , 77}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1 - s2)

# Additional set methods
print(s1.difference(s2))  # same as s1 - s2
print(s2.difference(s1))  # elements in s2 but not in s1
print(s1.symmetric_difference(s2))  # elements in either s1 or s2 but not in both
print(s1.issubset(s2))  # check if s1 is a subset of s2
print(s1.issuperset(s2))  # check if s1 is a superset of s2
print(s1.isdisjoint(s2))  # check if s1 and s2 have no elements in common
