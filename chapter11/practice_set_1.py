class C2Dvector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j \n"


class Vector3D(C2Dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        # self.icap = i
        # self.jcap = j
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


vector2 = C2Dvector(1, 3)
vector3 = Vector3D(2, 5, 7)

print(vector2, vector3)
