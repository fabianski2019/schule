while True:
    zahl = int(input("Geben Sie eine Zahl ein (oder '0' zum Beenden): "))
    if zahl == 0:
        print("Programm wird beendet.")
        break

    if zahl <= 1:
        print(f"{zahl} ist keine Primzahl. Die 1 ist per Definition ausgeschlossen.\n")
    elif zahl == 2:
        print(f"{zahl} ist eine Primzahl.")
    else:
        ist_primzahl = True
        teiler = []

        for i in range(2, zahl):
            if zahl % i == 0:
                teiler.append(i)
                ist_primzahl = False

        if ist_primzahl:
            print(f"{zahl} ist eine Primzahl.\n")
        else:
            print(f"{zahl} ist keine Primzahl, da sie durch {teiler} teilbar ist.\n")

