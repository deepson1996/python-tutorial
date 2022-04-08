'''
    We can raise(throw) custom exception using the raise keyword in python
'''



def increment(num):
    try:
        return (int(num) + 1)
    except Exception as e:
        raise ValueError("This is not good - Harry")

print(increment("asd"))