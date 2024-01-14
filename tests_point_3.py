
from distance import Millimeter, Centimeter, Meter, Inch

def test_add_method():
    left = Meter(9.2)
    right = Inch(9.2)
    assert (left + right).as_millimeters() == 9433.68, 'Метод __add__ реализован не корректно'

def test_sub_method():
    left = Inch(86.44)
    right = Millimeter(94.78)
    assert (left - right).as_millimeters() == 2100.796, 'Метод __sub__ реализован не корректно'

def test_mul_method():
    left = Centimeter(94.95)
    right = Millimeter(10.8)
    assert (left * right).as_millimeters() == 1025.46, 'Метод __mul__ реализован не корректно'

def test_truediv_method():
    left = Meter(38.07)
    right = Millimeter(44.74)
    assert (left / right).as_millimeters() == 850916.4059, 'Метод __mul__ реализован не корректно'


test_add_method()
test_sub_method()
test_mul_method()
test_truediv_method()
