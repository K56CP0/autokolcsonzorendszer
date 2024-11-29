class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        return [str(auto) for auto in self.autok]

    def berles_hozzaad(self, berles):
        self.berlesek.append(berles)

    def berlesek_listazasa(self):
        return [str(berles) for berles in self.berlesek]

    def torol_berlest(self, rendszam):
        for berles in self.berlesek:
            if berles in self.berlesek==rendszam:
                self.berlesek.remove(berles)
                return True
        return False