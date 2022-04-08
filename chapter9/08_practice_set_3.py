# Problem 8
import os


print("=============Problem 8=========")
with open('this.txt') as f:
    content = f.read()
with open('copy_this.txt', 'w') as f:
    f.write(content)

# Problem 9
print("=============Problem 9=========")
with open('this.txt') as f:
    content1 = f.read()
with open ('copy_this.txt') as f:
    content2 = f.read()

if(content1 == content2):
    print("identical")
else:
    print("not identical")

# Problem 10
print("=============Problem 10=========")
with open("wipe.txt", 'w') as f:
    f.write("")

# Problem 11 Rename a file
print("=============Problem 11=========")
oldname = "raname_undone.txt"
newname = "rename_done.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)

os.remove(oldname)



