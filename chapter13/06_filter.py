'''
Filter: Filter list and returns if the condition is true or false
'''

def greaterThanFive(num):
    if num>5:
        return True
    else:
        return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 45]
g10 = lambda num: num>10
print(list(filter(greaterThanFive, l)))
print(list(filter(g10, l)))