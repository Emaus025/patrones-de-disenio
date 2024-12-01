# Strategy pattern - different music styles to play

# Strategy interface
class PlayStyle:
    def play(self):
        pass

# Concrete strategies for various music styles
class AcousticStyle(PlayStyle):
    def play(self):
        return "🎸 Strum strum (Acoustic style)"

class ElectricStyle(PlayStyle):
    def play(self):
        return "🎸 Bzzzzzz (Electric style)"

class ClassicalStyle(PlayStyle):
    def play(self):
        return "🎹 Plink plonk (Classical piano style)"

class JazzStyle(PlayStyle):
    def play(self):
        return "🎷 Doo wop (Jazz style)"

class BluesStyle(PlayStyle):
    def play(self):
        return "🎸 Bbbbb blues (Blues guitar style)"

class FunkStyle(PlayStyle):
    def play(self):
        return "🎸 Funky groove (Funk style)"

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
    Marisco = Musician("Marisco", AcousticStyle())
    León = Musician("León", ElectricStyle())
    Adultante = Musician("Adultante", JazzStyle())

    Marisco.perform()  # Marisco playing in acoustic style
    León.perform()    # León playing in electric style
    Adultante.perform()  # Adultante playing in jazz style

    print("\nChanging Marisco's play style to classical:")
    Marisco.set_play_style(ClassicalStyle())
    Marisco.perform()  # Marisco playing in classical style

    print("\nChanging León's play style to blues:")
    León.set_play_style(BluesStyle())
    León.perform()  # León playing in blues style

    print("\nChanging Adultante's play style to funk:")
    Adultante.set_play_style(FunkStyle())
    Adultante.perform()  # Adultante playing in funk style
