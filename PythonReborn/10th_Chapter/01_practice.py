# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age

p1 = Programmer("Suman", "26", "123321")
print(p1.name, p1.age, p1.salary)

p2 = Programmer("Sujan", "20", "321123")
print(p2.name, p2.age, p2.salary)