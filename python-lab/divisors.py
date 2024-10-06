# Create a program that asks the user for a number and then 
# prints out a list of all the divisors of that number.

num = int(input("Please enter a number to find divisors: "))
 
divisorList = []

listRange = list(range(1, num+1))

for number in listRange:
    if(num % number == 0):
        divisorList.append(number)

print(divisorList)
