'''
The Data in RAM is volatile. So in orer to persist the data forever, we use file. in Storage device like HDD, SSD etc.

Eg. Game Progress in GTA V is saved in a file.

Python can read and write to file

There are 2 types of files
1. Text files (.txt, .csv, .json, .xml) # notepad maa kholna sakne file haru
2. Binary files (.bin, .jpg, .png, .mp3, .mp4) # binary data hunchha specific tarikale read garera display garnuparchha
    'rb' will open for read in binary mode
    'rt' will open for read in text mode(t by default linchha) 

Several functions can be used to read update and delete files
1. file = open(filename, mode) #mode = r, w, a, r+, w+, a+ (read, write, append, update(+) etc)
    and we can use
        file.read(), file.readline() to read the file
    if mode is not specified it will take r as default



'''

# Open file to read content
# f = open('sample.txt', 'r')
# is same as
f = open('sample.txt')

#read content
# data = f.read()
# we can specify the number of characters in read function as well
data = f.read(5) #read first 5 character but you cannot read 2 times in one open
print(data)

# close file
f.close()

