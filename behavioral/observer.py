# Observer pattern - notifying when an instrument plays

# Observer class
class Observer:
    def update(self, instrument):
        pass

# Concrete observer class for musicians
class Musician(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, instrument):
        print(f"{self.name} heard the sound: {instrument.play()}")

# Subject class (Instrument that notifies observers)
class Instrument:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

# Concrete classes for instruments
class Guitar(Instrument):
    def play(self):
        return "🎸 Strum strum (Guitar sound)"

class Piano(Instrument):
    def play(self):
        return "🎹 Plink plonk (Piano sound)"

class Melodica(Instrument):
    def play(self):
        return "🎶 Whoosh whoosh (Melodica sound)"

class Trombone(Instrument):
    def play(self):
        return "🎺 Wah wah (Trombone sound)"

class Flute(Instrument):
    def play(self):
        return "🎵 Fwee fwee (Flute sound)"

class Oboe(Instrument):
    def play(self):
        return "🎶 Oooo oooo (Oboe sound)"

class Saxophone(Instrument):
    def play(self):
        return "🎷 Wooooo wooo (Saxophone sound)"

# Client code to use the Observer pattern
if __name__ == "__main__":
    guitar = Guitar()
    piano = Piano()
    melodica = Melodica()
    trombone = Trombone()
    flute = Flute()
    oboe = Oboe()
    saxophone = Saxophone()

    musician1 = Musician("Marisco")
    musician2 = Musician("León")
    musician3 = Musician("Adultante")

    # Observers listening to different instruments
    guitar.add_observer(musician1)
    piano.add_observer(musician2)
    melodica.add_observer(musician3)
    trombone.add_observer(musician1)
    flute.add_observer(musician2)
    oboe.add_observer(musician3)
    saxophone.add_observer(musician1)

    print("Guitar playing:")
    guitar.notify()

    print("\nPiano playing:")
    piano.notify()

    print("\nMelodica playing:")
    melodica.notify()

    print("\nTrombone playing:")
    trombone.notify()

    print("\nFlute playing:")
    flute.notify()

    print("\nOboe playing:")
    oboe.notify()

    print("\nSaxophone playing:")
    saxophone.notify()
