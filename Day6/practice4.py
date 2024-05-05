# Figure out a way to store 9 & 9.0 as separate values in the set

values = {9, 9.0} # it will not work as both conciderd as 9
print(values)

values = {9, "9.0"} # we can make one element as string
print(values)

# we can store in a dictionary in the form of tuples
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)