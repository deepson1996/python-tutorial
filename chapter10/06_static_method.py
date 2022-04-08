'''

'''

class Employee:
    company = "Google"
    def getSalary(self, signature): 
        print(f"Salary for this worker working in {self.company} is {self.salary} \n{signature}")
# for  this kind of functions that doesnot require self to operate we can make it static method
    @staticmethod # this is a decorator
    def greet():
        print("Good morning Sir")

    @staticmethod
    def getTime():
        print("The time is 9 am in the morning")

harry = Employee()
harry.salary = 10000

harry.getSalary("Thanks!") # we can pass additional arguments in this way
harry.greet()
harry.getTime()