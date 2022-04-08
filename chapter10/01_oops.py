'''
Object oriented programming

Solving a problem by creating objects is one of the most popular approaches in programming. This is called object-oriented programming.

The concept focuses on using reusable code
    it implements dry principle
    used for code reuse

A class is a blueprint for creating objects.
    Inheritance, oop, polymorphism, abstraction, encapsulation

Class has methods as well as variables

example of class: Blank form
example of object: Filled form

Object is instantiation of a class. When class is defined, a template(info) is defined. Memory is allocated only after object instantiation

Objects of a given class can invoke the methods available to it without reading the implementation details to the user. (Abstraction and encapsulation)
'''
# Normal method (procedular oriented programming)
a = 12
b = 34
print("The sum of a and b is ", a+b)

# OOP (Object oriented programming)
class Number:
    def sum(self):
        return self.a + self.b

number = Number()
number.a = 12
number.b = 34
s = number.sum()

print(s)


