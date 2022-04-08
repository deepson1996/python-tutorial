'''
Formats the value inside the string into a desired output

Before using f string as f"{value} this is ...." the format method was used

string formatting

'''
name = "Harry"
channel = "CWH"
a = "This is {} and his channel is {}".format(name, channel) # displays in order

# if order is not actual
b = "This is {1} and his channel is {0}".format(name, channel) # displays in reverse order
print(a, b)
