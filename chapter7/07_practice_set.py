# Problem 1
givenNumber = 39
for i in range(1, 11):
    # print("{0} x {1} = {2}".format(givenNumber, i, givenNumber*i))
    # print (str(givenNumber) + " * " + str(i) +" = " + str(givenNumber*i))

    print(f"{givenNumber} x {i} = {givenNumber*i}")

# Problem 2
l1 = ["Harry", "Sally", "Mary", "John", "Sue"]

for name in l1:
    # if(name.lower().find("s") == 0):
    #     print(name)
    if(name.lower().startswith("s")):
        print(name)

# Problem 3
    i = 1
    while i <= 10:
        print(f"{givenNumber} X {i} = {givenNumber*i}")
        i = i + 1

# problem 4
number = 1
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break

if(prime):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


# problem 5
n = 4
sum = 0
i = 1
while i <= n:
    sum+=i
    i+=1

print(f"Sum of first {n} natural numbers is {sum}")

# problem 6
givenNumber = 4
factorial = 1
for i in range (givenNumber, 1, -1):
    factorial *= i

print(f"Factorial of {givenNumber} is {factorial}")


# problem 7
n = 3
for i in range (n):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1))

# problem 8
string = ""
for i in range(1, 4):
    for j in range(0, i):
        string += "*"
    string += "\n"
print (string)


for i in range(4):
    print("*" * (i+1))


# problem 9
n = 4
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * (n))
    else:
        print("*" + " " * (n-2) + "*")

number = 10
for i in range(10, 0, -1):
    print(f"{number} X {i} = {number*i}")

    

