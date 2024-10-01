a = (1, 5, 6, 88, 99, 65, 100)
b = (3,)
c = ()
# All of them are tuple, tuple is immutable. So we can't change the elements.
print(type(a))
print(type(b))
print(type(c))

entry = ("Apple", "Mango", 2, 5.6, 2, "Python", "Apple", 2, "Apple")

print(entry)

no = entry.count("Apple")
print(no)

i = entry.index("Python")
print(i)