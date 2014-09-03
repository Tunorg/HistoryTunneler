__author__ = 'ipetrash'

from Char import BaseCharacter
import CharType


class Hero(BaseCharacter):
    """Класс Герой"""

    def __init__(self):
        self.name = "Проходчик"
        self.description = "Собственно это я!"
        self.type = CharType.Hero()

        # self.type.b_atk = 10
        # self.type.b_strength = 8
        # self.type.b_hit = 100
        #
        # self.type.m_atk = 10
        # self.type.m_strength = 8
        # self.type.m_vitality = 6

        # self.level = 1  # По умолчанию, у всех 1 уровень
        self.update_states()


class Zombi(BaseCharacter):
    """Класс Зомби."""

    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."
        self.type = CharType.Zombi()

        # self.level = 1  # По умолчанию, у всех 1 уровень
        self.update_states()


class Goblin(BaseCharacter):
    """Класс Гоблин."""

    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."
        self.type = CharType.Goblin()

        # self.level = 1  # По умолчанию, у всех 1 уровень
        self.update_states()