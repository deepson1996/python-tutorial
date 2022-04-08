'''
Class method:
    A method bound to class and not the object of the class.

    @classmethod decorator is used to create class method

'''

class Employee:
    company = "Camel"
    salary = 100
    location = "Kathmandu"

    def changeSalary(self, sal): 
        #below line doesnot change but add new instance of salary to change it we need to implement class method
        self.salary = sal
        # one method is
        # self.__class__.salary = sal # it changes but  we dont do that 
    @classmethod
    def updateSalary(cls, sal): # by denoting and passing cls parameter it becomes class method
        cls.salary = sal


employee = Employee()

print(employee.salary)
employee.changeSalary(455)
print(employee.salary)
print(Employee.salary) # doesnot change in actual
employee.updateSalary(464)
print(Employee.salary)