class Calculator:
    def __init__(self, number):
        self.number = number

    def findSquare(self):
        return self.number**2

    def findCube(self):
        return self.number**3
    
    def findSquareRoot(self):
        return self.number**0.5

# calc = Calculator()
# calc.number = 34
calc = Calculator(16)
print(f"Values for {calc.number} Square is {calc.findSquare()} Cube is {calc.findCube()} and square root is {calc.findSquareRoot()}")