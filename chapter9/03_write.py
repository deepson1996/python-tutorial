'''
In order to write to a file we first open it in write or append mode after which, we use the f.write() method to write to the file!

If the file is not presents its created autometically

If the file is present it will overwrite the content

If we want to add at last we need to open in append mode

unline f.read() f.write() can be executed any number of time on file process

'''

f = open('another.txt', 'w') #
f.write("Please write this to the file")
f.write("this is appended to first text")
f.close()

