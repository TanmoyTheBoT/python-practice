# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("poems.txt", "r")

content = f.read()
if("twinkle" in content):
    print("The Word twinkle is present in the content")

else:
    print("The Word twinkle is not present in the content")


f.close