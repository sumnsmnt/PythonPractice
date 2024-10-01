# Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * * 

n = int(input("Enter the row number: "))

for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")