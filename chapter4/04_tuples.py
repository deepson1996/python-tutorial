'''
Tuples are inside () brackets.
Tuples are immutable. means tuple cannot be updated or changed.
() This is emptly tuple
(a,) This is a single element tuple it needs , at the end if tuple has only one element

'''
# 1 Creating a tuple
t = (1, 2, 4, 5)

#printing tuple and element
print(t, t[2])

# t[0] = 3 #invalid as tuple cannot be updated throws error

emptyTuple = () #empty tuple
print(emptyTuple)

singleElementTuple = (1, ) #single element tuple (a) is invalid for single element tuple
print(singleElementTuple)



# Slicing is same as list
print(t[:2]) #prints first two elements



