student = {
    "name" : "Suman",
    "class" : "12th",
    "marks" : {
        "phy" : 92,
        "chem" : 90,
        "math" : 83,
        "bio" : 95 
    }
}

# returns all keys
print(student.keys())

# we can typecast to list
print(list(student.keys()))

# to check the length of the dictionary
print(len(student))

# returns all values
print(student.values())

# returns all (key, value) pairs as typles
print(student.items())

# returns the key according to value
print(student.get("marks"))

# inserts the specified items to the dictionary
student.update({"city" : "kolkata"})
print(student)