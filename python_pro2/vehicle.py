class Vehicle:
    def __init__(self, reg=None, model=0, prod_year=2022):
        self.__reg = reg
        self.__model = model if model >= 0 else 0
        self.__prod_year = prod_year if prod_year >= 1900 and prod_year <= 2022 else 2022

    @property
    def reg(self):
        return self.__reg

    @reg.setter
    def reg(self, reg):
        self.__reg = reg

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model < 0:
            print("Nieprawidłowy model")
        else:
            self.__model = model

    @property
    def prod_year(self):
        return self.__prod_year

    @prod_year.setter
    def prod_year(self, prod_year):
        if prod_year < 1900 or prod_year > 2022:
            print("Nieprawidłowy rok produkcji")
        else:
            self.__prod_year = prod_year

    def brake(self):
        return "Zatrzymuję się"

    def drive(self):
        return f"Jadę świetnym pojazdem z roku {self.__prod_year}!"

    def __str__(self):
        reg_str = f"Rejestracja: {self.__reg}." if self.__reg else ""
        return f"Pojazd wyprodukowany w roku: {self.__prod_year}.\nModel: {self.__model}.\n{reg_str}"

    def __eq__(self, other):
        return self.__model == other.model and self.__prod_year == other.prod_year

    def __ne__(self, other):
        return not self.__eq__(other)
