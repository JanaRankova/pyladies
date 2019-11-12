hracie_pole = list('-' * 20)
cislo_policka = int  #0-19 podmienku definujem az pri dalsej ulohe
symbol = '' #len 'o' alebo 'x', ale myslim, ze tuto podmienku staci definovat az do dalsej casti pri inpute

def tah(hracie_pole, cislo_policka, symbol):
    """Vrati hracie pole upravene s danym symbolom na danej pozicii."""
    cislo_policka = cislo_policka - 1       #index zacina od nuly 
    hracie_pole[cislo_policka] = symbol
    hracie_pole = ''.join(hracie_pole)
    return hracie_pole

#napr.:
print(tah(hracie_pole, 10, 'x'))
