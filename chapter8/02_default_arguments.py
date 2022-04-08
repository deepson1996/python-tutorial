'''
    We can set default value for parameters in the function definition
'''
def greet(name = "Guest"):
    print(f"Good day, {name}")

greet("Dipshan")
greet() # it works with default parameter value which is "Guest"
