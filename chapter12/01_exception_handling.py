'''
Exception Handling in Python
There are many built in exceptions which are raised in python when something goes wrong. Exceptions in Python can be handled using a try statemenr. The code that handles the exception is written in the except clause.

Nameerror, Memory Error, ZeroDivisionEror, Type error, Value Error
int(string) something/0, 

When the exception is handled, the code flow contains without program interruption.
'''
while True:
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("You entered number greater than 6")
        else:
            print("You entered number less than or equal to 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")
print("Thanks for playing this game")


