# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
# num4 = int(input("Enter fourth number"))


# problem 1

num1 = 5
num2 = 6
num3 = 7
num4 = 4

if num1>num2 and num1>num3 and num1>num4:
    print(str(num1) + " is the largest number")
elif num2>num3 and num2>num4:
    print(str(num2) + " is the largest number")
elif num3>num4:
    print(str(num3) + " is the largest number")
else:
    print(str(num4) + " is the largest number")

# problem 2
mark1 = 36
mark2 = 50
mark3 = 34

percentage = (mark1+mark2+mark3)/3
print(percentage)

if(percentage <40):
    print("You have failed the exam")
elif(mark1<33 or mark2<33 or mark3 <33):
    print("You have failed the exam")
else:
    print("You have passed the exam")


#problem 3
comment = "Buy now a book that you enjoy reading"
comment = comment.lower()
spam = False
if("make a lot of money" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("click this" in comment):
    spam = True
elif("subscribe this" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("This message is spam")
else:
    print("This message is not a spam")


#problem 4
username = "hellou"
if len(username) > 10:
    print("This username contains more than 10 characters")
else:
    print("This username contains less than 10 characters")

#problem 5
name = "Dipshan"
namelist = ["Ram", "Shyam", "Dipshan1"]

if name in namelist:
    print("The given name is present in the list")
else:
    print("The given name is not present in the given string")


#problem 6
marks = 69
if(marks>=90 and marks<=100):
    print("Ex")
elif(marks>=80 and marks<=89):
    print("A")
elif(marks>=70 and marks<=79):
    print("B")
elif(marks>=60 and marks<=69):
    print("C")
elif(marks>=50 and marks<=59):
    print("D")
elif(marks>=40 and marks<=49):
    print("E")
else:
    print("F")    

#problem 7
post = "Hello World My name is Harfry kuram amatya. I am a good. How are you there"

if "harry" in post.lower():
    print("The post is talking about harry")
else:
    print("The post is not talking about Harry")

    


