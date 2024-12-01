# Singleton pattern for creating a unique Guitar Amp
class GuitarAmp:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Guitar Amp...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def play_sound(self):
        return "🎸 Amplified sound: Rrrrhhhhhhh!"

# Client code to use the Singleton
if __name__ == "__main__":
    amp1 = GuitarAmp()
    amp2 = GuitarAmp()
    
    print(f"Are both amps the same instance? {'Yes' if amp1 is amp2 else 'No'}")
    print(f"Sound from amp1: {amp1.play_sound()}")
    print(f"Sound from amp2: {amp2.play_sound()}")
