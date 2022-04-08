'''
    Join Method
    It creates a string from iterable objects
    list, tuple, etc
'''

l = ["Camera", "Laptop", "Mouse", "Keyboard", "Monitor", "CPU", "RAM", "HDD", "SSD"]

# if we want to join the list with and or anything and print as string we use join method

sentance = " and ".join(l)
print(sentance)