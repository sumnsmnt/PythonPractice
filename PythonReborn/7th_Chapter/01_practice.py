# Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")



n = int(input("Enter a number: "))
i = 1
while(i<=10):
    print(f"{n} X {i} = {n*i}")
    i +=1