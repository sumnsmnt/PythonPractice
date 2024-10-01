str = "\nThis line will be append on the file"

f = open("my_file.txt", "a")
f.write(str)
f.close()