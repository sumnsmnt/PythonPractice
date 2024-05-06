# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Which number you want to find? "))

idx = 0

while idx < len(tup):
    if(tup[idx] == x):
        print("Found at index", idx)
    idx += 1
