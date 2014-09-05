"""Zoo.py: Модуль содержит классы персонажей"""

__author__ = 'ipetrash'


from Char import BaseCharacter
import Type


class Hero(BaseCharacter):
    """Класс Герой"""

    def __init__(self):
        super().__init__(type=Type.Hero())


class Zombi(BaseCharacter):
    """Класс Зомби."""

    def __init__(self):
        super().__init__(type=Type.Zombi())


class Goblin(BaseCharacter):
    """Класс Гоблин."""

    def __init__(self):
        super().__init__(type=Type.Goblin())


class Ork(BaseCharacter):
    """Класс Орк."""

    def __init__(self):
        super().__init__(type=Type.Ork())