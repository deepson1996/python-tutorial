'''
    lists is collection of variables habing index
    order jun kram maa rakheko hunchha tei kram maa store bhako hunchha
'''

# 1. Creating List
a = [1,2,4,56,6]

# 2 Printing List 
print(a)

# 3 Accessing element from list using index
# Like strings we can access the elements of a list using index
# if index is not present in list it will throw an error like a[11]
print(a[0], a[-1])

# 4 Replacing element in list
# Lists are mutable and we can change the element of a list unlike strings 
a[0] = 99 # It replaces the value of first element with 99
print(a)

#5 Creating list with different types of elements
b = [1, "hello", True, [1,2,3], None] #any data type
print(b)




