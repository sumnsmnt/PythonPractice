# Write a program which finds out whether a given name is present in a list or not.

l1 = ["Suman", "Sujan", "Sajan", "Subham", "Sagar"]

name = input("Find the name: ")

if (name in l1):
    print("Name is present in the list")
else:
    print("Name is not present in the list")