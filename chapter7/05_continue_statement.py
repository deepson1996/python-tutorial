'''
Continue statement is used to skip the loop and move to next iteration when encountered. It instructs the program to exit the current iteration and move to next iteration.
'''

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

else:
    print("Loop is completed") # doesnot comes here as the break statement sends out of the context
print("You are out of loop")