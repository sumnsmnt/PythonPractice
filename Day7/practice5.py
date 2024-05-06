# WAP to sum of first n numbers using while loop.

n = int(input("How many numbers you want? "))

i = 0
sum = 0

while i < n:
    i += 1
    sum += i
print(sum)


# WAP to find the factorial of first n natual numbers using for loop

n = int(input("Enter any number: "))

fact = 1

for i in range(1, n+1):
    fact = fact * i
print(fact)