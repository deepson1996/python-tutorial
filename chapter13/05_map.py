'''
    Map
    If one function needs to be applied to all the elements  then we use map function

    It applies a function to all the elements of an iterable and returns map object which can be typecasted to list.
'''

def square(a):
    return a*a

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# method 1
l2 = []
for i in l:
    l2.append(square(i))
print(l2)

# Method using map function 
print(list(map(square, l)))