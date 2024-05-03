'''
# if-else 
age = 21
if(age >= 18):
    print("Now you can apply for Driving licence")
else:
    print("Can not apply for Licence")


# if elif else condition
light = "green"

if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("GO")
else:
    print("Light is off")

# if will check all the condition
num = 5
if(num > 2):
    print("Greater than 2")
if(num > 3):
    print("Greater than 3")


# elif will check the first condition
num = 15
if(num > 5):
    print("Greater than 5")
elif(num > 10):
    print("Greater than 10")

'''

# Grade students based on marks

marks = int(input("What's your marks? \n"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Your Grade is: ", grade)