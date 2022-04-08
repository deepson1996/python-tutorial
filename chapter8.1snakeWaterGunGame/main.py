'''
Random module ko randint method gives random integer between two integers return garchha
'''
import random


def gameWon(computersChoice, yourChoice):
    print(computersChoice, yourChoice)
    if (computersChoice == yourChoice):
        return None
    elif(computersChoice == 's'):
        if(yourChoice == 'w'):
            return False
        elif(yourChoice == 'g'):
            return True
    elif(computersChoice == 'w'):
        if(yourChoice == 's'):
            return True
        elif(yourChoice == 'g'):
            return False
    elif(computersChoice == 'g'):
        if(yourChoice == 's'):
            return False
        elif(yourChoice == 'w'):
            return True
    

choice = random.randint(1,3)

if choice == 1:
    computersChoice = "s"
elif choice == 2:
    computersChoice = "w"
elif choice == 3:
    computersChoice = "g"


print("Computers turn: Snake(s) or Water(w) or Gun(g): ")
yourChoice = input("Your turn: Snake(s) or Water(w) or Gun(g): ")

result = gameWon(computersChoice, yourChoice)

print(f"Computer chose {computersChoice}")
print(f"You chose {yourChoice}")
if result == None:
    print("The game is a tie!")
elif result == True:
    print("You win!")
elif result == False:
    print("You lose!")

