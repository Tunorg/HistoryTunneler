"""ClassPersonage.py: Модуль содержит классы персонажей"""

__author__ = 'ipetrash'


from BasePersonage import Personage
import Type


class Hero(Personage):
    """Класс Герой"""

    def __init__(self):
        super().__init__(ptype=Type.Hero())


class Zombi(Personage):
    """Класс Зомби."""

    def __init__(self):
        super().__init__(ptype=Type.Zombi())


class Goblin(Personage):
    """Класс Гоблин."""

    def __init__(self):
        super().__init__(ptype=Type.Goblin())


class Ork(Personage):
    """Класс Орк."""

    def __init__(self):
        super().__init__(ptype=Type.Ork())