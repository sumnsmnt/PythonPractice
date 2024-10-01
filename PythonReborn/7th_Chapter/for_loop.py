# For loop starts from 0 by default
for i in range(3):
    print(i)

# We can use for loop in lists
list = ["Suman", "Python", 12, 10, 1998, "Linux"]
for i in list:
    print(i)

# Also use in case of tuple
tup = (45, 78, "Python", "tuple")
for i in tup:
    print(i)

# For loop can be used in case of string
s = "SUMAN"
for i in s:
    print(i)

# For loop with else
l = [3, 4, 5]

for number in l:
    print(number)
else:
    print("done")