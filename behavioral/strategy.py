# Strategy pattern - different music styles to play

# Strategy interface
class PlayStyle:
    def play(self):
        pass

# Concrete strategies
class AcousticStyle(PlayStyle):
    def play(self):
        return "🎸 Strum strum (Acoustic style)"

class ElectricStyle(PlayStyle):
    def play(self):
        return "🎸 Bzzzzzz (Electric style)"

class ClassicalStyle(PlayStyle):
    def play(self):
        return "🎹 Plink plonk (Classical piano style)"

# Context class (Musician with strategy)
class Musician:
    def __init__(self, name, play_style):
        self.name = name
        self.play_style = play_style

    def set_play_style(self, play_style):
        self.play_style = play_style

    def perform(self):
        print(f"{self.name} is playing: {self.play_style.play()}")

# Client code to use the Strategy pattern
if __name__ == "__main__":
    alice = Musician("Alice", AcousticStyle())
    bob = Musician("Bob", ElectricStyle())

    alice.perform()  # Alice playing in acoustic style
    bob.perform()    # Bob playing in electric style

    print("\nChanging Alice's play style to classical:")
    alice.set_play_style(ClassicalStyle())
    alice.perform()  # Alice playing in classical style
