a = None

if(a is None): #a and None both are pointing to same object so we are using is here but == checks the value for both
    print("a is None")
else:
    print("a is not None")

b = [45, 56, 6]
if(56 in b):
    print("56 is in b")

print (a == None) # it ckechs value