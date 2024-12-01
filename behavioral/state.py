# State pattern - changing states of a music player

# State class (interface)
class PlayerState:
    def play(self):
        pass

# Concrete state class for stopped state
class StoppedState(PlayerState):
    def play(self):
        return "⏸️ The player is stopped. Press play to start."

# Concrete state class for playing state
class PlayingState(PlayerState):
    def play(self):
        return "▶️ The player is playing music now!"

# Concrete state class for paused state
class PausedState(PlayerState):
    def play(self):
        return "⏸️ The player is paused. Press play to resume."

# Concrete state class for muted state
class MutedState(PlayerState):
    def play(self):
        return "🔇 The player is muted, but still playing music!"

# Context class (Music Player)
class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()

    def set_state(self, state):
        self.state = state

    def press_play(self):
        print(self.state.play())

# Client code to use the State pattern
if __name__ == "__main__":
    player = MusicPlayer()

    print("Initial state:")
    player.press_play()  # Stopped state

    print("\nChanging state to playing:")
    player.set_state(PlayingState())
    player.press_play()  # Playing state

    print("\nChanging state to paused:")
    player.set_state(PausedState())
    player.press_play()  # Paused state

    print("\nChanging state to muted:")
    player.set_state(MutedState())
    player.press_play()  # Muted state

    print("\nChanging state back to playing:")
    player.set_state(PlayingState())
    player.press_play()  # Playing state again
