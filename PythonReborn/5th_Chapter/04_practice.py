# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name:lang})
name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name:lang})
name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name:lang})
name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name:lang})

print(d)

# If the names of 2 friends are same; what will happen to the program?

# If languages of two friends are same; what will happen to the program?
