'''
    Type casting and type function if 345 lai float banaunu paryo bhane
'''
a = "3434"
# sum = a + 5 Not valid as a is not integer and 5 is integer 
print(type(a))
a = int(a) # type casting if the value is not valid int value then it will throw error

sum = a + 5 #Now valid as a is also an integer
print(type(a))
print (sum)

# Similarly string can be converted to number as well 
print(type(str(34)), int("32"), float(34))