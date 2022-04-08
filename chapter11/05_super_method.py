'''
Super method
    - Super method is used to access the methods of a super class in the derived class

    super() __init__() -> calls constructor of the base class
'''


class Person:
    country = "India"

    def __init__(self):
        print("Initializing person.... \n")

    def takeBreath(self):
        print("I am breathing....")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__() # yesari super class ko constructor init garna milchha
        print("Initializing Employee.... \n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am breating as well .....")


class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        super().__init__() #calls the parent constructor
        print("Initializing Programmer.... \n")
    def getSalary(self):
        print(f"No salary to programmer")


# person = Person()
# employee = Employee()
programmer = Programmer()

# person.takeBreath()
# employee.takeBreath()  # overridden to above
# programmer.takeBreath()  # inherited from above
