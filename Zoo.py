"""Zoo.py: Модуль содержит классы персонажей"""

__author__ = 'ipetrash'

# TODO: нужно объединить модули Type.py и Zoo.py

from Char import BaseCharacter
import Type


class Hero(BaseCharacter):
    """Класс Герой"""

    def __init__(self):
        super().__init__(char_type=Type.Hero())


class Zombi(BaseCharacter):
    """Класс Зомби."""

    def __init__(self):
        super().__init__(char_type=Type.Zombi())


class Goblin(BaseCharacter):
    """Класс Гоблин."""

    def __init__(self):
        super().__init__(char_type=Type.Goblin())