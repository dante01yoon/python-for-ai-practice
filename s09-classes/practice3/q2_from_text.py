class Temperature:
    def __init__(self, degrees, unit):
        self.degrees = degrees
        self.unit = unit

    @classmethod
    def from_text(cls, text):
        number, unit = text.split()
        return cls(float(number), unit)


reading = Temperature.from_text("72 F")
print(reading.degrees, reading.unit)
