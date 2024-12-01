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

# Client code to use the Prototype
if __name__ == "__main__":
    guitar1 = Guitar()
    piano1 = Piano()

    guitar2 = guitar1.clone()
    piano2 = piano1.clone()

    print(f"Cloned Guitar: {guitar2.name} - {guitar2.play()}")
    print(f"Cloned Piano: {piano2.name} - {piano2.play()}")