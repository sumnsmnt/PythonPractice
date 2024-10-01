# Write a program to input eight numbers from the user and display all the unique numbers

s = set()

num = int(input("Enter your 1st number: "))
s.add(int(num))
num = int(input("Enter your 2nd number: "))
s.add(int(num))
num = int(input("Enter your 3rd number: "))
s.add(int(num))
num = int(input("Enter your 4th number: "))
s.add(int(num))
num = int(input("Enter your 5th number: "))
s.add(int(num))
num = int(input("Enter your 6th number: "))
s.add(int(num))
num = int(input("Enter your 7th number: "))
s.add(int(num))
num = int(input("Enter your 8th number: "))
s.add(int(num))

print(s)