from abc import ABC, abstractmethod

# Abstract class for general interface
class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

# Specific classes that implements each instrument
class Guitar(Instrument):
    def play(self):
        return "🎸 Strum strum (Guitar sound)"

class Piano(Instrument):
    def play(self):
        return "🎹 Plink plonk (Piano sound)"

class Drums(Instrument):
    def play(self):
        return "🥁 Boom boom (Drums sound)"

# Fabric to create the instruments
class InstrumentFactory:
    @staticmethod
    def create_instrument(instrument_type):
        if instrument_type == "guitar":
            return Guitar()
        elif instrument_type == "piano":
            return Piano()
        elif instrument_type == "drums":
            return Drums()
        else:
            raise ValueError(f"Instrument type '{instrument_type}' not recognized")

# Using the factory pattern
if __name__ == "__main__":
    instrument_type = input("Enter instrument type (guitar, piano, drums): ").lower()
    try:
        instrument = InstrumentFactory.create_instrument(instrument_type)
        print(f"You chose a {instrument_type.capitalize()} and it sounds like: {instrument.play()}")
    except ValueError as e:
        print(e)
