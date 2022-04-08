'''
In order to append to a file we first open it in append mode after which, we use the f.write() method to append to the file!

If the file is not presents its created autometically

If the file is present it will append the content at last

Its same as write except the mode "a" while open function

'''

f = open('another2.txt', 'a') #
f.write("Please append this to the file")
f.close()

