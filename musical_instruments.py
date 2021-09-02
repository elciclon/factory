class Instrument:
    """
    Class to create musical instruments
    """

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __str__(self):
        return f"{self.brand} - {self.price}$"

    def play(self):
        print("playing")

    def keep_in_case(self):
        print("keep in case")

    def tune(self):
        print("tuned")


class Guitar(Instrument):
    """
    Class to create guitar
    """

    def __init__(self, brand):
        super().__init__(200, brand)
        self.state = "new"
        print(f"This is a {self.state} guitar - {self.price}$")


class Piano(Instrument):
    """
    Class to create piano
    """

    def __init__(self, brand):
        super().__init__(1500, brand)
        self.state = "used"
        print(f"This is a {self.state} {brand} piano - {self.price}$")

    def repair_action(self):
        print("Piano refurbished")
