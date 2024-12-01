# Class that plays music
class MusicPlayer:
    def play_music(self, instrument):
        print(instrument.play())

# Old instrument interface (assumed incompatible)
class OldGuitar:
    def strum(self):
        return "🎸 Strum strum (Old Guitar sound)"

# New instruments
class Piano:
    def play(self):
        return "🎹 Plink plonk (Piano sound)"

class Drums:
    def play(self):
        return "🥁 Boom boom (Drums sound)"

# Adapter to make OldGuitar compatible with MusicPlayer
class GuitarAdapter:
    def __init__(self, old_guitar):
        self.old_guitar = old_guitar

    def play(self):
        return self.old_guitar.strum()

# Adapter to make Piano compatible with MusicPlayer
class PianoAdapter:
    def __init__(self, piano):
        self.piano = piano

    def play(self):
        return self.piano.play()

# Adapter to make Drums compatible with MusicPlayer
class DrumsAdapter:
    def __init__(self, drums):
        self.drums = drums

    def play(self):
        return self.drums.play()

# Client code to use the Adapter
if __name__ == "__main__":
    old_guitar = OldGuitar()
    guitar_adapter = GuitarAdapter(old_guitar)
    
    piano = Piano()
    piano_adapter = PianoAdapter(piano)
    
    drums = Drums()
    drums_adapter = DrumsAdapter(drums)

    music_player = MusicPlayer()
    music_player.play_music(guitar_adapter)
    music_player.play_music(piano_adapter)
    music_player.play_music(drums_adapter)
