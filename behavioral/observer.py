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

# Client code to use the Observer pattern
if __name__ == "__main__":
    guitar = Guitar()
    piano = Piano()

    musician1 = Musician("Alice")
    musician2 = Musician("Bob")

    guitar.add_observer(musician1)
    piano.add_observer(musician2)

    print("Guitar playing:")
    guitar.notify()

    print("\nPiano playing:")
    piano.notify()
