# CHAPTER 5  – PRACTICE SET  
# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 
# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# 5. s = {} 
# What is the type of 's'? 
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
# 7. If the names of 2 friends are same; what will happen to the program in problem 
# 6? 
# 8. If languages of two friends are same; what will happen to the program in problem 
# 6? 
# 9. Can you change the values inside a list which is contained in set S?  
# s = {8, 7, 12, "Harry", [1,2]} 

# ---------------------------------------------------------------------------

## ans 1

# words = {
#     "alu": "potato",
#     "billi": "cat", 
#     "kutta": "dog" 

# }

# word = input("Enter the word you want English meaning: ")

# print(words[word])

# ---------------------------------------------------------------------------


## ans 2
# s = set()

# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# print(s)

# ---------------------------------------------------------------------------

## ans 3


# s = set()
# s.add(18)
# s.add("18")
# print(s)

# ---------------------------------------------------------------------------

## ans 4

# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# print(len(s))

# ---------------------------------------------------------------------------

## ans 5

# s = {} 
# print(type(s)) # <class 'dict'>


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

## ans 6 & 7 the vlaue  enterd later witll be updated & 8 Nothing Will happande Can be same valuse

# d = {}

# name = input("Enter Friends Name: ")
# lang = input("Enter Language Name: ")
# d.update({name: lang})

# name = input("Enter Friends Name: ")
# lang = input("Enter Language Name: ")
# d.update({name: lang})

# name = input("Enter Friends Name: ")
# lang = input("Enter Language Name: ")
# d.update({name: lang})

# name = input("Enter Friends Name: ")
# lang = input("Enter Language Name: ")
# d.update({name: lang})

# print(d)

# ---------------------------------------------------------------------------

## ans 9

# s = {8, 7, 12, "Harry", [1,2]}
# s[4][0] = 9
# # TypeError: unhashable type: 'list'



 
 
  
