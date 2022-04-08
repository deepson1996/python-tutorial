'''
Multiple inheritance:
    - When the child class inherits from more than one parent class

    - (parent1, parent2, ... parentn) -> child

'''

class Employee:
    company = "Visa"
    eCode = "120"

class Freelancer:
    company = "Fiverr"
    lavel = 0
    def upgradeLevel(self):
        self.lavel+=1

#Multiple inheritance
class Programmer(Employee, Freelancer):
    name = "Rohit"

programmer = Programmer()
print(programmer.lavel)
programmer.upgradeLevel()
print(programmer.lavel)

print(programmer.company) # if the attribute is present in multiple parents and not in child, calling it from clild will execute the it from the first inherited class

class AnotherProgrammer(Freelancer, Employee): 
    name = "Sujan"

sujan = AnotherProgrammer()
print(sujan.company) #berore freelance bhayera before ko aauchha


