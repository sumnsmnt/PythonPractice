# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old.

name = input("What is your name? ")
age = int(input("Please enter your age: "))

new_age = 100 - age

print("Hi!", name)
print("After", new_age, "years, you'll turn 100.")