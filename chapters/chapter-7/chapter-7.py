# CHAPTER 7 – LOOPS IN PYTHON

## 01 loop

print(1)
print(2)
print(3)
print(4)
print(5)

# the same task can be done like 

for i in range(1, 6):
    print(i)


## 02 while loops

i = 1

while(i<51):
    print(i)
    i +=1

# """
# output:
# 1
# 2
# 3
# 4
# 5
# """

i = 0
while i < 5: # print "Harry" – 5 times!
  print("Harry")
  i = i + 1


## 03 list using while loop


l = [1 , "Tanmoy", 2025, "hello", "luffy", "Robin" , "Zoro", "No.4"]

i = 0
while(i<len(l)):
    print(l[i])
    i +=1


## 04 for loops

for i in range(0, 7, 2):
    print(i)


# ## 05 for loops iterate

## for loop in list 
l = [1, 2, 5, 90, 90]
for i in l:
    print(i)

## for loop in tuples

t = {1, 2, 5, 90, 90 , 3999, "hello"}
for i in t:
    print(i)

## for loop in strings
s = "Tanmoy"
for i in s:
    print(i)

## 06 for loops with else whne for loop exhosted thne go to else 
l = [99, 2, 5, 69, 90]
for item in l:
    print(item)
else:
    print("Done")


## 07 break and continued and pass

for i in range (100):
    if(i == 51):
        break # exit the loop right now 
    print(i)

for i in range (30):
    if(i == 15):
        continue # skip this iteration
    print(i)

## 07 pass

for i in range (10):
    pass


i = 0
while(i<10):
    print(i)
    i +=1










