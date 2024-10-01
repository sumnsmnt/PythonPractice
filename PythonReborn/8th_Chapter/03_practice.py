# How do you prevent a python print() function to print a new line at the end.

print("a", end="")
print("b")
print("c", end="")
print("d")

# Write a recursive function to calculate the sum of first n natural numbers.


def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(f"The Sum is : {sum(5)}")