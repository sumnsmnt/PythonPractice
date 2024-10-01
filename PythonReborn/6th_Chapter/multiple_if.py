a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if (a%2 == 0):
    print("The number is even")


if (a>20):
    print("The number is geater than 20")
elif (a<20):
    print("The number is less than 20")
elif (a==20):
    print("The number is equals to 20")
else:
    print("Enter a valid positive number")


if (a%b ==0):
    print("1st number can be divided by 2nd number")
else:
    print("1st number can not be divided by 2nd number")