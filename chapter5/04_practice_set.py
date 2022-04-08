
#2. Dictionary with nepali word key and english value
nepaliDict = {
    'kaam': 'work',
    'bina': 'without',
    'aafno': 'my',
}
print("Options are: ",nepaliDict.keys())
# a = input("Enter your text: ")
a = "kaam"
print("The value of\"", a, "\"is", nepaliDict.get(a, "Not found in the dictionary"))

#2. input 8 numbers from user and display all unique numbers

# first = input("Enter first number: ")
# second = input("Enter second number: ")
# third = input("Enter third number: ")
# fourth = input("Enter fourth number: ")
# fifth = input("Enter fifth number: ")
# sixth = input("Enter sixth number: ")
# seventh = input("Enter seventh number: ")
# eighth = input("Enter eighth number: ")
# numberSet = {int(first), int(second), int(third), int(fourth), int(fifth), int(sixth), int(seventh), int(eighth)}
numberSet = {1, 1, 3, 5 ,6 ,7 ,8 ,8}
print(numberSet)

#3. Can set contain int as well as string
mixedSet = {18, "18", 18.1}
print(len(mixedSet), mixedSet)
# Yes it can 

#4. What will be the length of given set
s = set()
s.add(20)
s.add(20.0) # this will not add the value because the value is equal but string will be taken as string
s.add("20")
print(len(s))

#5. Type of {}
print(type({})) # dictionary

#6. Create empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.
favLang = {}
# a = input("Enter your favourite language shubham: ")
# b = input("Enter your favourite language sonali: ")
# c = input("Enter your favourite language rajesh: ")
# d = input("Enter your favourite language raj: ")

# favLang["shubham"] = a
# favLang["sonali"] = b
# favLang["rajesh"] = c
# favLang["raj"] = d
favLang["shubham"] = "C++"
favLang["sonali"] = "Java"
favLang["rajesh"] = "JS"
favLang["raj"] = "Python"

print(favLang)

#7. If the name of the friend is duplicate the later one will replace the previous one.

#8. If language is same for two or more it will not matter but stored in value 

#9. Can you change the values inside a list which is contained in set S
# s = {8, 7, 12, "Harry", [1, 2]}
# print(s)
# ==> Set cannot contain list
# ==> if changed to tuple tuple cannot be changed