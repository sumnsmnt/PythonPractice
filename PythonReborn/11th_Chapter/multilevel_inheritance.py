class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

# Employee can only access a attribute
o = Employee()
print(o.a)

# Programmer can only access a and b attribute
o = Programmer()
print(o.a, o.b)

# Manager can access a, b and c attribute
o = Manager()
print(o.a, o.b, o.c)

