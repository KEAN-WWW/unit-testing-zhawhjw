"""This is the starting test file"""
from app.multiplication import multiply


def test_multiplication():
    """multiply two numbers"""
    result = multiply(2, 2)
    assert result == 4
