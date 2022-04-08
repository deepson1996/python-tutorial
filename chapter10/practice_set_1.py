class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getInformation(self):
        information = {
            "name": self.name,
            "salary": self.salary,
            "company": self.company
        }
        return information

harry = Programmer("Dipshan", 20000)
print(harry.getInformation())
