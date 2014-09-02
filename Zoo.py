__author__ = 'ipetrash'

from Char import Character
import CharType

class Hero(Character):
    """Класс Герой"""

    def __init__(self):
        self.name = "Проходчик"
        self.description = "Собственно это я!"
        self.type = CharType.HumanoidsType()

        self.type.b_atk = 10
        self.type.b_strength = 8
        self.type.b_hit = 100

        self.type.m_atk = 8
        self.type.m_strength = 5
        self.type.m_vitality = 4

        self.level = 1


class Zombi(Character):
    """Класс Зомби."""

    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."
        self.type = CharType.ZombiType()

        self.level = 1


class Goblin(Character):
    """Класс Гоблин."""

    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."
        self.type = CharType.GoblinType()

        self.level = 1