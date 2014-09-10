"""Type.py: Модуль содержит персонализированные типы персонажей

С модулем Type, возможно, можно создавать персонажей динамично.
Для создания нужного существа, создавать экземпляр BaseCharacter и
передавать нужный тип персонажа, например для гоблина:
import Type
from Char import BaseCharacter
g = BaseCharacter()
g.type = Type.Goblin()

А если передавать в конструктор, то будет выглядеть приятнее:
import Type
from Char import BaseCharacter
g = BaseCharacter(type=Type.Goblin())

Или:
from Type import Goblin
from Char import BaseCharacter
g = BaseCharacter(char_type=Goblin())
print(g)
"""

__author__ = 'ipetrash'


# TODO: добавить регистрация типов, так чтобы можно было в любой момент получить список типов, или получить
# тип по имени (или другому индивидуальному признаку)

# TODO: рассчитать базовые статы типов


import BaseType as bt


class Human(bt.Humanoids):
    """Человек"""

    def __init__(self):
        super().__init__()

        self.race = "Человек"

        self.b_atk = 4
        self.b_strength = 4
        self.b_vitality = 4
        self.b_speed = 10


class Hero(Human):
    """Герой"""

    def __init__(self):
        super().__init__()

        self.name = "Герой"
        self.desc = "Главный герой этой истории"

        self.b_atk = 10
        self.b_strength = 8
        self.b_hit = 100
        self.b_speed = 15
        self.b_evasion = 10

        self.m_atk = 10
        self.m_strength = 8
        self.m_vitality = 6

    def do_calc_stats(self, c):
        """Переопределенная функция выполняет подсчет статов героя"""

        super().do_calc_stats(c)

        # Добавим собственное правило для героя:
        # шанс уклонения повышается на 1 за каждые 5 уровней персонажа
        c.evasion += c.level // 5

        # скорость повышается на 1 за каждые 7 уровней персонажа
        c.speed += c.level // 7

        # все герои удачливые и наш не исключение!
        # удача повышается на 1 за каждые 5 уровней персонажа
        c.luck += c.level // 5


# TODO: реализовать в классе персонажа, наследуя от класса персонажа Goblin
# # http://www.mirf.ru/Articles/art200.htm
# class Hobgoblin(Goblin):
#     """Хобгоблин"""
#
#     def __init__(self):
#         super().__init__()
#
#         self.name = "Хобгоблин"
#
#         self.b_atk = 12
#         self.b_strength = 10
#         self.b_vitality = 10
#         self.b_evasion = 3
#
#         # Хобгоблин сильнее гоблина
#         self.m_atk *= 1.3
#         self.m_strength *= 1.3
#         self.m_vitality *= 1.3
