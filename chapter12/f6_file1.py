'''
__name__ evaluates to the name of the module in python from where the program is ran

if the module is being run directly from the command line the __name__ is set to string "__main__" Thus this behaviour is used to check whether the module is run directly of imported to another file

'''
def greet(name):
    print(f"Good morning, {name}")

# f7 file maa import garda talako pani run hunchha if nahune banaune ho bhane if condition rakhne
print(__name__) # gives different output calling from different files
if __name__ == "__main__": #(If executing from this file)
    n = input("Enter a name: ")
    greet(n)