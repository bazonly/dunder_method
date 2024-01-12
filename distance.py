
from functools import total_ordering
from typing import Any

@total_ordering
class Millimeter:
    _label = 'мм'
    _ratio = 1 # Отношение определяемой еденицы измерения к миллиметрам
    _value: float = 0

    def __init__(self, value: Any) -> None:

        try:
            if type(value) == int:
                self._value = float(value)
            elif type(value) == float:
                self._value = value
            elif issubclass(value, Millimeter):
                self._value = float(value.as_millimeters()/self._ratio)
        except TypeError:
            print('enter valid dictionary')

    def __repr__(self):
        return (f'class name: {__name__}, '
                f'label: {self._label}, '
                f'ratio: {self._ratio}'
                f'value: {self._value}')

    def __hash__(self):
        return hash(self.as_millimeters())

    def as_millimeters(self) -> float:
        """Возвращает значение длины в миллиметах.

        :rtype: float
        :return: Значение округленное до 5 знаков после запятой
        """
        return round(self._value * self._ratio, 5)

    def __add__(self, other):
        return self._value + other._value

    def __sub__(self, other):
        return self._value - other._value

    def __mul__(self, other):
        return self._value * other._value

    def __truediv__(self, other):
        if other._value == 0:
            raise 'division by zero is not possible'
        else:
            return self._value / other._value

    def __eq__(self, other):
        return self._value == other._value

    def __lt__(self, other):
        return self._value < other._value

    def __int__(self):
        return int(self.as_millimeters())

    def __float__(self):
        return float(self.as_millimeters())

class Centimeter(Millimeter):
    label = 'см'
    ratio = 10


class Meter(Millimeter):
    label = 'метр'
    ratio = 1000


class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4
