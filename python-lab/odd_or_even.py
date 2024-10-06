# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user.

num = int(input("Please enter a number to check: "))

if(num % 2 ==0):
    print(num, "is even number")
else:
    print(num, "is odd number")