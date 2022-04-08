# Problem 1 
'''

'''
f = open('poems.txt')
text = f.read()

if('twinkle' in text):
    hasText = True
else:
    hasText = False

print(hasText)
f.close()

# Problem 2
print("============Problem 2============")
def game():
    return 39

score = game()
with open("hiscore.txt", "r") as f:
    hiscoreStr = f.read()
if hiscoreStr == "":
    with open("hiscore.txt", 'w') as f2:
        f2.write(str(score))
elif(score > int(hiscoreStr)):
    with open("hiscore.txt", 'w') as f2:
        f2.write(str(score))

# Problem 3
print("============Problem 3============")

for i in range(2, 21):
    with open(f"tables/multiplication{i}.txt", "w") as f:
        for j in range(10):
            f.write(f"{i} * {j+1} = {i*(j+1)}\n")




