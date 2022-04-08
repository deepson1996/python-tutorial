'''Class Attributes
    An attribute that belongs to the class rather than a particular object
        

Instance Attributes
    An attribute that belong to a particular object/instance.

Instance attributes take preference over class attributes during assignment & retrieval

'''
#Eg of class attributes : 
class Employee:
    company = "Google" #specific to each class
    salary = 100
harry = Employee()
rajani = Employee()
print(harry.company) # get the company name
print(rajani.company)
Employee.company = "Youtube" # Changing the company for changing class attribute
print(harry.company) # get the company name
print(rajani.company)


#Eg of instance attributes :

harry1 = Employee()
rajani1 = Employee()

harry1.salary = 300 
# rajani1.salary = 400

'''
first_preference: 
checks if salary is present in object
    then display that
second preference:
    else display the salary from class attribute

dubai thauma chhaina bhane error throw garchha


'''

print(harry1.salary, rajani1.salary)


