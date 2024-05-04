'''

# List is a built in data type in Python
marks = [90.5, 87.3, 81.8, 69.69]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

# We can store different data types in a single list
student = ["Suman", 95, "Kolkata"]
print(student)

# Lists are mutable in nature, so we can change the value
student[0] = "Hunter"
print(student[0])
print(student)

# List Slicing
marks = [96, 64, 66, 87, 99, 79]
print(marks[1:4])
print(marks[0:5])
print(marks[3:])
print(marks[-6:])

'''

# List Methods
list = [3, 2, 1, 4]

# add one element at the end
list.append(5)
# print(list.append(5)) # it returns none
print(list)

# sort in ascending order
list.sort()
# print(list.sort()) # it returns none
print(list)

# sort in descending order
list.sort(reverse=True)
# print(list.sort(reverse=True))
print(list)

# reverse list
list.reverse()
print(list)

# insert element at index
list.insert(5, 6)
print(list)

# removes first occurence of element
list.remove(1)
print(list)

# removes element at index
list.pop(3)
print(list)