import ai
import piskvorky
import pytest

def test_ai_lenght():
    """Checks lenght of output and whether only one symbol is added in each round."""
    board = list(20 * '-')
    lenght = ai.comp_turn(board)
    assert len(lenght) == 20
    assert lenght.count('o') == 1
    assert lenght.count('-') == 19

def test_ai_output():
    """Checks whether output of comp_turn() is string not list."""
    board = list(20 * '-')
    output_type = ai.comp_turn(board)
    assert type(output_type) == str

def test_x_win():
    """Whether 'xxx' combination on board leads to x victory."""
    xxx = piskvorky.evaluate('--xxx---------------')
    assert xxx == 'x'

def test_o_win():
    """Whether 'xxx' combination on board leads to x victory."""
    ooo = piskvorky.evaluate('--ooo---------------')
    assert ooo == 'o'

def test_draw():
    board = ('oxoxoxoxoxoxoxoxoxox')
    with pytest.raises(ValueError):
        ai.comp_turn(board)

def test_turn_type():
    board = ('--------------------')
    with pytest.raises(TypeError):
        ai.comp_turn(board)
