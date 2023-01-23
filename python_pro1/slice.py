class Slice(Pizza):
    def __init__(self, diameter, toppings, how_many_slices):
        super().__init__(diameter, toppings)
        if how_many_slices < 4 or how_many_slices > 12 or how_many_slices % 2 != 0:
            print("Błędna ilość kawałków")
            exit(-10)
        self.__how_many_slices = how_many_slices

    @property
    def how_many_slices(self):
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, how_many_slices):
        if how_many_slices < 4 or how_many_slices > 12 or how_many_slices % 2 != 0:
            print("Błędna ilość kawałków")
            exit(-10)
        self.__how_many_slices = how_many_slices

    def part_price(self, ordered_slices):
        return self.price * ordered_slices / self.how_many_slices

    def __str__(self):
        toppings_str = ', '.join([f"{topping} x {quantity}" for topping, quantity in self.__toppings.items()])
        return f"Pizza:\nśrednica: {self.__diameter}\ndodatki: {toppings_str}\ncena: {self.__price}\nkawałki {self.__how_many_slices}\ncena za kawałek {self.price / self.how_many_slices}"
