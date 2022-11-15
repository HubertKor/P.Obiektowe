import math


class Polynomial():
    def __init__(self, coefficients):
        self.corfficients = list(coefficients)

    def deg(self):
        z = len(self.corfficients) - 1
        y = self.corfficients[:: -1]
        for x in range(len(y)):
            if y[x] == 0:
                z-=1
            else:
                return z
        return z

    def __str__(self):
        return str(self.corfficients)

    def __neg__(self):
        return self.corfficients[::-1]

    def __add__(self, other_poly):
        for x in range(len(self.corfficients)):
            for x in other_poly:
                self.corfficients[x] = self.corfficients[x] + other_poly[x]
                return self.corfficients

    def __sub__(self, other_poly):
        for x in range(len(self.corfficients)):
            for x in other_poly:
                self.corfficients[x] = self.corfficients[x] - other_poly[x]
                return self.corfficients

    def __mul__(self, other_poly):
        for x in range(len(self.corfficients)):
            for x in other_poly:
                self.corfficients[x] = self.corfficients[x] * other_poly[x]
                return self.corfficients

    def __eq__(self, other_poly):
        for x in range(len(self.corfficients)):
            for x in other_poly:
                if self.corfficients[x] != other_poly[x]:
                    return False
                else:
                    return True

    def __call__(self, x):
        return self.corfficients[x]






w = Polynomial([4, 2, 5, 0, 1])

print(w.deg())
print(w.__str__())
print(w.__neg__())
print(w + [1, 2, 3])
print(w.__eq__([4,2,5,0,1]))
print(w.__call__(2))
print((w.__mul__([4, 2, 3, 1, 4])))


class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x and self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x and self.y - other.y)

    def __eq__(self, other):
        if self.x != other.x or self.y != other.y:
            return False
        else:
            return True

    def __len__(self):
        return math.sqrt((self.x)^2 + (self.y)^2)

    def __getitem__(self, item):
        print(type(item), item)

v1 = Vector(3,4)
print(v1.__len__())
test = Vector(3,4)
print(test[3])