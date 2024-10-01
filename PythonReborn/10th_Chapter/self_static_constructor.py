class Employee:
    language = "Python" # This is a class attribute
    salary = "123456" # This is a class attribute

    def __init__(self):
        print("This method is automatically called.\nIt is called 'dunder method'")


    def getInfo(self):
        print(f"This language is: {self.language}.\nThe salary is: {self.salary}")


    @staticmethod # This is static method, no need to pass 'self'
    def greet():
        print("Hello, good morning")


sujan = Employee()
sujan.name = "Sujan S" 
sujan.getInfo()
sujan.greet()
