class Employee:
    company = "TCS"
    def show(self):
        print(f"The name of the Employee is {self.name} and salary is {self.salary}")

    
class Programmer(Employee):
    company = "ITC"
    def showLanguage(self):
        print(f"{self.name} is good with {self.language}")


a = Employee()
b = Programmer()

print(a.company, b.company)