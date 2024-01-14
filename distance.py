
from functools import total_ordering
from typing import Any

@total_ordering
class Millimeter:
    _label = 'мм'
    _ratio = 1 # Отношение определяемой еденицы измерения к миллиметрам
    _value: float = 0

    def __init__(self, value) -> None:
        try:
            if isinstance(value, (int, float)):
                self._value = float(value)
            else:
                self._value = float(value.as_millimeters() / self._ratio)
        except TypeError:
            print('enter valid dictionary')
    def __repr__(self):
        return f'{self.__class__.__name__}(value={self._value})'

    def __hash__(self):
        return hash(self.as_millimeters())

    def as_millimeters(self) -> float:
        """Возвращает значение длины в миллиметах.

        :rtype: float
        :return: Значение округленное до 5 знаков после запятой
        """
        return round(self._value * self._ratio, 5)

    def __add__(self, other)-> Any:
        return type(self)((self.as_millimeters() / self._ratio) + (other.as_millimeters() / self._ratio))

    def __sub__(self, other)-> Any:
        return type(self)((self.as_millimeters() / self._ratio) - (other.as_millimeters() / self._ratio))

    def __mul__(self, other)-> Any:
        return type(self)((self.as_millimeters() / self._ratio) * (other.as_millimeters() / self._ratio))

    def __truediv__(self, other)-> Any:
        if other._value == 0:
            raise 'division by zero is not possible'
        else:
            return type(self)((self.as_millimeters() / self._ratio) / (other.as_millimeters() / self._ratio))

    def __eq__(self, other)-> Any:
        return hash(self) == hash(other)

    def __lt__(self, other)-> Any:
        return self.as_millimeters() < other.as_millimeters()

    def __int__(self)-> Any:
        return int(self.as_millimeters())

    def __float__(self)-> Any:
        return float(self.as_millimeters())

class Centimeter(Millimeter):
    _label = 'см'
    _ratio = 10


class Meter(Millimeter):
    _label = 'метр'
    _ratio = 1000


class Inch(Millimeter):
    _label = 'дюйм'
    _ratio = 25.4
