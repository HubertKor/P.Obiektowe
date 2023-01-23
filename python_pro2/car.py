class Car(Vehicle):
    def __init__(self, reg=None, model=0, prod_year=2022, price=0, colour=None, extra_seats=0):
        super().__init__(reg, model, prod_year)
        self.__price = price if price >= 0 else 0
        self.__colour = colour
        self.__extra_seats = extra_seats if extra_seats >= 0 else 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            print("Nieprawidłowa cena")
        else:
            self.__price = price

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def extra_seats(self):
        return self.__extra_seats

    @extra_seats.setter
    def extra_seats(self, extra_seats):
        if extra_seats < 0:
            print("Nieprawidłowa liczba siedzeń")
        else:
            self.__extra_seats = extra_seats
    
    def drive(self):
        return f"Jadę świetnym pojazdem z roku {self.prod_year}! Ma kolor {self.colour}."

    def __eq__(self, other):
        return self.model == other.model and self.price == other.price

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return (f"Pojazd wyprodukowany w roku: {self.prod_year}.\n"
                f"Model: {self.model}.\n"
                f"Rejestracja: {self.reg}.\n"
                f"Cena: {self.price}.\n"
                f"Kolor: {self.colour}.\n"
                f"Dodatkowe siedzenia: {self.extra_seats}.")

