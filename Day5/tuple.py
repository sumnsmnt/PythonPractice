'''

# Tuple is a built in data type in Python and it's immutable.
# So we can't change any values within tuple.

tup = (1, 4, 2, 5, 3)
print(type(tup))
print(tup[3])

# we can create an empty tuple
tup = ()
print(tup)
print(type(tup))
# if only 1 element is there, then we have to add comma to make it tuple
# otherwise it will be different data types
tup = (1)
print(type(tup))

tup = (1.0)
print(type(tup))

tup = ("Suman")
print(type(tup))

tup = (5,)
print(type(tup))

# Tuple Slicing
tup = (1, 2, 4, 6)
print(tup[1:3])

'''

# Tuple Methods
tup = (2, 4, 2, 1, 4, 1, 3, 5)

# returns index of first occurrence
print(tup.index(1))

# counts total occurence
print(tup.count(4))