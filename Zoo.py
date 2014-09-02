__author__ = 'ipetrash'

from Char import Character


class Hero(Character):
    """Класс Герой"""

    def __init__(self):
        self.name = "Проходчик"
        self.description = "Собственно это я!"

        self.atk = 20
        self.strength = 25
        self.vitality = 10
        # self.magic = 6
        # self.spirit = 5
        # self.speed = 21
        self.evasion = 20
        self.hit = 100
        self.luck = 10

        self.level = 1
        self.hp = self.max_hp


class Zombi(Character):
    """Класс Зомби."""

    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."

        self.atk = 10
        self.strength = 8
        self.vitality = 10
        # self.magic = 6
        # self.spirit = 5
        # self.speed = 21
        self.evasion = 0
        self.hit = 65
        self.luck = 5

        self.level = 1
        self.hp = self.max_hp


class Goblin(Character):
    """Класс Гоблин."""

    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."

        self.atk = 8
        self.strength = 5
        self.vitality = 5
        # self.magic = 10
        # self.spirit = 4
        # self.speed = 17
        self.evasion = 5
        self.hit = 68
        self.luck = 5

        self.level = 1
        self.hp = self.max_hp