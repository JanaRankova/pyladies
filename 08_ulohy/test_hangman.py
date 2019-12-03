import hm_functions
import pytest 

def test_get_word():
    """Tests if output of the function is string."""
    output = hm_functions.get_word()
    assert type(output) == str
