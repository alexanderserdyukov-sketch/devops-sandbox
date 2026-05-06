import os

# test_app.py
from simple_math_uv.app import add_numbers, subtract_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5
