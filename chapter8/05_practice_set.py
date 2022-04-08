# Problem 1
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(greatest(2,9,5))

# Problem 2
def forenheight(celcius):
    return (celcius * 9/5) + 32
n = 37
converted = forenheight(n)
print(F"The converted foreinheit of {n} is {converted}")

# Problem 3
for i in range(5):
    print("hello there ", end="")

# Problem 4
n = 8
def sumOfNaturalNumbers(n):
    if n <= 1:
        return 1
    else:
        return n + sumOfNaturalNumbers(n-1)
sumO = sumOfNaturalNumbers(n)
print(f"The sum of first {n} natural numbers is {sumO}")

# Problem 5

def lines(n):
    for i in range(n, 0, -1):
        print("*" * i)

lines(9)

# Problem 6 
def centi(incles):
    return incles * 2.54
n = 12
converted = centi(n)
print(F"The converted centimeter of {n} inch is {converted}")

# Problem 7 # string strip: "    Harry   k " => strip le extra space remove gardinchha
this = "    Harry   k "
print(this)
print(this.strip())

def removeStrip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

string = "       Harry is a good boy        "
word = "good"
print(removeStrip(string, word))


def multiTable(n):
    for i in range(10):
        print(f"{n} x {i+1} = {n*(i+1)}")

multiTable(15)

