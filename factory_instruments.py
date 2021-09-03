from musical_instruments import Guitar, Piano


class FactoryInstrument:
    @staticmethod
    def get_instrument(type, brand):
        if type == "guitar":
            return Guitar(brand)
        elif type == "piano":
            return Piano(brand)
        else:
            return "Invalid type"
