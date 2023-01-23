import math
class Pizza:
    def __init__(self, diameter, toppings):
        self.__diameter = diameter
        self.__toppings = toppings
        if diameter < 20:
            print("Błędny promień")
            exit(-10)
        if not all(0 <= value <= 3 for value in toppings.values()):
            print("Błędny słownik dodatków")
            exit(-20)
        self.__price = self.area() * 0.05 + sum(toppings.values()) * 2

    @staticmethod
    def area():
        return math.pi * (self.__diameter / 2) ** 2

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 20:
            print("Błędna średnica")
            exit(-10)
        self.__diameter = diameter
        self.__price = self.area() * 0.05 + sum(self.__toppings.values()) * 2

    def add_topping(self, topping):
        if topping in self.__toppings:
            self.__toppings[topping] += 1
        else:
            self.__toppings[topping] = 1
        self.__price += 2

    def __str__(self):
        toppings_str = ', '.join([f"{topping} x {quantity}" for topping, quantity in self.__toppings.items()])
        return f"Pizza:\nśrednica: {self.__diameter}\ndodatki: {toppings_str}\ncena: {self.__price}"

    def __add__(self, other):
        diameter = max(self.diameter, other.diameter)
        toppings = {**self.__toppings, **other.__toppings}
        for topping in toppings:
            toppings[topping] = max(self.__toppings.get(topping, 0), other.__toppings.get(topping, 0))
        return Pizza(diameter, toppings)
