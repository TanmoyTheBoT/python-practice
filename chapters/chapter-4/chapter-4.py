# CHAPTER 4 – LISTS AND TUPLES


## 01 List 

friends = ["Apple" , "Orange", "Rayhan" , "Saim" , 5 , 4.75 , True ]

print(friends[2])
friends[2] = "Sani" # Unlike Strings list are mutable
print(friends[2])

print(friends[2:4])

## 02. list methods

friends.append("Harry") #
print(friends)


l1 = [1, 32, 10, 90, 3, 200, 5, 2, 9, 1, 5, 6]
# l1.sort()
# l1.reverse()
# l1.insert(3 ,20) # insert 20 in list lindex 3
value = l1.pop(3)
print(value)
l1.remove(200)
print(l1.count(5))  
print(l1)


## 03 Tuples

a = (1,1, 32, 10, 90, 3, 200, 5, 2, 9, 1, 5, 6, "Apple" , "Orange", "Rayhan" , "Saim" , 5 , 4.75 , True) 

print(type(a))
print(a)


## 04 Tuples methods


a = (1,1, 32, 10, 90, 3, 200, 5, 2, 9, 1, 5, 6, "Apple" , "Orange", "Rayhan" , "Saim" , 5 , 4.75 , True) 

print(a)
no = a.count(1)
print(no)

i = a.index(5)
print(i)

print(len(a))
