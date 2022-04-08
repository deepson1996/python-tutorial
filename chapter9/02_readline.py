'''
    Readline: This function reads the line of the input file line by line.
    How many time we use the method it reads next line to the current

    'rb' will open for read in binary mode
    'rt' will open for read in text mode(t by default linchha)
'''
f = open('sample.txt')

#read first line
data = f.readline()
print(data)
#read second line
data = f.readline()
print(data)

# and so on
data = f.readline()
print(data)

f.close()