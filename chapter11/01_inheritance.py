'''
    Dry principle: Donot repeat ...... (functions, classes, inheritance, loops maa hunchha)
    Inheritance:
        Its a way of creating a new class from an existing class

    Like parent->child
    Base class ->Derived or child class
        Derived class maa base class ko method ra attrubute ta aaihalchha & Derived class ko aafno attribute and functions aaihalchha
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

'''
In the above classes Employee is parent class and programmer is base class
We can use the methods and attributes of Employee in Programmer Object
Also we can overwrite or add new attributes and methods in Programmer class

Types of Inheritance
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
'''
