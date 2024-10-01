# To read a file

f1 = open("file.txt")
data = f1.read()
print(data)
f1.close()

# To write in a file

line = "This line will be written on that file"
f2 = open("my_file.txt", "w")
f2.write(line)
f2.close()