class Vector:
    def __init__(self, d1, d2, d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    
    def __str__(self):
        return f"{self.d1}i + {self.d2}j + {self.d2}k"

vec = Vector(7, 8, 10)
print(vec)