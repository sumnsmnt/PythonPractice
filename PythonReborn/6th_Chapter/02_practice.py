# Write a program to find out whether a student has passed and failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

phy = int(input("Marks in Physics: "))
chem = int(input("Marks in Chemistry: "))
bio = int(input("Marks in Biology: "))

total_percent = (phy + chem + bio)/3

if (total_percent >= 40 and phy >=33 and chem >= 33 and bio >= 33):
    print("You are pass")
else:
    print("You failed")