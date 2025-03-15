# CHAPTER 9 – FILE I/O

# ---------------------------------------------------------------------------
##  01 file

'''
a = "a very long string with emails"

emails = []
3 seconds
'''
# f = open("file.txt", "r")
# data = f.read()
# print(data)
# f.close()

# ---------------------------------------------------------------------------
##  02 file_write

# s = "hello how are you iam file my name is tanmoy"

# f = open("file02.txt", "w")

# f.write(s)

# f.close

# ---------------------------------------------------------------------------
##  03 more file functions 

# f = open("file.txt", "r")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))

# line = f.readline()
# while(line != ""):
#     print(line ,end="")
#     line = f.readline()


# f.close()

# ---------------------------------------------------------------------------
##  04 append mode


# s = "hello how are you iam file my name is tanmoy\n"

# f = open("file02.txt", "a")

# f.write(s)

# f.close


# ---------------------------------------------------------------------------
## 05 with

# f = open("file.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:
with open("file.txt", "r") as f:
    print(f.read())

# You dont have to explicitly close the file

