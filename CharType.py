__author__ = 'ipetrash'

# Типы существ в D&D, можно там подчерпнуть варианты.
# http://ru.rpg.wikia.com/wiki/%D0%A2%D0%B8%D0%BF_%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0
# TODO: Привести все типы персонажей из типов существ (думаю воспользоваться 5-й редакцией D&D)

from math import floor
import Char

# TODO: Модуль CharType переименовать в Type

class BaseType:
    """Базовый класс типов персонажей."""

    name = "???"  # конкретное название: name_type: гуманоид, но name может быть человек, орк, эльф и т.п.
    name_type = "???"  # например, нежить, люди, звери
    description = "???"  # короткое описание типа персонажа
    race = "???"  # раса: например, люди, орки, эльфы, нежить, драконы и т.п.

    # базовые статы
    b_atk = 5
    b_strength = 5
    b_vitality = 5
    b_evasion = 5
    b_hit = 95
    b_luck = 5

    # множитель статов
    m_atk = 5
    m_strength = 3
    m_vitality = 2


    def do_calc_stats(self, char):
        """Функция выполняет подсчет статов персонажа"""

        char.atk = floor(self.b_atk + self.m_atk * char.level)
        char.strength = floor(self.b_strength + self.m_strength * char.level)
        char.vitality = floor(self.b_vitality + self.m_vitality * char.level)
        char.evasion = self.b_evasion
        char.hit = self.b_hit
        char.luck = self.b_luck

        # FF9: http://finalfantasy.wikia.com/wiki/HP
        # [Str * HPMod(Level) / 50]
        char.max_hp = floor(char.strength * Char.HPMOD[char.level] / 50)
        char.hp = char.max_hp


class Undead(BaseType):
    """Тип нежить"""

    name_type = "Нежить"
    desc = "Оживлённые останки существ или неупокоенные духи"
    race = "Нежить"


class Zombi(Undead):
    """Тип нежить: зомби"""

    name = "Зомби"

    b_evasion = 0  # Зомби медленные и неуклюжие, потому не умеют уклоняться
    b_hit = 85  # Зомби сложно попасть


class SuperZombi(Zombi):
    """Тип нежить: зомби-чемпион"""

    name = "Зомби-Чемпион"

    # Чемпион-зомби будет сильнее обычного зомби
    m_atk = Zombi.m_atk * 1.5
    m_strength = Zombi.m_strength * 1.5
    m_vitality = Zombi.m_vitality * 1.5


class Humanoid(BaseType):
    """Тип гуманоид"""

    name_type = "Гуманоид"
    desc = ("Представители типовых разумных видов среднего "
            "фентези-мира: эльфы, орки, люди и подобные существа.")

    def do_calc_stats(self, char):
        """Переопределенная функция выполняет подсчет статов гуманоидов"""
        BaseType.do_calc_stats(self, char)

        # Добавим собственное правило для гуманоидов:
        # шанс уклонения повышается на 1 за каждые 20 уровней персонажа
        char.evasion = self.b_evasion + char.level // 20


class Human(Humanoid):
    """Тип человек"""

    race = "Человек"


class Hero(Human):
    """Тип герой"""

    name = "Герой"

    b_atk = 10
    b_strength = 8
    b_hit = 100
    b_evasion = 10

    m_atk = 10
    m_strength = 8
    m_vitality = 6


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

    name = "Гоблин"
    race = "Гоблин"  # TODO: гоблины и орки, кажется, относятся к одной расе

    b_atk = 2
    b_strength = 2
    b_vitality = 1
    b_evasion = 7


class Beast(BaseType):
    """Тип зверь"""

    name_type = "Зверь"
    desc = ("Естественные существа фентезийных миров. Обычные животные, "
            "а также динозавры, гигантские варианты животных и схожие существа")