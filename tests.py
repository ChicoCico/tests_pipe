import pytest  
import simple_calc   

def test_add():  
    assert simple_calc.add(2, 2) == 4 
def test_devide():
    assert simple_calc.divide(8, 2) == 4 
def test_multiply():
    assert simple_calc.multiply(2, 3) == 6 
def test_subtract():
    assert simple_calc.subtract(2, 2) == 1
