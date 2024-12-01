# Builder pattern - creating a complex musical instrument (Guitar)

# Product class (Guitar)
class Guitar:
    def __init__(self, body, neck, strings, pickups):
        self.body = body
        self.neck = neck
        self.strings = strings
        self.pickups = pickups

    def __str__(self):
        return f"Guitar with a {self.body} body, {self.neck} neck, {self.strings} strings, and {self.pickups} pickups."

# Abstract Builder class
class GuitarBuilder:
    def build_body(self):
        pass

    def build_neck(self):
        pass

    def build_strings(self):
        pass

    def build_pickups(self):
        pass

    def get_result(self):
        return self.guitar

# Concrete Builder class for Electric Guitar
class ElectricGuitarBuilder(GuitarBuilder):
    def __init__(self):
        self.guitar = Guitar("", "", "", "")

    def build_body(self):
        self.guitar.body = "Solid Body"
    
    def build_neck(self):
        self.guitar.neck = "Maple Neck"
    
    def build_strings(self):
        self.guitar.strings = "6 Strings"
    
    def build_pickups(self):
        self.guitar.pickups = "Humbucker Pickups"

# Concrete Builder class for Acoustic Guitar
class AcousticGuitarBuilder(GuitarBuilder):
    def __init__(self):
        self.guitar = Guitar("", "", "", "")

    def build_body(self):
        self.guitar.body = "Hollow Body"
    
    def build_neck(self):
        self.guitar.neck = "Rosewood Neck"
    
    def build_strings(self):
        self.guitar.strings = "6 Nylon Strings"
    
    def build_pickups(self):
        self.guitar.pickups = "None (Acoustic)"

# Concrete Builder class for Bass Guitar
class BassGuitarBuilder(GuitarBuilder):
    def __init__(self):
        self.guitar = Guitar("", "", "", "")

    def build_body(self):
        self.guitar.body = "Larger Solid Body"
    
    def build_neck(self):
        self.guitar.neck = "Rosewood Neck"
    
    def build_strings(self):
        self.guitar.strings = "4 Strings"
    
    def build_pickups(self):
        self.guitar.pickups = "P Bass Pickups"

# Director class (director of guitar construction)
class GuitarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_guitar(self):
        self.builder.build_body()
        self.builder.build_neck()
        self.builder.build_strings()
        self.builder.build_pickups()

# Client code to use the Builder pattern
if __name__ == "__main__":
    # Constructing an Electric Guitar
    electric_builder = ElectricGuitarBuilder()
    electric_director = GuitarDirector(electric_builder)
    electric_director.construct_guitar()
    electric_guitar = electric_builder.get_result()
    print(f"Built electric guitar: {electric_guitar}")

    # Constructing an Acoustic Guitar
    acoustic_builder = AcousticGuitarBuilder()
    acoustic_director = GuitarDirector(acoustic_builder)
    acoustic_director.construct_guitar()
    acoustic_guitar = acoustic_builder.get_result()
    print(f"Built acoustic guitar: {acoustic_guitar}")

    # Constructing a Bass Guitar
    bass_builder = BassGuitarBuilder()
    bass_director = GuitarDirector(bass_builder)
    bass_director.construct_guitar()
    bass_guitar = bass_builder.get_result()
    print(f"Built bass guitar: {bass_guitar}")
