# Common list methods
# Most Methods present in list class are mutable and operates to itself but doesnot return so we cannot assign to new variable

# from os import remove


l1 = [1,8, 7, 2, 21, 15]

#  1 Sorting the list 
# l1_sorted = l1.sort() #invalid because it doesnot return but sorts the actual list
# Correct method 
l1.sort() #sorts the original sort
print(l1)

# 2 Reverse the list
l1.reverse()
print(l1)

# 3 Append element to list
# adds element at the end of the list
l1.append(43)
print(l1)

# 4 Insert element to the list
# inserts element at the specified index and shifts the elements after that index
l1.insert(2, 99)
print(l1)

#  5 Deleting and returning element by index from the list
# deletes the element at the specified index and returns the deleted element
# if index is not given it deletes the last element
removed = l1.pop()
removed = l1.pop(3)
print(removed, l1)

# 6 Deleting element by value from the list and doesnot returns anything
# deletes the first element with the specified value
l1.remove(99)
print(l1)

# 7 Extending the list
# adds the elements of list or the iterable to the end of current list
fruits = ['apple', 'banana', 'cherry']
cars = ['bmw', 'audi', 'toyota']
fruits.extend(cars) # fruits = fruits + cars
print(fruits)

# List ko aru pani tannai method haru chha python docs maa gayera check garnu
# count: like string count elements with the specified value
# clear: remove all elements from list
# copy: returns a copy of the list
# index: returns the index of the first element with the specified value







