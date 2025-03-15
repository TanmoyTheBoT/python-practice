# CHAPTER 3  – STRINGS

# 1 intro to string

name = "Tanmoy"

nameshort = name[0:3] # start form index 0  all the way till 3 till 3 (excluding 3)
print(nameshort)

character1 = name[1]
print(character1)

# 2 negative slicing with adv

name = "Tanmoy"

print(name[0:3])

print(name[-4:-1]) # convert to positive 
print(name[2:5])

print(name[:6]) # same as print(name[0:6])
print(name[0:]) # same as print(name[1:length of string])

print(name[1:6])
# anmoy

print(name[1:6:2])
# amy

word = "amazing"

print(word[:7]) # word[0:7]
print(word[0:]) # word[0:7]


# 3 string function

name = "tanmoy" 
print(len(name))
print(name.endswith("moy"))
print(name.startswith("Tan"))
print(name.capitalize())

# from chat gpt

s = " hello world "

print(s.upper())         # HELLO WORLD
print(s.lower())         # hello world
print(s.strip())         # "hello world"
print(s.replace("world", "Python"))  # " hello Python "
print(s.split())         # ['hello', 'world']
print(" | ".join(["a", "b", "c"]))  # "a | b | c"
print(s.startswith(" h"))  # True
print(s.endswith("d "))  # True
print(s.count("o"))      # 2
print(s.find("o"))       # 5
print(s[::-1])           # Reverse string
print(s.title())


# 3 Escape Securance

a = "Strow hat is a good boy\nbut not a bad \"boy\" "
print(a)


print("Newline character: \\n")
print("Tab character: \\t")
print("Backslash character: \\\\")
print("Single quote: \\'")
print("Double quote: \\\"")
print("Carriage return: \\r")
print("Backspace: \\b")
print("Form feed: \\f")
print("Octal value: \\ooo")
print("Hex value: \\xhh")


