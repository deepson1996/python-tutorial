'''
Single inheritance
    - When child class inherits a single parents class (base->derived)
    - The above example is single inheritance
'''

#Base class
class Employee:
    company ="Google"
    def showDetails(self):
        print(f"This is an employee of {self.company}")
        
    def showDetails2(self):
        print(f"2. This is an employee of {self.company}")


#Derived class child of Employee
class Programmer(Employee):
    language="Python"
    company = "Youtube"
    def getLang(self):
        print(f"The language is {self.language}")

    def showDetails2(self):
        print("This is programmer")

employee = Employee()
employee.showDetails()
programmer = Programmer()
programmer.showDetails() # method inherited from employee 

print("===========Override=========")

# override
employee.showDetails2() #employee class
programmer.showDetails2() #programmer class ko override bhako

print(employee.company)
print(programmer.company)