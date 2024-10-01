# Write a python function which converts inches to cms

def i2c(i):
    return i*2.54

n = int(input("Enter inches: "))
print(f"The value in cm is: {i2c(n)}")