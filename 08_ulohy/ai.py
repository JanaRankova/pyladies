def comp_turn(board):
    """Generates random turn for pc. Rewrites and returns board with changes."""
    import random
    position = random.randrange(0, 20)
    if board[position] == '-':
            board[position] = 'o'          
            board = ''.join(board)
    else:
        comp_turn(board)
        board = ''.join(board)
    return board