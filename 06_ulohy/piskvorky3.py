hracie_pole = list('------xx------o-----')
cislo_policka = int
symbol = ''

def tah_hraca(hracie_pole):
    """Spyta sa hraca na poziciu, na ktoru chce  umiestnit symbol (hrac hra za 'x'). Zamietne nespravne zadane znaky.
    Prepise hracie pole a vrati ho."""
    cislo_policka = int(input('Zadajte poziciu, na ktoru chcete umiestnit symbol. Platne su cisla od 1-20. '))
    cislo_policka -= 1 #prepocet z cisla hraca na index
    if cislo_policka >= 0 and cislo_policka <= 19:
        if hracie_pole[cislo_policka] == '-':
            hracie_pole[cislo_policka] = 'x'
            hracie_pole = ''.join(hracie_pole)
            return hracie_pole
        else:
            print('Vami zadana pozicia je obsadena alebo neexistuje. Skuste vybrat inu poziciu.')
            tah_hraca(hracie_pole)
            hracie_pole = ''.join(hracie_pole)
    else:
        print('Vami zadana pozicia je obsadena alebo neexistuje. Skuste vybrat inu poziciu.')
        tah_hraca(hracie_pole)
        hracie_pole = ''.join(hracie_pole)
    return hracie_pole

print(tah_hraca(hracie_pole))
