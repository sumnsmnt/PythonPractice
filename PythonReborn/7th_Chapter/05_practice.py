# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number: "))
product = 1
for i in range(1, n+1):
    product *= i

print(f"The factorial of {n} is {product}")