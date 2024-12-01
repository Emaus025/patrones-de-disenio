# Template Method pattern - musical performance with predefined steps

# Abstract class for music performance
class MusicPerformance:
    def perform(self):
        self.prepare_instruments()
        self.warm_up()
        self.play_music()
        self.finish_performance()

    def prepare_instruments(self):
        print("Preparing instruments... 🎸 🎹 🥁 🎻 🎺 🎷")

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

# Concrete class for drums performance
class DrumsPerformance(MusicPerformance):
    def play_music(self):
        print("Playing drums... 🥁 Boom boom!")

# Concrete class for violin performance
class ViolinPerformance(MusicPerformance):
    def play_music(self):
        print("Playing violin... 🎻 Vroom vroom!")

# Concrete class for flute performance
class FlutePerformance(MusicPerformance):
    def play_music(self):
        print("Playing flute... 🎶 Fwoooosh!")

# Client code to use the Template Method pattern
if __name__ == "__main__":
    guitar_performance = GuitarPerformance()
    piano_performance = PianoPerformance()
    drums_performance = DrumsPerformance()
    violin_performance = ViolinPerformance()
    flute_performance = FlutePerformance()

    print("Guitar performance:")
    guitar_performance.perform()

    print("\nPiano performance:")
    piano_performance.perform()

    print("\nDrums performance:")
    drums_performance.perform()

    print("\nViolin performance:")
    violin_performance.perform()

    print("\nFlute performance:")
    flute_performance.perform()
