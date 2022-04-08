'''
    Python offers a finally clause which ensures execution of a piece of coce irrespective of the exception
'''

try:
    i = 'sld'
    c = 1 / i
except Exception as e:
    print(e)
    exit()
finally: # it executes regardless of error or exception
    print("We are done")

print("We are done part 2")