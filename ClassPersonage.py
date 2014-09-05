"""ClassPersonage.py: Модуль содержит классы персонажей"""

__author__ = 'ipetrash'


from Personage import Personage
import Type


class Hero(Personage):
    """Класс Герой"""

    def __init__(self):
        super().__init__(type=Type.Hero())


class Zombi(Personage):
    """Класс Зомби."""

    def __init__(self):
        super().__init__(type=Type.Zombi())


class Goblin(Personage):
    """Класс Гоблин."""

    def __init__(self):
        super().__init__(type=Type.Goblin())


class Ork(Personage):
    """Класс Орк."""

    def __init__(self):
        super().__init__(type=Type.Ork())