'''
Break statement is used to come out of the loop when encountered. It instructs the program esit the loop now
'''

for i in range(1, 10):
    print(i)
    if i == 5:
        break
else:
    print("Loop is completed") # doesnot comes here as the break statement sends out of the context
print("You are out of loop")