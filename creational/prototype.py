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

# Concrete class for Guitar
class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar", "🎸 Strum strum!")

# Concrete class for Piano
class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano", "🎹 Plink plonk!")

# Concrete class for Drums
class Drums(Instrument):
    def __init__(self):
        super().__init__("Drums", "🥁 Boom boom!")

# Concrete class for Flute
class Flute(Instrument):
    def __init__(self):
        super().__init__("Flute", "🎶 Fweet fweet!")

# Concrete class for Trumpet
class Trumpet(Instrument):
    def __init__(self):
        super().__init__("Trumpet", "🎺 Blat blat!")

# Client code to use the Prototype pattern
if __name__ == "__main__":
    guitar1 = Guitar()
    piano1 = Piano()
    drums1 = Drums()
    flute1 = Flute()
    trumpet1 = Trumpet()

    # Cloning the objects
    guitar2 = guitar1.clone()
    piano2 = piano1.clone()
    drums2 = drums1.clone()
    flute2 = flute1.clone()
    trumpet2 = trumpet1.clone()

    # Displaying cloned objects and their sounds
    print(f"Cloned Guitar: {guitar2.name} - {guitar2.play()}")
    print(f"Cloned Piano: {piano2.name} - {piano2.play()}")
    print(f"Cloned Drums: {drums2.name} - {drums2.play()}")
    print(f"Cloned Flute: {flute2.name} - {flute2.play()}")
    print(f"Cloned Trumpet: {trumpet2.name} - {trumpet2.play()}")
