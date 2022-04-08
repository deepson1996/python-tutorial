#Problem 1
# name = input("Enter your name\n")
name = "Hello  Dipshan space  is space"
print ("Good Afternoon,", name)

# Problem 2 
letter = '''Dear <|Name|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected !
Have a great day ahead!
Thanks with regard
Harry!
Date: <|Date|>'''
# date = input("Enter date\n")
date = "27 dec 2019"
letter = letter.replace("<|Name|>", name) # assign garnu parchha aafuma replace hudaina
letter = letter.replace("<|Date|>", date)

print("================")
# Problem 3
spaces = letter.count("  ")
hasSpaces = letter.find("  ")
print("Number of double spaces:", spaces, "Has spaces:", hasSpaces)

# Problem 4 
space_replaced = name.replace("  ", " ")
print(space_replaced)

# Problem 5
letter = "Dear Harry,\n\t\"This Python Course is nice.\"\n\t\t\tThanks!"
print(letter)
