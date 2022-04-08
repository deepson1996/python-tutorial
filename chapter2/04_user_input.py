'''
User sanga input lina ko laagi input function ko use hunchha

input function always returns string value if we need to convert it to integer or float then we need to use typecasting
'''
a = input("Enter your name: ")
print(a, type(a))
a = int(a) # if valid else throws error
print(type(a))

