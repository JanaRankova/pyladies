def turn(board, position, symbol):
    """Rewrites the board with given symbol on given position. Returns new version of the board."""
    board[position] = symbol
    return board

def what_symbol():
    """Ask player to choose symbol to play with. Returns symbol."""
    while True:
        player_symbol = input('S ktorym symbolom chcete hrat? "x" alebo "o"? ')
        try:
            assert player_symbol == 'x' or player_symbol == 'o'
        except AssertionError:
            print('Na vyber mate len z "x" a "o"!')
        else:
            break
    return player_symbol

