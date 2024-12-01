# Template Method pattern - musical performance with predefined steps

# Abstract class for music performance
class MusicPerformance:
    def perform(self):
        self.prepare_instruments()
        self.warm_up()
        self.play_music()
        self.finish_performance()

    def prepare_instruments(self):
        print("Preparing instruments... 🎸 🎹 🥁")

    def warm_up(self):
        print("Warming up... 🎶")

    # Abstract method, to be defined by concrete classes
    def play_music(self):
        pass

    def finish_performance(self):
        print("Thank you for listening! 👏 👏 👏")

# Concrete class for guitar performance
class GuitarPerformance(MusicPerformance):
    def play_music(self):
        print("Playing guitar... 🎸 Strum strum!")

# Concrete class for piano performance
class PianoPerformance(MusicPerformance):
    def play_music(self):
        print("Playing piano... 🎹 Plink plonk!")

# Client code to use the Template Method pattern
if __name__ == "__main__":
    guitar_performance = GuitarPerformance()
    piano_performance = PianoPerformance()

    print("Guitar performance:")
    guitar_performance.perform()

    print("\nPiano performance:")
    piano_performance.perform()
