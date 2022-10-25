# zad1
def nwd(a: int, b: int) -> int:
    if b == 0:
        return a
    return nwd(b, a % b)

class Wymierna(object):
    def __init__(self, p: int = 0, q: int = 1):
        if type(p) != int:
            p = int(p)
        if type(q) != int:
            q = int(q)

        nwdValue = nwd(q, p)

        if nwdValue != 1:
            q = int(q / nwdValue)
            p = int(p / nwdValue)

        if q < 0:
            p = -p
            q = -q

        self.p = p
        self.q = q

    @staticmethod
    def wzglednie_pierwsze(p, q):
        while q:
            p, q =q, p % q
        return abs(p) == 1

    def get_licznik(self):
        return self.p

    def get_mianownik(self):
        if self.q > 0:
            return self.q
        else:
            return False

    def __repr__(self):
        return f'{self.p} / {self.q}'

    def __float__(self):
        return float(self.p/self.q)

    def __add__(self, other):
        iloMianowniku = self.q * other.q
        if iloMianowniku < 0:
            iloMianowniku = -iloMianowniku

        self.p *= int(iloMianowniku / self.q)
        other.p *= int(iloMianowniku / other.q)

        return Wymierna(self.p + other.p, iloMianowniku)

    def __sub__(self, other):
        return self + Wymierna(-other.p, other.q)

    def __eq__(self, other):
        return self.p == other.p and self.q == other.q

    def __ne__(self, other):
        return self.p != other.p and self.q != other.q

    def __gt__(self, other):
        if self.p < 0 < other.p:
            return True
        if self.p > 0 > other.p:
            return False

        ratio = (self.p / other.p) / (self.q / other.q)

        if self.p > 0 and self.q > 0:
            return ratio < 1
        return ratio > 1

    def __ge__(self, other):
        if self.p == other.p and self.q == other.q:
            return True

        return self > other

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    def __mul__(self, other):
        return Wymierna(self.p * other.p, self.q * other.q)

    def __truediv__(self, other):
        return Wymierna(self.p * other.q, self.q * other.p)

    def eq2(self, other):
        return not (self > other or self < other)






liczba = Wymierna(1, 4)
liczba2 = Wymierna(3, 5)
print(liczba.get_licznik())
print(liczba.get_mianownik())
print(str(liczba))
print(float(liczba))
print(liczba + liczba2)
print(liczba - liczba2)



