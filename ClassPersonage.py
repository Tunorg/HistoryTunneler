"""ClassPersonage.py: Модуль содержит классы персонажей"""

__author__ = 'ipetrash'


from BasePersonage import Personage
import Type as t
import BaseType as bt


class Hero(Personage):
    """Класс Герой"""

    def __init__(self):
        super().__init__()
        self.type = t.Hero()


class Bandit(Personage):
    """Класс Бандит"""

    def __init__(self):
        super().__init__()
        self.name = "Бандит"

        self.type = t.Human()
        self.type.name = "Бандит"
        self.type.b_atk = 4
        self.type.b_strength = 3
        self.type.b_vitality = 2
        self.type.b_evasion = 2

        self.update_states()


class Thief(Personage):
    """Класс Вор"""

    def __init__(self):
        super().__init__()
        self.name = "Вор"

        self.type = t.Human()
        self.type.name = "Вор"
        self.type.b_atk = 2
        self.type.b_strength = 2
        self.type.b_vitality = 2
        self.type.b_evasion = 7
        self.type.b_luck = 7  # Воры более удачливее обычных людей

        self.update_states()


class Zombi(Personage):
    """Класс Зомби."""

    def __init__(self):
        super().__init__()
        self.name = "Зомби"

        self.type = bt.Undead()
        self.type.name = "Зомби"
        self.type.desc = "Когда-то это было живым существом."
        self.type.b_evasion = 0  # Зомби медленные и неуклюжие, потому не умеют уклоняться
        self.type.b_speed = 6
        self.type.b_hit = 85  # Зомби сложно попасть

        self.update_states()


# http://www.mirf.ru/Articles/art200.htm
class Goblin(Personage):
    """Класс Гоблин."""

    def __init__(self):
        super().__init__()
        self.name = "Гоблин"
        
        self.type = bt.Humanoids()
        self.type.name = "Гоблин"
        self.type.desc = "Маленькое, пронырливое, трусливое зеленокожее существо."
        self.type.race = "Гоблиноид"
        self.type.b_atk = 2
        self.type.b_strength = 2
        self.type.b_vitality = 1
        self.type.b_speed = 9
        self.type.b_evasion = 7
        
        self.update_states()
        

# http://www.mirf.ru/Articles/art200.htm
class Ork(Personage):
    """Класс Орк."""

    def __init__(self):
        super().__init__()
        self.name = "Орк"
        
        self.type = bt.Humanoids()
        self.type.name = "Орк"
        self.type.race = "Гоблиноид"
        self.type.b_atk = 8
        self.type.b_strength = 8
        self.type.b_vitality = 8
        self.type.b_speed = 8
        self.type.b_evasion = 5

        self.update_states()
        

# Класс персонажа можно создать не из "готового" типа,
# из базового типа, только придется вручную заполнить тип
class Wolf(Personage):
    """Класс Волк."""

    def __init__(self):
        super().__init__()

        self.name = "Лесной Волк"

        self.type = bt.Beast()
        self.type.name = "Волк"
        self.type.b_atk = 5
        self.type.b_strength = 5
        self.type.b_vitality = 5
        self.type.b_evasion = 10

        self.update_states()
