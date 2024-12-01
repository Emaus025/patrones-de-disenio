# Base class for instruments
class Instrument:
    def play(self):
        pass

# Concrete class for a basic Guitar
class Guitar(Instrument):
    def play(self):
        return "🎸 Strum strum (Guitar sound)"

# Concrete class for a Piano
class Piano(Instrument):
    def play(self):
        return "🎹 Plink plonk (Piano sound)"

# Concrete class for Drums
class Drums(Instrument):
    def play(self):
        return "🥁 Boom boom (Drums sound)"

# Decorator class to add effects
class InstrumentDecorator(Instrument):
    def __init__(self, instrument):
        self._instrument = instrument
    
    def play(self):
        return self._instrument.play()

class ReverbDecorator(InstrumentDecorator):
    def play(self):
        return f"{self._instrument.play()}...with Reverb!"

class DistortionDecorator(InstrumentDecorator):
    def play(self):
        return f"{self._instrument.play()}...with Distortion!"

class EchoDecorator(InstrumentDecorator):
    def play(self):
        return f"{self._instrument.play()}...with Echo!"

# Client code to use the Decorators
if __name__ == "__main__":
    guitar = Guitar()
    piano = Piano()
    drums = Drums()

    guitar_with_reverb = ReverbDecorator(guitar)
    guitar_with_distortion = DistortionDecorator(guitar)
    piano_with_echo = EchoDecorator(piano)

    print(guitar.play())  # Basic guitar sound
    print(guitar_with_reverb.play())  # Guitar with reverb
    print(guitar_with_distortion.play())  # Guitar with distortion
    print(piano_with_echo.play())  # Piano with echo
    print(drums.play())  # Basic drums sound
