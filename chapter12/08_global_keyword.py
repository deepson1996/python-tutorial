'''
    Global keyword is used to modify the variable outside of the current scope

    Global use garena bhane chhuttai hunchha bhitrako bahira ko variable same name bhayepani use hunna
'''

a = 54 # Global variable
def func1():
    a = 8 # if not set 54 prints this replaces but for this function only Local bariable
    print(a)

func1()
print(a) # Global

b = 54 # Global variable
def func2():
    global b # Uses global valiable
    b = 8  # sets to global variable
    print(b)

func2()
print(b) # Global

