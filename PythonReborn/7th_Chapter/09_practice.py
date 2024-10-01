# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))

for i in range(1, n+2):
    print(f"{n} X {(n+1)-(i-1)} = {n*((n+1)-(i-1))}")

for i in range(1, n+1):
    print(f"{n} X {(n+1)-i} = {n*((n+1)-i)}")