import ai
import turn_piskvorky

def evaluate(board):
    """Evaluates curent state of the game and determines winner."""
    state = ''
    if 'xxx' in board:
        state = 'x'
    elif 'ooo' in board:
        state = 'o'
    elif '-' not in board:
        state = '!'
    else:
        state = '-'
    return state

def user_turn(board):
    """Ask player for a position to place 'x' on. Denies wrong position and non integer input. Rewrites 
    and returns board."""
    symbol = turn_piskvorky.what_symbol()
    while True:
        position = int(input('Zadajte poziciu, na ktoru chcete umiestnit symbol. Platne su cisla od 1-20. '))
        position -= 1 
        if position not in range(0, 20):
           print('Vami zadana pozicia je obsadena alebo neexistuje. Skuste vybrat inu poziciu.')
        elif board[position] != '-':
           print('Vami zadana pozicia je obsadena alebo neexistuje. Skuste vybrat inu poziciu.')
        else:
            break
    return turn_piskvorky.turn(board, position, symbol)

def tictactoe_1D():
    """Alternately calls for user_turn and comp_turn up the winning turn of either.
    Prints board state after each turn."""
    round_count = 0
    board = '-' * 20
    while True:
        board = list(board)
        board = user_turn(board)
        board = ''.join(board)
        evaluate(board)
        round_count += 1
        print('{}. kolo: {}'.format(round_count, board))
        board = list(board)
        board = ai.comp_turn(board)
        board = ''.join(board)
        evaluate(board)
        print('{}. kolo: {}'.format(round_count, board))
        if evaluate(board) != '-':
            break
    if evaluate(board) == 'x':
        print('Hru vyhral hrac hrajuci za "x" symbol.')
    elif evaluate(board) == 'o':
        print('Hru vyhral hrac hrajuci za "o" symbol.')
    else:
        print('Hra skoncila remizou hraca a pocitaca.')
