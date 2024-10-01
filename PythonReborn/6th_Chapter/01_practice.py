# Write a program to find the greatest of four numbers entered by the user

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))

if (n1>n2 and n1>n3 and n1>n4):
    print(n1, " is the greatest among these 4 numbers")
elif (n2>n1 and n2>n3 and n2>n4):
    print(n2, " is the greatest among these 4 numbers")
elif (n3>n2 and n3>n1 and n3>n4):
    print(n3, " is the greatest among these 4 numbers")
else:
    print(n4, " is the greatest among these 4 numbers")

