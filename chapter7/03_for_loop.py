'''
forloop is used to iterate through a sequence like list, tuple or string [iterables]
Syntax:
for item in iterable:
    statements

For loop can also take for loop else like while loop


Range function:
The range function in python is used to generate a sequence of numbers.
We can also specify the start stop and step-size of the sequence.

for loop jastai ho range function

'''
#For loop
fruits = ["Apple", "Banana", "Cherry", "Grapes", "Mango"]
for fruit in fruits:
    print(fruit)

print("==================first==================")

#Range function
for i in range(5): #starts from 0 goes upto 4
    print(i)
print("==================second==================")
for i in range(1, 11): #starts from 1 goes upto 10
    print(i)
print("==================third==================")
for i in range(1, 11, 2): # starts from 1 goes upto 10 with by printing every second character 
    print(i)


("==================fourth==================")
for i in range(1, 11, 2): 
    print(i)
else: # forloop sakkine bitikai else execute hunchha
    print(i, "is not present")

