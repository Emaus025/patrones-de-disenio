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

# Singleton pattern for creating a unique Piano Amp
class PianoAmp:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Piano Amp...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def play_sound(self):
        return "🎹 Amplified sound: Plink plonk!"

# Singleton pattern for creating a unique Drum Amp
class DrumAmp:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Drum Amp...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def play_sound(self):
        return "🥁 Amplified sound: Boom boom boom!"

# Singleton pattern for creating a unique Saxophone Amp
class SaxophoneAmp:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Saxophone Amp...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def play_sound(self):
        return "🎷 Amplified sound: Woohooo!"

# Client code to use the Singleton
if __name__ == "__main__":
    amp1 = GuitarAmp()
    amp2 = PianoAmp()
    amp3 = DrumAmp()
    amp4 = SaxophoneAmp()
    
    print(f"Are both Guitar amps the same instance? {'Yes' if amp1 is GuitarAmp() else 'No'}")
    print(f"Sound from Guitar Amp: {amp1.play_sound()}")
    
    print(f"Are both Piano amps the same instance? {'Yes' if amp2 is PianoAmp() else 'No'}")
    print(f"Sound from Piano Amp: {amp2.play_sound()}")
    
    print(f"Are both Drum amps the same instance? {'Yes' if amp3 is DrumAmp() else 'No'}")
    print(f"Sound from Drum Amp: {amp3.play_sound()}")
    
    print(f"Are both Saxophone amps the same instance? {'Yes' if amp4 is SaxophoneAmp() else 'No'}")
    print(f"Sound from Saxophone Amp: {amp4.play_sound()}")
