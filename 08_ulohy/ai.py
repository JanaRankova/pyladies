import turn_piskvorky

def comp_turn(board):
    """Generates random turn for pc. Rewrites and returns board with changes."""
    import random
    if 'x' in board:
        symbol = 'o'
    else:
        symbol = 'x'
    while True:
        position = random.randrange(0, 20)
        if board[position] == '-':
            return turn_piskvorky.turn(board, position, symbol)
    