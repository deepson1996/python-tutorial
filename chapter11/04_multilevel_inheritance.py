'''
Multilevel Inheritance
    - When the child class becomes a parent of another alild class

    - parent1-> childparent -> child
'''

class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am breating as well .....")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")

person = Person()
employee = Employee()
programmer = Programmer() 

person.takeBreath()
employee.takeBreath() # overridden to above
programmer.takeBreath() # inherited from above


