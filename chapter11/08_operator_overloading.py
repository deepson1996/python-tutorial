'''
Operators in python can be overloaded using dender methods.
These methods are called when a given operator is used on the objects

Other of these are

p1 + p2 -> p1 __add__(p2)
p1 - p2 -> p1 __sub__(p2)
p1 * p2 -> p1 __mul__(p2)
p1 / p2 -> p1 __truediv__(p2)
p1 // p2 -> p1 __floordiv__(p2)


new data type banako jasto ho tesko add maa len maa ... maa k return garney bhanera dender methods maa overload garne ho


'''

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2): #inbuilt method overload + lai auto add maa lera aauchha
        print("lets add")
        return self.num + num2.num

    def __truediv__(self, num2):
        print("lets divide")
        return self.num / num2.num

n1 = Number(12)
n2 = Number(6)

addition = n1+n2
div = n1/n2

print(addition, div)

