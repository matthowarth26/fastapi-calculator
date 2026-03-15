import pytest
from app.operations import add, subtract, multiply, divide

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(5,2) == 3

def test_multiply():
    assert multiply(2,3) == 6

def test_division_positive():
    assert divide(6, 3) == 2

def test_division_negative():
    assert divide(-1, 1) == -1

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1, 0)