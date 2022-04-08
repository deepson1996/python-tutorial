'''
    Dictionary
    key, value pair (Like json)
    value can be of any type (int, string, list, dictionary, float, etc)
    It is unordered unlike list and tuple but key hunchha

    It is mutable and can be changed

    Cannot use duplicate keys is attempted it will override the previous value
'''

# Create a dictionary
myDict = {
    "Fast" : "In a quick manner",
    "Harry" : "A coder",
    "Marks" : [90, 25, 67, 45, 80]
}

# Print the dictionary
print(myDict)

# Print the value of the key "Fast"
print(myDict["Fast"], myDict["Harry"], myDict["Marks"])
print(myDict["Marks"][0]) # inside maa bhako list, dictionary, tuple yesari access garna milchha

# Changing value of a key
myDict["Fast"] = "In a slow manner" #override hunchha
print(myDict)

# Adding a new key value pair
myDict["added"] = "new item" # new key added
print(myDict)




