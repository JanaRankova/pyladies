surname = ''

def get_name():
    """Asks for user surname."""
    surname = input('Napiste svoje priezvisko, prosim. ')
    return surname.lower()         #vystup do lower() aby som nemusela v podmnienky_pre_urcenie dat aj podmienku navyse

def validate_surname(surname):
    """Checks whether all elements in string are alpha characters.""" 
    char = surname.isalpha()
    if char == True:
        return True
    else:
        return False

def conditions_for_surname(surname):
    """Sets conditions for male and female surname."""
    if surname[-1] == 'a' or surname[-1] == 'á':
        sex = 'zena'
    else: 
        sex = 'muz'
    return sex

surname = get_name()              
while validate_surname(surname) == False:             #pokial surname nie je spravne, poziada o opatovne zadanie az pokym nie su splnene podmienky
    print('Zadane priezvisko nie je v spravnom formate. Skuste ho, prosim, zadat znova: ')
    surname = get_name()
    if validate_surname(surname) == True:
        break

if conditions_for_surname(surname) == 'zena':
    print('Zadane priezvisko {} je pravdepodobne zenske.'.format(surname.capitalize()))
else:
    print('Zadane priezvisko {} je pravdepodobne muzske.'.format(surname.capitalize()))
