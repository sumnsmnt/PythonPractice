# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Suman", "Sachin", "Rahul"]

l = ["Harry", "Suman", "Sachin", "Rahul"]

for name in l:
    if (name.startswith("S")):
        print("Hello, ", name)
    