import math

class Rownoleglobok:
    bok1: int
    bok2: int
    kat: int

    def __init__(self,bok1:int,bok2:int,kat:int):
        if bok1 > 100 or bok1 <= 0:
            print("zle parametry")
            exit(-2)
        if bok2 > 100 or bok2 <= 0:
            print("zle parametry")
            exit(-2)
        if kat > 180 or kat <= 0:
            print("zle parametry")
            exit(-2)
        self.bok1 = bok1
        self.bok2 = bok2
        self.kat = kat

    def pobierz_pole(self) -> float:
        return float(math.sin(self.kat)*self.bok1*self.bok2)

    def pobierz_obwod(self) -> float:
        return float(2*self.bok1 + 2*self.bok2)

    def duplikuj_ze_skala(self, skala: int):
        if skala > 10 or skala < 1:
            print("zle parametry")
            exit(-2)
        if self.bok1 * skala > 100 or self.bok1 * skala <= 0:
            print("zle parametry")
            exit(-2)
        if self.bok2 * skala >100 or self.bok2 * skala <= 0:
            print("zle parametry")
            exit(-2)
        return Rownoleglobok(self.bok1*skala,self.bok2*skala,self.kat)

    def __repr__(self) -> str:
        return f'{self.bok1} {self.bok2} {self.kat}'

    def __add__(self,other):
        return Rownoleglobok(self.bok1 + other.bok1, self.bok2 + other.bok2, min(self.kat , other.kat))