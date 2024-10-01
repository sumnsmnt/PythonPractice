# Write a program using functions to find greatest of three numbers.

def greatest(n1, n2, n3):
    if(n1>n2 and n1>n3):
        print(f"{n1} is the greatest among all")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is the greatest among all")
    else:
        print(f"{n3} is the greatest among all")

greatest(45, 56, 67)
