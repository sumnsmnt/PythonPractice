# Write a recursive function to calculate the sum of
# first n natural numbers.

# def cal_sum(n):
#     sum = 0
#     i = 0
#     for i in range(1, n+1):
#         sum = sum + i
#         i += 1
#     print(sum)

# cal_sum(5)

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

print(cal_sum(5))


# Write a recursive function to print all elements in a list.
# Use list & index as parameters.

lists = [1, 3, 5, 7, "Suman", "India"]

def print_ele(list, idx = 0):
    if(idx == len(lists)):
        return 
    print(list[idx])
    print_ele(list, idx+1)

print_ele(lists)