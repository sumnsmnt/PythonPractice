# Write a python function to print multiplication table of a given number.

def multi(n):
    for i in range(1, n+1):
        print(f"{n} X {i} = {n * i}")

multi(10)