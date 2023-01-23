from rownoleglobok import Rownoleglobok
from typing import List

class Kwadrat(Rownoleglobok):
    __kolor: str

    def __init__(self, bok: int, kolor: str):
        if kolor == "" or (bok > 100 or bok <= 0):
            print("zle parametry")
            exit(-2)
        super().__init__(bok, bok, 90)
        self.__kolor = kolor

    @property
    def kolor(self):
        return self.__kolor

    @kolor.setter
    def kolor(self, value:str):
        if self.kolor == "":
            print("zle parametry")
            exit(-2)
        self.kolor = value
    
    @staticmethod
    def generuj_kwadrat(lista):
        if lista is []:
            return []
        temp_list = []
        i = 10
        for kolor in lista:
            temp_list.append(Kwadrat(i, kolor))
            i+=1
        return temp_list

    def __str__(self) -> str:
        return f'dlugosc boku= {self.bok1}, kolor = {self.__kolor}, obwod= {self.bok1*4}'