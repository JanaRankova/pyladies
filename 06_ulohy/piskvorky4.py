from random import randrange

hracie_pole = list('------xx------o-----')
cislo_policka = int
symbol = ''

def tah_pocitaca(hracie_pole):
    """Generuje nahodne cislo a tah pocitaca na prazdne pole. Vracia hracie pole uz s tahom pc."""
    cislo_policka = randrange(0, 20)
    if hracie_pole[cislo_policka] == '-':
            hracie_pole[cislo_policka] = 'o'            #pocitac hra za 'o'
            hracie_pole = ''.join(hracie_pole)
    else:
        tah_pocitaca(hracie_pole)
        hracie_pole = ''.join(hracie_pole)

    return hracie_pole

print (tah_pocitaca(hracie_pole))