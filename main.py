from classes.szemelyauto import Szemelyauto
from classes.autokolcsonzo import Autokolcsonzo
from classes.berles import Berles
from classes.teherauto import Teherauto


def inicializalas():
    kolcsonzo = Autokolcsonzo("TopCar Kft.")
    auto1 = Szemelyauto("KIK-129", "Kia Ceed", 15000, 5)
    auto2 = Teherauto("DOG-972", "VW Transporter", 20000, 2540)
    auto3 = Szemelyauto("IRM-007", "Opel Astra", 10000, 5)
    kolcsonzo.hozzaad_auto(auto1)
    kolcsonzo.hozzaad_auto(auto2)
    kolcsonzo.hozzaad_auto(auto3)
    kolcsonzo.berles_hozzaad(Berles(auto1, "2024-11-26"))
    kolcsonzo.berles_hozzaad(Berles(auto2, "2024-11-27"))
    return kolcsonzo

def menu():
    kolcsonzo = inicializalas()
    while True:
        print("\n--- Autókölcsönző Rendszer ---")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("0. Kilépés")
        valasztas = input("Választás: ")

        if valasztas == "1":
            print("\nElérhető autók:")
            for auto in kolcsonzo.autok_listazasa():
                print(auto)

        elif valasztas == "2":
            rendszam = input("Adja meg az autó rendszámát: ")
            nap = input("Adja meg a bérlés napját (YYYY-MM-DD): ")
            for auto in kolcsonzo.autok:
                if auto.rendszam == rendszam:
                    kolcsonzo.berles_hozzaad(Berles(auto, nap))
                    print(f"Bérlés sikeres! Ár: {auto.berleti_dij} Ft")
                    break
            else:
                print("Nincs ilyen rendszámú autó.")
        elif valasztas == "3":
            rendszam = input("Adja meg a lemondandó bérlés rendszámát: ")
            if kolcsonzo.torol_berlest(rendszam):
                print("Bérlés sikeresen törölve.")
            else:
                print("Nincs ilyen bérlés.")
        elif valasztas == "4":
            print("\nAktuális bérlések:")
            for berles in kolcsonzo.berlesek_listazasa():
                print(berles)
        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    menu()