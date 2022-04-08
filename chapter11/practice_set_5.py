class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in range(len(self.vec)):
            str1+= f"{self.vec[i]}a{index} + "
            index += 1
        return str1[:-2]

    def __add__(self, another):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + another.vec[i])
        return newList

    def __mul__(self, another):
        sum = 0
        for i in range(len(self.vec)):
            sum+= self.vec[i] * another.vec[i]
        return sum
    def __len__(self):
        return (len(self.vec))

    

# v1 = Vector([1, 4, 5])

v1 = Vector([1, 4, 6, 20])
v2 = Vector([1, 6, 9, 10])

print(v1)
print(v2)

print (len(v2))

print(v1 + v2)
print(v1*v2)