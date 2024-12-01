from abc import ABC, abstractmethod

# Abstract class for instruments
class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

# Abstract class for cases (to store instruments)
class InstrumentCase(ABC):
    @abstractmethod
    def material(self):
        pass

# Concrete classes for Guitar
class Guitar(Instrument):
    def play(self):
        return "🎸 Strum strum (Guitar sound)"

class GuitarCase(InstrumentCase):
    def material(self):
        return "Hardwood with velvet lining 🎻"

# Concrete classes for Piano
class Piano(Instrument):
    def play(self):
        return "🎹 Plink plonk (Piano sound)"

class PianoCase(InstrumentCase):
    def material(self):
        return "Sturdy metal case 🏋️"

# Concrete classes for Drums
class Drums(Instrument):
    def play(self):
        return "🥁 Boom boom (Drums sound)"

class DrumCase(InstrumentCase):
    def material(self):
        return "Reinforced plastic 🛢️"

# Abstract Factory for creating instruments and cases
class InstrumentFactory(ABC):
    @abstractmethod
    def create_instrument(self):
        pass

    @abstractmethod
    def create_case(self):
        pass

# Concrete factory for Guitars
class GuitarFactory(InstrumentFactory):
    def create_instrument(self):
        return Guitar()

    def create_case(self):
        return GuitarCase()

# Concrete factory for Pianos
class PianoFactory(InstrumentFactory):
    def create_instrument(self):
        return Piano()

    def create_case(self):
        return PianoCase()

# Concrete factory for Drums
class DrumFactory(InstrumentFactory):
    def create_instrument(self):
        return Drums()

    def create_case(self):
        return DrumCase()

# Client code to use the factories
if __name__ == "__main__":
    print("Choose an instrument: guitar, piano, drums")
    instrument_type = input("Your choice: ").lower()

    # Map input to the correct factory
    factories = {
        "guitar": GuitarFactory(),
        "piano": PianoFactory(),
        "drums": DrumFactory()
    }

    factory = factories.get(instrument_type)
    
    if factory:
        instrument = factory.create_instrument()
        case = factory.create_case()
        print(f"You chose a {instrument_type.capitalize()}.")
        print(f"It sounds like: {instrument.play()}")
        print(f"Its case is made of: {case.material()}")
    else:
        print(f"Sorry, we don't have a factory for '{instrument_type}'.")