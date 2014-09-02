__author__ = 'ipetrash'

# Типы существ в D&D, можно там подчерпнуть варианты.
# http://ru.rpg.wikia.com/wiki/%D0%A2%D0%B8%D0%BF_%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0

from math import floor
import Char

# TODO: Модуль CharType переименовать в Type
# TODO: Класс CharType переименовать в Base

class CharType:
    """Базовый класс типов персонажей."""
    name = "???"
    description = "???"

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


# TODO: Класс UndeadType переименовать в Undead
class UndeadType(CharType):
    """Тип нежить"""
    name = "Нежить"
    desc = "Оживлённые останки существ или неупокоенные духи"


# TODO: Класс ZombiType переименовать в Zombi
class ZombiType(UndeadType):
    """Тип нежить: зомби"""
    name = "Зомби"
    desc = "Оживлённые останки существ или неупокоенные духи"


# TODO: Класс SuperZombiType переименовать в SuperZombi
class SuperZombiType(ZombiType):
    """Тип нежить: зомби-чемпион"""
    name = "Зомби-Чемпион"
    desc = "Оживлённые останки существ или неупокоенные духи"

    # Чемпион-зомби будет сильнее обычного зомби
    m_atk = ZombiType.m_atk * 1.5
    m_strength = ZombiType.m_strength * 1.5
    m_vitality = ZombiType.m_vitality * 1.5


# TODO: Класс HumanoidsType переименовать в Humanoid
class HumanoidsType(CharType):
    """Тип гуманоиды """
    name = "Гуманоиды"
    desc = ("Представители типовых разумных видов среднего "
            "фентези-мира: эльфы, орки, люди и подобные существа.")


# TODO: Класс GoblinType переименовать в Goblin
class GoblinType(HumanoidsType):
    """Тип гуманоиды: гоблин"""
    name = "Гуманоиды: гоблин"
    desc = ("Представители типовых разумных видов среднего "
            "фентези-мира: эльфы, орки, люди и подобные существа.")
    b_atk = 2
    b_strength = 2
    b_vitality = 1
    b_evasion = 10


# TODO: Класс BeastsType переименовать в Beast
class BeastsType(CharType):
    """Тип звери"""
    name = "Звери"
    desc = ("Естественные существа фентезийных миров. Обычные животные, "
            "а также динозавры, гигантские варианты животных и схожие существа")