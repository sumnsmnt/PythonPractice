class Employee:
    company = "TCS"
    salary = "12 LPA"
    name = "Suman S"
    def show(self):
        print(f"The name of the Employee is {self.name} and salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"{self.name} is expert in {self.language}")

    
class Programmer(Employee, Coder):
    company = "ITC"
    def showLanguage(self):
        print(f"{self.name} is good with {self.language} and his salary is {self.salary} and company is {self.company}")


a = Employee()
b = Programmer()


b.show()
b.printLanguage()
b.showLanguage()