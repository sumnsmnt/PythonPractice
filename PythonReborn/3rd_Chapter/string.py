name = "SUMAN"

# Indexing starts from 0 (starting to ending)
# We can do backward indexing from -1 (ending to starting)

print(name[:5])
print(name[0:])

positive_slice = name[0:3]
negative_slice = name[-4:-1]

print(positive_slice)
print(negative_slice)

number = "01234567890"
print(number[0:10:3]) # it will print from 0th index to 10th index for every 3rd number