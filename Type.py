__author__ = 'ipetrash'
# TODO: добавить __doc__ с описанием модуля

import BaseType


class Zombi(BaseType.Undead):
    """Тип нежить: зомби"""

    def __init__(self):
        BaseType.Undead.__init__(self)

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


class Human(BaseType.Humanoids):
    """Тип человек"""

    def __init__(self):
        BaseType.Humanoids.__init__(self)

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

        BaseType.Humanoids.do_calc_stats(self, c)

        # Добавим собственное правило для героя:
        # шанс уклонения повышается на 1 за каждые 5 уровней персонажа
        c.evasion = self.b_evasion + c.level // 5

        # все герои удачливые и наш не исключение!
        # удача повышается на 1 за каждые 5 уровней персонажа
        c.luck = self.b_luck + c.level // 5


# Инфа по оркам, гоблинам и хобгоблинам: http://www.mirf.ru/Articles/art200.htm
# TODO: почему бы "их", смотри выше, не отнести к "Гоблиноидам".
# TODO: добавить Орка и Хобгоблина (класс Хобгоблин наследуется от Гоблин).
class Goblin(BaseType.Humanoids):
    """Тип гуманоид: гоблин"""

    def __init__(self):
        BaseType.Humanoids.__init__(self)

        self.name = "Гоблин"
        self.race = "Гоблин"  # TODO: гоблины и орки, кажется, относятся к одной расе
    
        self.b_atk = 2
        self.b_strength = 2
        self.b_vitality = 1
        self.b_evasion = 7