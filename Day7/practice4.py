'''

# Print the elements of the following list using for loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

n = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 1

for i in n:
    i*i
    print(i)
    i += 1

'''


# Search for a number x in this tuple using for loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

n = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = int(input("Enter any number: "))

i = 0

for i in n:
    if(i == x):
        print("number found", i)
        break
    i += 1