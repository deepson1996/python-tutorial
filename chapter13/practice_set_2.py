name = input("Enter your name: ")
marks = input ("Enter your marks: ")
phone = input("Enter your phone number: ")

string = "Hello {0}, your phone number is {2} and your marks is {1}".format(name, marks, phone)
print(string)