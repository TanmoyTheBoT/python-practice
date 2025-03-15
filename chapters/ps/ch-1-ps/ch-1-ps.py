# CHAPTER 1 – PRACTICE SET
# 1. Write a program to print Twinkle twinkle little star poem in python.
# 2. Use REPL and print the table of 5 using it.
# 3. Install an external module and use it to perform an operation of your interest.
# 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
# 5. Label the program written in problem 4 with comments. 

# ---------------------------------------------------------------------------

print("Answer 1")
print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
""")

# ---------------------------------------------------------------------------

print("Answer 2")
print(r"""
PS C:\Users\TanmoyTheBoT\repo\python-practice> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5*1
5
>>> 5*2
10
>>> 5*3
15
>>> 5*4
20
>>> 5*5
25
>>> 5*6
30
>>> 5*7
35
>>> 5*8
40
>>> 5*9
45
>>> 5*10
50
""")

# ---------------------------------------------------------------------------

# pip install pyttsx3
print("Answer 3")

import pyttsx3
engine = pyttsx3.init()
engine.say("this is 3rd question answer")
engine.runAndWait()

# ---------------------------------------------------------------------------

print("Answer 4")
import os

# Select the dirctory thats content that you want to list
directory_path = '/'

# use os module to list directory contents
contents = os.listdir(directory_path)

# Print the content
print(contents)
print('Answer 5 comments in 4 ')

