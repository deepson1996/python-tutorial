from ast import increment_lineno


class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai / self.salary

employee = Employee()
print(employee.salaryAfterIncrement)

print(employee.increment)
employee.salaryAfterIncrement = 20000 #calls setter method
print(employee.increment)


