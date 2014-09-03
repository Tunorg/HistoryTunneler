__author__ = 'ipetrash'

from Char import BaseCharacter
import Type


class Hero(BaseCharacter):
    """Класс Герой"""

    def __init__(self):
        self.name = "Проходчик"
        self.description = "Собственно это я!"
        self.type = Type.Hero()

        self.update_states()


class Zombi(BaseCharacter):
    """Класс Зомби."""

    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."
        self.type = Type.Zombi()

        self.update_states()


class Goblin(BaseCharacter):
    """Класс Гоблин."""

    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."
        self.type = Type.Goblin()

        self.update_states()