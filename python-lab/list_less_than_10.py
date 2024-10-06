# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 97]
# and write a program that prints out all the elements of the list that are less than 10.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 97]

print( [ x for x in a if x<10 ] )