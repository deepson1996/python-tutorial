'''
--inti__() is  a Constructor
its a special method that is called when an object is created.

It takes self argument and can also take further arguents
 
'''

class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
 
harry = Employee("Harry", 20000, "Youtube") # the constructor is called here
harry.getDetails()


