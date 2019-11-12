from random import randrange                  
playerturn = ''
compturn = ''

def player_turn():
    """Ask player for a turn."""
    response = input('Vyber si: kamen, papier alebo noznice?')
    response_num = int
    if response == 'kamen':
        response_num = 0
        return response_num
    elif response == 'noznice':
        response_num = 1
        return response_num
    elif response == 'papier':
        response_num = 2
        return response_num
    else:
        print('Nerozumiem!')
    

def comp_turn():
    """Generates random turn for a computer."""
    throw = randrange(3)
    if throw == 0:                           
        print('Pocitac si nahodne vybral kamen.')
    elif throw == 1:
        print('Pocitac si nahodne vybral noznice.')
    elif throw == 2:
        print('Pocitac si nahodne vybral papier.')
    return throw
    
def results(playerturn, compturn):
    """Evaluates turns and print results."""
    if playerturn == compturn:
        print('Plichta.')
    elif ((playerturn == 0 and compturn == 1) or (playerturn == 1 and compturn == 2) or (playerturn == 2 and compturn == 0)):
        print('Vyhral(a) si!')
    else:
        print('Prehral(a) si!')
    return 

while True:
    playerturn = player_turn()
    if playerturn == None:
        break

    compturn = comp_turn()
    results(playerturn, compturn)
    print('Chces si zahrat este jedno kolo? (ak nie napis "koniec")')
    play_again = input()
    if play_again == 'koniec':
        break
