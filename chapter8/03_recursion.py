'''
Recursion is a function which calls itself

It is used to directly use a mathematical formula as a function

Its used to implement the beauty of mathematics

Factorial
    n! = 1 * 2 * 3 * 4 ....*n
    n! = [1 * 2 * 3 * 4 ....*n-1] * n
    n! = (n-1)! * n
    n! = n * (n-1)!

The programmer need to be extremely careful while working with recursion to ensure that the function doesnot infinity keep calling itself. Recursion is sometimes the most direct way to code an algorithm.

'''

# Without function
# n = 5
# fact = 1
# for i in range(n):
#     fact = fact * (i+1)

# print(fact)

# With function
def factorial_iter(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact
f = factorial_iter(5)
print(factorial_iter(5), f)

# with recursion

def factorialRecursive(n): # CALLS UNTILL N IS 1
    if n <= 1:
        return 1
    else:
        return n * factorialRecursive(n-1)


print(factorialRecursive(3))

