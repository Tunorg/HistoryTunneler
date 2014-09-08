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


import BaseType


class Zombi(BaseType.Undead):
    """Зомби"""

    def __init__(self):
        super().__init__()

        self.name = "Зомби"
        self.desc = "Когда-то это было живым существом."

        self.b_evasion = 0  # Зомби медленные и неуклюжие, потому не умеют уклоняться
        self.b_speed = 6
        self.b_hit = 85  # Зомби сложно попасть


class SuperZombi(Zombi):
    """Зомби-чемпион"""

    def __init__(self):
        super().__init__()

        self.name = "Зомби-Чемпион"

        self.b_speed *= 1.2

        # Чемпион-зомби будет сильнее обычного зомби
        self.m_atk *= 1.5
        self.m_strength *= 1.5
        self.m_vitality *= 1.5


class Human(BaseType.Humanoids):
    """Человек"""

    def __init__(self):
        super().__init__()

        self.race = "Человек"


class Hero(Human):
    """Герой"""

    def __init__(self):
        super().__init__()

        self.name = "Проходчик"
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
        c.evasion = self.b_evasion + c.level // 5

        # все герои удачливые и наш не исключение!
        # удача повышается на 1 за каждые 5 уровней персонажа
        c.luck = self.b_luck + c.level // 5


# http://www.mirf.ru/Articles/art200.htm
class Goblin(BaseType.Humanoids):
    """Гоблин"""

    def __init__(self):
        super().__init__()

        self.name = "Гоблин"
        self.desc = "Маленькое, пронырливое, трусливое зеленокожее существо."
        self.race = "Гоблиноид"
    
        self.b_atk = 2
        self.b_strength = 2
        self.b_vitality = 1
        self.b_speed = 9
        self.b_evasion = 7


# http://www.mirf.ru/Articles/art200.htm
class Hobgoblin(Goblin):
    """Хобгоблин"""

    def __init__(self):
        super().__init__()

        self.name = "Хобгоблин"

        self.b_atk = 12
        self.b_strength = 10
        self.b_vitality = 10
        self.b_evasion = 3

        # Хобгоблин сильнее гоблина
        self.m_atk *= 1.3
        self.m_strength *= 1.3
        self.m_vitality *= 1.3


# http://www.mirf.ru/Articles/art200.htm
class Ork(BaseType.Humanoids):
    """Орк"""

    def __init__(self):
        super().__init__()

        self.name = "Орк"
        self.race = "Гоблиноид"

        self.b_atk = 8
        self.b_strength = 8
        self.b_vitality = 8
        self.b_speed = 8
        self.b_evasion = 5