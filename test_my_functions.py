import pytest


def test_add():
    result = my_functions.add(1, 5)
    assert result == 6

def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5