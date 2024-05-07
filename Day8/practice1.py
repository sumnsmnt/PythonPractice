# WAF to print the length of a list.(list is the parameter)

list = [1, 2, 3, 4, 5, 6, 7]

def len_list(lists):
    print(len(lists))

len_list(list)


# WAF to print the elements of a list in a single line.(list is the parameter)

num = [11, 22, 33, 44, 55]

def print_list(list):
        for element in list:
              print(element, end = " ")

print_list(num)
print()


# WAF to find the factorial of n.(n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

factorial(6)

# WAF to convert USD to INR
def convert(usd):
     inr = 88 * usd
     print(usd, "USD =", inr, "INR")

convert(1000)


# WAF to print ODD or EVEN
n = int(input("Please enter a number: "))

def odd_even(n):
     if(n % 2 == 0):
          print("EVEN")
     else:
          print("ODD")

odd_even(n)