meno = ''

def get_name():
    """Zoberie meno od pouzivatela."""
    meno = input('Napiste svoje priezvisko, prosim. ')
    return meno.lower()         #vystup do lower() aby som nemusela v podmnienky_pre_urcenie dat aj podmienku navyse

def overenie_mena(meno):
    """Skontroluje, ci su v stringu len pismena.""" 
    pismena = meno.isalpha()
    if pismena == True:
        return True
    else:
        return False

def podmienky_pre_urcenie(meno):
    """Urci podmienky, pri ktorych povazujeme meno za zenske/muzske."""
    if meno[-1] == 'a' or meno[-1] == 'á':
        pohlavie = 'zena'
    else: 
        pohlavie = 'muz'
    return pohlavie

meno = get_name()              
while overenie_mena(meno) == False:             #pokial meno nie je spravne, poziada o opatovne zadanie az pokym nie su splnene podmienky
    print('Zadane meno nie je v spravnom formate. Skuste ho, prosim, zadat znova: ')
    meno = get_name()
    if overenie_mena(meno) == True:
        break

if podmienky_pre_urcenie(meno) == 'zena':
    print('Zadane meno {} je pravdepodobne zenske.'.format(meno.capitalize()))
else:
    print('Zadane meno {} je pravdepodobne muzske.'.format(meno.capitalize()))
