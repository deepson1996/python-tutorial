age = int(input("How old are you? "))

if(age>34 and age <56):
    print("You can work with us")
else:
    print("You cannot work with us")

if(age>34 or age <56):
    print("You can work with us")
else:
    print("You cannot work with us")

print(not age<56)