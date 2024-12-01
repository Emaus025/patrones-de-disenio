# Class that plays music
class MusicPlayer:
    def play_music(self, instrument):
        print(instrument.play())

# Old instrument interface (assumed incompatible)
class OldGuitar:
    def strum(self):
        return "🎸 Strum strum (Old Guitar sound)"

# Adapter to make OldGuitar compatible with MusicPlayer
class GuitarAdapter:
    def __init__(self, old_guitar):
        self.old_guitar = old_guitar

    def play(self):
        return self.old_guitar.strum()

# Client code to use the Adapter
if __name__ == "__main__":
    old_guitar = OldGuitar()
    guitar_adapter = GuitarAdapter(old_guitar)
    music_player = MusicPlayer()
    music_player.play_music(guitar_adapter)
