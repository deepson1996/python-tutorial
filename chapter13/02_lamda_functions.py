'''
Lambda functions
    Functions created using and expression using lambda keyword

    lamda arguments: expressions (can be used as a normal function)

    Function as an arguments pass garnuparne thauma lambda function use garchham

    One line function
'''
# Traditional method for writing function
def func(a):
    return a+5
x = 566
print(func(x))

# Lamda method for writing function
func2 = lambda a: a+5 # here a is input argument and a+5 is its return value
print(func2(x))

summation = lambda a, b, c: a+b+c
print(summation(3, 8, 5))


