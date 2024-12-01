import copy

# Base class for musical instruments
class Instrument:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def play(self):
        return self.sound

    def clone(self):
        return copy.deepcopy(self)

# Example instruments
class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar", "🎸 Strum strum!")

class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano", "🎹 Plink plonk!")

class Trombone(Instrument):
    def __init__(self):
        super().__init__("Trombone", "🎺 Wahhh wahhh!")

class Flute(Instrument):
    def __init__(self):
        super().__init__("Flute", "🎶 Fweee fwee!")

class Oboe(Instrument):
    def __init__(self):
        super().__init__("Oboe", "🎷 Woo waahh!")

class Saxophone(Instrument):
    def __init__(self):
        super().__init__("Saxophone", "🎷 Swooosh swooosh!")

# Client code to use the Prototype
if __name__ == "__main__":
    guitar1 = Guitar()
    piano1 = Piano()
    trombone1 = Trombone()
    flute1 = Flute()
    oboe1 = Oboe()
    saxophone1 = Saxophone()

    guitar2 = guitar1.clone()
    piano2 = piano1.clone()
    trombone2 = trombone1.clone()
    flute2 = flute1.clone()
    oboe2 = oboe1.clone()
    saxophone2 = saxophone1.clone()

    print(f"Cloned Guitar: {guitar2.name} - {guitar2.play()}")
    print(f"Cloned Piano: {piano2.name} - {piano2.play()}")
    print(f"Cloned Trombone: {trombone2.name} - {trombone2.play()}")
    print(f"Cloned Flute: {flute2.name} - {flute2.play()}")
    print(f"Cloned Oboe: {oboe2.name} - {oboe2.play()}")
    print(f"Cloned Saxophone: {saxophone2.name} - {saxophone2.play()}")
