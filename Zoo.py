__author__ = 'ipetrash'

from Character import Character


class Zombi(Character):
    """Класс Зомби."""

    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."

        self.atk = 40
        self.level = 7
        self.strength = 30
        self.vitality = 10
        # self.magic = 6
        # self.spirit = 5
        # self.speed = 21
        self.evasion = 0
        self.hit = 100
        self.luck = 10

        self.hp = self.max_hp


class Goblin(Character):
    """Класс Гоблин."""

    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."

        self.atk = 30

        self.level = 17
        self.strength = 18
        self.vitality = 5
        # self.magic = 10
        # self.spirit = 4
        # self.speed = 17
        self.evasion = 10
        self.hit = 100
        self.luck = 15

        self.hp = self.max_hp