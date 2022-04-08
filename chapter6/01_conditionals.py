'''
if else elif
else if haina elif hunchha

euta condition ko bata only one execute hunchha

indentation: 4 spaces or one tab

Else is not mandatory we can not use it with elif as well as 
'''
#1. if elif else ladder
a = 1
if(a<3):
    print("The value of a is less than 3")
elif(a>3):
    print("The value of a is greater than 3")
else:
    print("The value of a is equal to 3")

#2. Multiple if statements if all are matched all will be executed
if(a<3):
    print("The value of a is less than 3")
if(a>3):
    print("The value of a is greater than 3")
if(a == 3):
    print("The value of a is equal to 3")

#3. quick quiz

age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")




