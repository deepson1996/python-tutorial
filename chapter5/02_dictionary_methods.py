'''Dictionary Methods'''
myDict = {
    "fast" : "In a quick manner",
    "harry" : "A coder",
    "marks" : [90, 25, 67, 45, 80],
    "anotherdict" : {'a': 1, 'b': 2, 'c': 3},
    1:2
}

# Getting all the keys of dictionary in dict_keys type
print(myDict.keys())
#can be converted to list
print(list(myDict.keys()))

# Values of dictionery
print(myDict.values()) # dict_values type

#tuples of key value (key, value) for all contents of dictionary
print(myDict.items()) # dict_items type

# Updating dictionary by adding new key value pairs
# if key already exists, it will override the previous value
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Shubham": "Friend",
    "harry": "Decoder"
}
myDict.update(updateDict) # like extend in list
print(myDict)


# Get the value of a key like myDict["Lovish"]
# difference is [] throws error if key not found but get returns None
# key error bata bachna lai get use garne ho
print(myDict.get("Lovish"))

# remove and return last element
a = myDict.popitem()
print(a, myDict)

# from keys: Inserts value to the dictionary
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x)
thisdict1 = dict.fromkeys(x, y)

print(thisdict)
print(thisdict1)

# set default value of key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

a = car.setdefault("submodel", "Bronco")
b = car.setdefault("brand", "Hyundai")

print(car, a, b)

'''Other methods are
clear :removes all elements from dictionary
copy : returns a copy of the dictionary
fromkeys : returns a dictionary with the specified keys and values
pop : removes the element with the specified key and returns the element value requires the key
popitem : removes the last inserted item(key, value) pair and returns it
setdefault : returns the value of the specified key. If the key does not exist, insert the key, with the specified value

'''