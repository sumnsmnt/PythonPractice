# Funtions is a block of code that perform a specific task.
# There are some predefind functions in python like print(), len(), type(), range(), etc.


def calculate_sum1(a, b): #parameters
    sum1 = a + b
    print(sum1)
    return sum1

calculate_sum1(10, 15) #function call; arguments


# We can make it shorter
def calculate_sum2(c, d): #parameters
    return c + d

sum2 = calculate_sum2(15, 30) #function call; arguments
print(sum2)


###########
def print_hello():
    print("Hello")

print_hello()

# calculate the average of 3 numbers
def cal_avg(a, b, c):
    avg = (a + b + c)/3
    print("The average is: ", avg)
    return avg

cal_avg(5, 7, 9)
