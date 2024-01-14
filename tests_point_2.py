

from distance import Millimeter, Centimeter, Meter, Inch

def test_repr_method():
    instance = Inch(9.2332)
    assert repr(instance) in ['Inch(value=9.2332)', 'Inch(9.2332)'], 'Метод __repr__ представляет некорректную или недостаточно информации об объекте'

test_repr_method()
