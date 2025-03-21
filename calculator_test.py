import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(1, 9) == 10

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 1) == 2

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(8,0.5) == 4

def test_divide(calc):
    assert calc.divide(6, 2) == 3
    assert calc.divide(8, 4) == 2

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(6, 0)
        calc.divide(0, 0)

def test_get_random(calc):
    assert calc.get_radnom(0,6) <= 6
    assert calc.get_radnom(1,4) >= 1
    assert not calc.get_radnom(2,5) > 5 
