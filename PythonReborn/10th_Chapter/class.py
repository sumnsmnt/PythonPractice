class Employee:
    language = "Python" # This is a class attribute
    salary = "123456" # This is a class attribute

suman = Employee()
suman.name = "Suman S" #This is a instance attribute
print(suman.name, suman.language, suman.salary)

sujan = Employee()
sujan.name = "Sujan S" #This is a instance attribute
sujan.language = "HTML" # instance attribute takes preferance
print(sujan.salary, sujan.language, sujan.name)


