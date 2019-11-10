hracie_pole = '--------------------'

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

print(vyhodnot(hracie_pole))