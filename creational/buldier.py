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

# Concrete Builder class
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
    builder = ElectricGuitarBuilder()
    director = GuitarDirector(builder)

    director.construct_guitar()
    guitar = builder.get_result()

    print(f"Built guitar: {guitar}")
