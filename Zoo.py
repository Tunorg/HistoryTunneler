__author__ = 'ipetrash'

from Character import Character


class Zombi(Character):
    """Класс Зомби."""

    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."

        self.atk = 40
        self.level = 7
        self.max_hp, self.hp = 468, 468
        self.strength = 30
        self.vit = 10
        self.mag = 6
        self.spr = 5
        self.spd = 21
        self.eva = 0
        self.hit = 100
        self.luck = 10


class Goblin(Character):
    """Класс Гоблин."""

    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."

        self.atk = 30

        self.level = 17
        self.max_hp, self.hp = 482, 482
        self.strength = 18
        self.vit = 5
        self.mag = 10
        self.spr = 4
        self.spd = 17
        self.eva = 10
        self.hit = 100
        self.luck = 15