piesen = """Got a doll, baby, I love her so
        Nothing else like her anywhere you go
        Man, she's anything but calm
        A regular pint sized atom bomb

        Atom bomb baby, little atom bomb
        I want her in my wigwam
        She's just the way I want her to be
        A million times hotter than TNT

        Atom bomb baby loaded with power
        Radioactive as a TV tower
        A nuclear fission in her soul
        Loves with electronic control
    """

def ktory_znak():
    """Spyta sa pouzivatela na znak, ktory chce vyhladat."""
    znak = input('Ktory znak by ste chceli vyhladat v piesni? ')
    return znak

def uprava_piesne(piesen):
    """Zmeni vsetky znaky na male. Prevedie str na list."""
    piesen = piesen.lower()
    piesen_list = list(piesen)
    return piesen_list

def najdi_znak(nas_list, znak):
    """Najde pozadovany znak v liste. Znak zada pouzivatel."""
    pocet = nas_list.count(znak)
    return pocet


piesen_list = uprava_piesne(piesen)
znak = ktory_znak()
print(najdi_znak(piesen_list, znak))
