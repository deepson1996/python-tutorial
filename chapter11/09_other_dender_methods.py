'''
Other Operators

__str__(), __len()__
'''


class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num

    def __str__(self): # overloaded check without it and with it
        return f"Decimal number: {self.num}"

    def __len__(self):
        return 1

    
n = Number(9)
print(n)

print(len(n)) # gives before overloading