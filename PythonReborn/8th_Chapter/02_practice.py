# Write a python program using function to convert Celsius to Fahrenheit

def c2f(c):
    return c*9/5 + 32

celcius = int(input("Enter the value in Celcius: "))
print(f"The Fahrenheit temperature will be: {c2f(celcius)}")