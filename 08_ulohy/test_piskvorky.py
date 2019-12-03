import ai
import piskvorky
import pytest
import turn_piskvorky

def test_ai_lenght():
    """Checks lenght of output and whether only one symbol is added in each round."""
    board = list(20 * '-')
    lenght = turn_piskvorky.turn(board, 10, 'o')
    assert len(lenght) == 20
    assert lenght.count('o') == 1
    assert lenght.count('-') == 19

def test_ai_output():
    """Checks whether output of comp_turn() is string not list."""
    board = list(20 * '-')
    output_type = turn_piskvorky.turn(board, 10, 'x')
    assert type(output_type) == list

def test_x_win():
    """Whether 'xxx' combination on board leads to x victory."""
    xxx = piskvorky.evaluate('--xxx---------------')
    assert xxx == 'x'

def test_o_win():
    """Whether 'xxx' combination on board leads to x victory."""
    ooo = piskvorky.evaluate('--ooo---------------')
    assert ooo == 'o'

def test_board_lenght():
    from random import randrange
    board = list('')
    with pytest.raises(IndexError):
        turn_piskvorky.turn(board, randrange(0, 20), 'x')

def test_turn_type():
    board = ('--------------------')
    with pytest.raises(TypeError):
        ai.comp_turn(board)
