happy_str = ''
wealthy_str = ''

def user_input(and_or):
    """Takes user anwer and modifies it."""
    and_or = input('Odpovedaj len ano alebo nie (a/n). ')
    and_or = and_or.lower()
    and_or = and_or.replace(' ', '')
    return and_or

def conditions(state_str):
    """podla podmienok prideli stavu True alebo False"""
    if state_str == 'ano' or state_str == 'a':
        return True
    elif state_str == 'ne' or state_str == 'n':
        return False
    else:
        print('Nerozumím!')

def advice(state1, state2):
    """priradi komentar ku roznym stavom"""
    if state1 and state2:
        print('Gratuluji!')
    elif state2:
        print('Zkus se víc usmívat.')
    elif state1:
        print('Zkus míň utrácet.')
    else:
        print('To je mi líto.')
    return

print('Si stastna? ')
happy_str = user_input('')
print('Si bohata? ')
wealthy_str = user_input('')
happy = conditions(happy_str)
wealthy = conditions(wealthy_str)
advice(happy, wealthy)
