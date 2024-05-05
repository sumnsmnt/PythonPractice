'''

# Set is mutable but the elements are immutable

collection = set()

# adds an element
# we can not store list and dictionary as they are mutable
collection.add(1)
collection.add("kolkata")
collection.add(2)
collection.add(1)
collection.add((1, 2, 3))
collection.add("kolkata")
collection.add(1)

print(collection)

# removes an element
collection.remove(1)
collection.remove((1, 2, 3))

print(collection)

# clear the set and make it empty
collection.clear()
print(collection)

# removes a random value
collection2 = {"kolkata", "suman", (1, 2, 3), 2}

print(collection2.pop())

'''
# combines both set values and returns new
set1 = {1, 2, 3, "kolkata", "suman"}
set2 = {3, 4, 5, "kolkata", "python"}

print(set1.union(set2))
print(set1)
print(set2)

# combines common values and return new
print(set1.intersection(set2))