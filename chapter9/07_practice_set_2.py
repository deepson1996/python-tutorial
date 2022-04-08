# Problem 4
print("============Problem 4============")

with open("sensor.txt", "r") as f:
    sensorStr = f.read()
    updated = sensorStr.replace("donkey", "######")
print(updated)
with open("sensor.txt", "w") as f:
    f.write(updated)

# Problem 5
print("============Problem 5============")
sensorWords = ["donkey", "eat"]

with open('sensor.txt', "r") as f:
    text = f.read()

for word in sensorWords:
    updated = text.replace(word, "######")

with open('sensor.txt', 'w') as f:
    f.write(updated)

# Problem 6
print("===============Problem 6===========")

with open('log.txt') as f:
    text = f.read().lower()
if("python" in text):
    print("This file contains python")
else:
    print("This file doesnot contains word python")

# Problem 7
print("===========Problem 7============")

text = True
i = 1
with open('log.txt') as f:
    while text:
        text = f.readline().lower()
        if("python" in text):
            print("This file contains python in line", i)
        i+=1


        # else:
        #     print("This file doesnot contains word python")

