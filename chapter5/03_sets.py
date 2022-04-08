'''
Sets
Set in python is created as dictionary but without key and value pairs
There is another way as well
Set doesnot take repetaion of elements
It removes the duplicate elements except first occurance autometically
Sets are unordered and unindexed 
cannot change the items in set (adding items is repeatedly doesnot change set) but we can add and remove items from set
'''

# creating set
a = {1,3,4,5, 1}
d = {} # is not empty set because it gives empty dictionary 
b = set() # is empty set
print(type(b))
# adding values to set
a.add(23)
b.add(22)
b.add(25)
b.add(37)
b.add(37)
# b.add([4, 5, 6]) # invalid operation list as well as dictionary set maa add garna mildaina because list is not hashable but we can add tuple
b.add((4, 5, 6))

print(type(a), a)
print(type(b), b)
# print(a)

# length
print(len(b))

#remove
print(b)
b.remove(37) # throws error if value doesnot exist
print(b)

#Pop removes one random element and returns but doesnot take index as sets dont have index
deleted = b.pop()
print(deleted, b)

# clear same as others

# union this methods returns doesnot mutate
setA = b
setB = {1,22,3}
unionSet = setA.union(setB)
print(unionSet)

#intersection set
intersectionSet = setA.intersection(setB)
print(intersectionSet)

#difference
differenceSet = setA.difference(setB)
print(setA, setB, differenceSet)
#OR
print(setA - setB)

print(setA^setB) # symmetric difference A maa bhako B maa bhako but intersection maa nabhako




