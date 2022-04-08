'''
    Property makes method as property

    Settor: its called with property decorater
    can define by @functionName.setter
'''
class Employee:
    company = "Nepal Gas"
    salary = 4500
    salaryBonus = 500
    # totalSalary = 5000 instead of this we make this function

    #is function but we can call it as property emp.totalSalary garera call garna milchha () lagauna pardaina
    @property 
    def totalSalary(self):
        return self.salary + self.salaryBonus

    #setter 
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary) # function as a property

# But can we change it lets check it??
e.totalSalary = 5800 #gives error so we use setter method

print(e.salary, e.salaryBonus, e.totalSalary)