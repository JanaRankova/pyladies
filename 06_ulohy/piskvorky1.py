hracie_pole = ['-' * 20]

def vyhodnot(hracie_pole):
    """Vezme momentalny stav hracieho pola a podla podmienok vo funkcii, urci vyhercu."""
    stav = ''
    if 'xxx' in hracie_pole[0]:
        stav = 'x'
    elif 'ooo' in hracie_pole[0]:
        stav = 'o'
    elif '-' not in hracie_pole[0]:
        stav = '!'
    else:
        stav = '-'
    return stav

print(vyhodnot(hracie_pole))