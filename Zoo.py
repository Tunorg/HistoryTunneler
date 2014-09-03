__author__ = 'ipetrash'
# TODO: добавить __doc__ с описанием модуля

from Char import BaseCharacter
import Type


# TODO: С развитием модуля Type, возможно, нет смысла в наследовании от BaseCharacter, ведь
# все можно описать в типе. А для создания нужного существа, создавать экземпляр BaseCharacter и
# передавать нужны тип персонажа, например для гоблина:
# import Type
# g = BaseCharacter()
# g.type = Type.Goblin()
#
# А если передавать в конструктор, то будет выглядеть приятнее:
# import Type
# g = BaseCharacter(type=Type.Goblin())
#
# Или:
# from Type import Goblin()
# g = BaseCharacter(type=Goblin())
#

# TODO: переименовать модуль, название зоопарк не совсем корректно, хоть и забавно :)


class Hero(BaseCharacter):
    """Класс Герой"""

    def __init__(self):
        BaseCharacter.__init__(self)

        self.name = "Проходчик"
        self.description = "Собственно это я!"
        self.type = Type.Hero()

        self.update_states()


class Zombi(BaseCharacter):
    """Класс Зомби."""

    def __init__(self):
        BaseCharacter.__init__(self)

        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."
        self.type = Type.Zombi()

        self.update_states()


class Goblin(BaseCharacter):
    """Класс Гоблин."""

    def __init__(self):
        BaseCharacter.__init__(self)

        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."
        self.type = Type.Goblin()

        self.update_states()