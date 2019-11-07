hracie_pole = ['-' * 20]

def vyhodnot(hracie_pole):
    """Vezme momentalny stav hracieho pola a podla podmienok vo funkcii, urci vyhercu."""
    if 'xxx' in hracie_pole == True:
        stav = 'x'
    elif 'ooo' in hracie_pole == True:
        stav = 'o'
    elif '-' in hracie_pole == False:
        stav = '!'
    else:
        stav = '-'
    return stav

print(vyhodnot(hracie_pole))