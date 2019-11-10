from random import randrange

def vyhodnot(hracie_pole):
    """Vezme momentalny stav hracieho pola a podla podmienok vo funkcii, urci vyhercu."""
    stav = ''
    if 'xxx' in hracie_pole:
        stav = 'x'
    elif 'ooo' in hracie_pole:
        stav = 'o'
    elif '-' not in hracie_pole:
        stav = '!'
    else:
        stav = '-'
    return stav

def tah_hraca(hracie_pole):
    """Spyta sa hraca na poziciu, na ktoru chce  umiestnit symbol (hrac hra za 'x'). Zamietne nespravne zadane znaky.
    Prepise hracie pole a vrati ho."""
    cislo_policka = int(input('Zadajte poziciu, na ktoru chcete umiestnit symbol. Platne su cisla od 1-20. '))
    cislo_policka -= 1 
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

def tah_pocitaca(hracie_pole):
    """Generuje nahodne cislo a tah pocitaca na prazdne pole. Vracia hracie pole uz s tahom pc."""
    cislo_policka = randrange(0, 20)
    if hracie_pole[cislo_policka] == '-':
            hracie_pole[cislo_policka] = 'o'          
            hracie_pole = ''.join(hracie_pole)
    else:
        tah_pocitaca(hracie_pole)
        hracie_pole = ''.join(hracie_pole)
    return hracie_pole

def piskvorky_1D():
    """Striedavo vola tah_hraca a tah_pocitaca a kontroluje vysledky az do momentu, kym jedna strana nevyhra.
    Printuje medzistav po kazdom kole."""
    pocet_kol = 0
    hracie_pole = list('-' * 20)
    while True:
        hracie_pole = list(hracie_pole)
        hracie_pole = tah_hraca(hracie_pole)
        vyhodnot(hracie_pole)
        pocet_kol += 1
        print('{}. kolo: {}'.format(pocet_kol, hracie_pole))
        hracie_pole = list(hracie_pole)
        hracie_pole = tah_pocitaca(hracie_pole)
        vyhodnot(hracie_pole)
        pocet_kol += 1
        print('{}. kolo: {}'.format(pocet_kol, hracie_pole))
        if vyhodnot(hracie_pole) != '-':
            break
    if vyhodnot(hracie_pole) == 'x':
        vyherca = 'x'
    elif vyhodnot(hracie_pole) == 'o':
        vyherca = 'o'
    else:
        vyherca = 'none'
    return vyherca

print('Hru vyhral hrac hrajuci za "{}" symbol.'.format(piskvorky_1D()))
