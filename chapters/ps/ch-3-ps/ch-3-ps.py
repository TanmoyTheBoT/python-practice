# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"


# ---------------------------------------------------------------------------

# 1 ans 

name = str(input(" Enter Your Name: "))

print(f"Good Afternoon!, {name} ")

# ---------------------------------------------------------------------------

# 2 Ans

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>" , "Tanmoy").replace("<|Date|>" , "8 March 2025"))

# ---------------------------------------------------------------------------

# 3 Ans

str = "Write a program to detect  double space in a string"

print(str.find("  "))

# ---------------------------------------------------------------------------

# 4 ans

str = "Write a program to detect  double space in a string"

print(str.replace("  " , " "))
print(str)  # string are immutable which means that you cnanot chnage them by runing functions on them

# ---------------------------------------------------------------------------

# 5 ans

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"

print(letter)