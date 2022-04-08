'''
Function is a group of statements performing a specific task

When a program gets bigger in size and its complexity grows, it gets difficult for a programmer to track on which piece of code is doing what

A function can be reused by the programmer in given porgram any number of times

function is defined by def 

Two types
    1. Built functions
        int(), sum(), len(), etc
    2. User Defined functions
        def greet(name): as in this file

We can pass the default value for parameters in the function definition
'''

marks = [45, 78, 86, 77]
marks2 = [46, 79, 87, 78]

percentage1 = ((marks[0]+ marks[1]+ marks[2]+ marks[3])/400)*100
percentage2 = (sum(marks2)/400)*100

print(percentage1, percentage2)

# for the above logic we can use the logic of sum

def percent(marks):
    return (sum(marks)/400)*100

print(percent(marks), percent(marks2))

# Quick quiz
# Write a program to great a user with "Good day" using functions

def greet(name):
    print(f"Good day, {name}")

greet("Dipshan")

def mySum(num1, num2):
    return num1 + num2

print(mySum(10, 20))




