stastna_str = ''
bohata_str = ''
stastna = bool
bohata = bool 

def user_input(a_n):
    """zoberie odpoved od uzivatela"""
    a_n = input('Odpovedaj len ano alebo nie (a/n). ')
    a_n = a_n.lower()
    a_n = a_n.replace(' ', '')
    return a_n

def conditions(stav_str):
    """podla podmienok prideli stavu True alebo False"""
    if stav_str == 'ano' or stav_str == 'a':
        stav = True
        return stav
    elif stav_str == 'ne' or stav_str == 'n':
        stav = False
        return stav
    else:
        print('Nerozumím!')

def advice(stav1, stav2):
    """priradi komentar ku roznym stavom"""
    if stav1 and stav2:
        print('Gratuluji!')
    elif stav2:
        print('Zkus se víc usmívat.')
    elif stav1:
        print('Zkus míň utrácet.')
    else:
        print('To je mi líto.')
    return

print('Si stastna? ')
stastna_str = user_input('')
print('Si bohata? ')
bohata_str = user_input('')
stastna = conditions(stastna_str)
bohata = conditions(bohata_str)
advice(stastna, bohata)
