'''
Reduce needs to be imported
It applies a function to all the elements of an iterable and returns a single value.
'''
from functools import reduce

sum = lambda a, b: a+b #Sums two numbers

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

val = reduce(sum, l) # sum of all the elements in the list 2 by 2
print(val)
