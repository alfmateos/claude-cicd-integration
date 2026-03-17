"""Tests for the calculator module."""
import pytest
from src.calculator import add, subtract, multiply, divide, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
