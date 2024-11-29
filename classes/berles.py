class Berles:

    def __init__(self, auto, nap):
        self.auto = auto
        self.nap = nap

    def __str__(self):
        return f'{self.auto.rendszam} - {self.auto.tipus} (Bérlés időpontja: {self.nap})'