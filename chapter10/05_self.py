'''
 self refers to the instance of the class which is autometically passed with a function call from an object

 harry.getSalary() -> here self is harry
    equivalent ot Employee.getSalary(harry)
'''

class Employee:
    company = "Google"
    def getSalary(self): # self defines harry here hatayo bhane argument ko error aauchha
        print(f"Salary for this worker working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000

harry.getSalary()
# Its same as Employee.getSalary(harry)
Employee.getSalary(harry) # harry is the argument
