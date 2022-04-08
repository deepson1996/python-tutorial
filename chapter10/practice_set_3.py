class MyClass:
    a  = 1
    @staticmethod
    def greet():
        print("Hello user")

myClass = MyClass()
myClass.a = 0
print(myClass.a)
print(MyClass.a)
# Doesnot changes but
MyClass.a = 0 # It does change the value
print(MyClass.a)

myClass.greet()