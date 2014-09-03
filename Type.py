__author__ = 'ipetrash'

# Типы существ в D&D, можно там подчерпнуть варианты.
# http://ru.rpg.wikia.com/wiki/%D0%A2%D0%B8%D0%BF_%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0
# TODO: Привести все типы персонажей из типов существ (думаю воспользоваться 5-й редакцией D&D)

from math import floor
import Char

# TODO: Модуль CharType переименовать в Type

class BaseType:
    """Базовый класс типов персонажей"""
    
    def __init__(self):
        self.name = "???"  # конкретное название: name_type: гуманоид, но name может быть человек, орк, эльф и т.п.
        self.name_type = "???"  # например, нежить, люди, звери
        self.description = "???"  # короткое описание типа персонажа
        self.race = "???"  # раса: например, люди, орки, эльфы, нежить, драконы и т.п.
    
        # базовые статы
        self.b_atk = 5
        self.b_strength = 5
        self.b_vitality = 5
        self.b_evasion = 5
        self.b_hit = 95
        self.b_luck = 5
    
        # множитель статов
        self.m_atk = 5
        self.m_strength = 3
        self.m_vitality = 2

    def do_calc_stats(self, c):
        """Функция выполняет подсчет статов персонажа"""

        c.atk = floor(self.b_atk + self.m_atk * c.level)
        c.strength = floor(self.b_strength + self.m_strength * c.level)
        c.vitality = floor(self.b_vitality + self.m_vitality * c.level)
        c.evasion = self.b_evasion
        c.hit = self.b_hit
        c.luck = self.b_luck

        # FF9: http://finalfantasy.wikia.com/wiki/HP
        # [Str * HPMod(Level) / 50]
        c.max_hp = floor(c.strength * Char.HPMOD[c.level] / 50)
        c.hp = c.max_hp


class Undead(BaseType):
    """Тип нежить"""

    def __init__(self):
        BaseType.__init__(self)

        self.name_type = "Нежить"
        self.desc = "Оживлённые останки существ или неупокоенные духи"
        self.race = "Нежить"


class Zombi(Undead):
    """Тип нежить: зомби"""

    def __init__(self):
        Undead.__init__(self)

        self.name = "Зомби"
    
        self.b_evasion = 0  # Зомби медленные и неуклюжие, потому не умеют уклоняться
        self.b_hit = 85  # Зомби сложно попасть


class SuperZombi(Zombi):
    """Тип нежить: зомби-чемпион"""

    def __init__(self):
        Zombi.__init__(self)

        self.name = "Зомби-Чемпион"
    
        # Чемпион-зомби будет сильнее обычного зомби
        self.m_atk *= 1.5
        self.m_strength *= 1.5
        self.m_vitality *= 1.5


class Humanoid(BaseType):
    """Тип гуманоид"""

    def __init__(self):
        BaseType.__init__(self)

        self.name_type = "Гуманоид"
        self.desc = ("Представители типовых разумных видов среднего "
                     "фентези-мира: эльфы, орки, люди и подобные существа.")

    def do_calc_stats(self, c):
        """Переопределенная функция выполняет подсчет статов гуманоидов"""
        BaseType.do_calc_stats(self, c)

        # Добавим собственное правило для гуманоидов:
        # шанс уклонения повышается на 1 за каждые 20 уровней персонажа
        c.evasion = self.b_evasion + c.level // 20


class Human(Humanoid):
    """Тип человек"""

    def __init__(self):
        Humanoid.__init__(self)

        self.race = "Человек"


class Hero(Human):
    """Тип герой"""

    def __init__(self):
        Human.__init__(self)

        self.name = "Герой"
    
        self.b_atk = 10
        self.b_strength = 8
        self.b_hit = 100
        self.b_evasion = 10
    
        self.m_atk = 10
        self.m_strength = 8
        self.m_vitality = 6

    def do_calc_stats(self, c):
        """Переопределенная функция выполняет подсчет статов героя"""
        Humanoid.do_calc_stats(self, c)

        # Добавим собственное правило для героя:
        # шанс уклонения повышается на 1 за каждые 5 уровней персонажа
        c.evasion = self.b_evasion + c.level // 5

        # все герои удачливые и наш не исключение!
        # удача повышается на 1 за каждые 5 уровней персонажа
        c.luck = self.b_luck + c.level // 5


class Goblin(Humanoid):
    """Тип гуманоид: гоблин"""

    def __init__(self):
        Humanoid.__init__(self)

        self.name = "Гоблин"
        self.race = "Гоблин"  # TODO: гоблины и орки, кажется, относятся к одной расе
    
        self.b_atk = 2
        self.b_strength = 2
        self.b_vitality = 1
        self.b_evasion = 7


class Beast(BaseType):
    """Тип зверь"""

    def __init__(self):
        BaseType.__init__(self)

        self.name_type = "Зверь"
        self.desc = ("Естественные существа фентезийных миров. Обычные животные, "
                     "а также динозавры, гигантские варианты животных и схожие существа")