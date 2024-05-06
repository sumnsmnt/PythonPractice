# Range functions returns a sequence of numbers, starting from 0 by default,
# and increased by 1 ( by default), and stops before a specified number.
# range(start, stop, step)


# seq = range(3)
# for i in seq:
#     print(i)


# for i in range(2, 5):
#     print(i)


# for i in range(2, 10, 2):
#     print(i)


# Print numbers from 10 to 1.
for i in range(10, 1, -1):
    print(i)

# Create a multiplication table
n = int(input("Enter any number: "))
for i in range(1, 11):
    print(i * n)


# Pass is a null statement that does nothing.
# It is used a placeholder for future code.

for i in range(5):
    pass
print("We'll work on this later")