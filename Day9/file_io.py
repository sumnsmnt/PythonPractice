# Python can used to perform operations on a file. (read and write data)

# Read

f = open("demo.txt", "r")

# data = f.read()
# print(data)
# print(type(data))

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)


# Write and Append

# f = open("demo.txt", "w")

# f.write("I will complete the Python very soon.")

f = open("demo.txt", "a")

f.write("\nI'll get into DevOps after that.")

f.close()

