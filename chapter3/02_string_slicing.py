from unicodedata import name

greeting = "Good morning, "
name = "harry"
# print(type(name))

# string concatenation
c = greeting + name 
# print(c)

# Positive index 0, 1, 2, 3, ........
print (c[1]) # prints the second character like in array

# Negative index -1, -2, -3, ....
print (c[-1]) # prints the last character

# but it cannot be changed 
# c[0] = 'A' #invalid

# Slicing strings from position: to position+1:
print (c[0:4]) # (0 dekhi 3 samma ko index)

print(c[3:8]) # (3 dekhi 7 samma ko index)

print(c[0:-1]) # (0 dekhi end -1 samma ko index)

print(c[:5]) #  = [0:5]
print(c[5:]) #  = [5:end]


print("========================================================")

# Slicing with skip value
name = "Harryis good"
print(name[0::2]) # (0 dekhi end samma ko index) skip every second value = Good = G..o.. = Go
print(name[::3]) # (0 dekhi end samma ko index) skip every third 

                




