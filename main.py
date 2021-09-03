from factory_instruments import FactoryInstrument


def main():
    guitar = FactoryInstrument.get_instrument("guitar", "Gibson L-5 CES")
    piano = FactoryInstrument.get_instrument("piano", "Yamaha DX-7")
    guitar.play()
    piano.repair_action()


main()
