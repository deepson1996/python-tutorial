'''
    Sometimes we want to run a piece of code when try was successful in such case we use else
'''
try:
    i = "as"
    c = 1 / i
except Exception as e:
    print(e)
else: # If exception doesnot occure than only else block is occured
    print("No exception occured in try block")