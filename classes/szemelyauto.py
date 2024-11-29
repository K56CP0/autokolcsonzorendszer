from classes.auto import  Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasok_szama = utasok_szama

    def __str__(self):
        return f'{self.rendszam} - {self.tipus} (Személyautó, Utasok: {self.utasok_szama})'