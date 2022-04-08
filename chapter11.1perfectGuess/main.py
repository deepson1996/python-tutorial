import random
randNumber = random.randint(1,100)
print(randNumber)
with open ("hiscore.txt", 'r') as f:
    hiscore = f.read()
    if(hiscore == ""):
        hiscore = 99999999
    else:
        hiscore = int(hiscore)
print("Your hi score is :", hiscore)
totalGuesses = 0
while True:
    guess = int(input("Enter your guess: "))
    if(guess == randNumber):
        print("You guessed it right")
        break
    else:
        if(guess > randNumber):
            print("You guessed it wrong! Enter smaller number")
        else:
            print("You guessed it wrong! Please enter larger number")
    totalGuesses += 1
print("Total attempts: ", totalGuesses)




if(totalGuesses < hiscore):
    print("You have just broken the record")
    with open("hiscore.txt", "w") as f:
        f.write(str(totalGuesses))