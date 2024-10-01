class Employee:
    a = 1

    @classmethod
    def show(self):
        print(f"The class attribute of Employee is {self.a}")

e = Employee()
e.a = 2

e.show()