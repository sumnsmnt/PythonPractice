# Check that a tuple type cannot be changed in python.

tup = ("Suman", 67, 78.9, "linux")

tup[0] = "Python"

print(tup)

# So here it will give an error, cause tuple is immutable.