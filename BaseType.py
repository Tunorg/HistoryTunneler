"""BaseType.py: Модуль содержит типы персонажей"""

__author__ = 'ipetrash'


from math import floor
import BasePersonage as bp


class BaseType:
    """Базовый класс типов персонажей"""

    def __init__(self):
        self.name = None  # конкретное название: name_type: гуманоид, но name может быть человек, орк, эльф и т.п.
        self.name_type = None  # например, нежить, люди, звери
        self.desc = None  # короткое описание типа персонажа
        self.race = None  # раса: например, люди, орки, эльфы, нежить, драконы и т.п.

        # базовые статы
        self.b_atk = 5
        self.b_strength = 5
        self.b_vitality = 5
        self.b_evasion = 5
        self.b_speed = 8
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
        c.speed = self.b_speed
        c.evasion = self.b_evasion
        c.hit = self.b_hit
        c.luck = self.b_luck

        # FF9: http://finalfantasy.wikia.com/wiki/HP
        # [Str * HPMod(Level) / 50]
        c.max_hp = floor(c.strength * bp.HPMOD[c.level] / 50)
        c.hp = c.max_hp

        # Возвращаемый опыт = планка опыта для следующего уровня,
        # деленное на значение текущего уровня умноженное на 4
        # TODO: доработать формулу получения возвращаемого опыта
        c.gives_exp = c.exp_next_level() // (c.level * 4)

        c.name = self.name if not c.name else c.name
        c.desc = self.desc if not c.desc else c.desc


# #### Основные типы персонажей #####
# Ссылка: http://ru.rpg.wikia.com/wiki/Тип_существа

class Plants(BaseType):
    """Тип Растения"""

    def __init__(self):
        super().__init__()

        self.name_type = "Растения"
        self.desc = ("Обычные растения, а также монстры растительного происхождения. Для игровых целей "
                     "сюда же попадают грибы, плесень и создания схожей основы.")


# http://ru.rpg.wikia.com/wiki/Животные
class Beast(BaseType):
    """Тип Звери"""

    def __init__(self):
        super().__init__()

        self.name_type = "Звери"
        self.desc = ("Естественные существа фентезийных миров. Обычные животные, "
                     "а также динозавры, гигантские варианты животных и схожие существа")


# http://ru.rpg.wikia.com/wiki/Гуманоиды
class Humanoids(BaseType):
    """Тип Гуманоиды"""

    def __init__(self):
        super().__init__()

        self.name_type = "Гуманоиды"
        self.desc = ("Представители типовых разумных видов среднего "
                     "фентези-мира: эльфы, орки, люди и подобные существа.")

        self.b_speed = 10

    def do_calc_stats(self, c):
        """Переопределенная функция выполняет подсчет статов гуманоидов"""
        BaseType.do_calc_stats(self, c)

        # Добавим собственное правило для гуманоидов:
        # шанс уклонения повышается на 1 за каждые 20 уровней персонажа
        c.evasion = self.b_evasion + c.level // 20


# http://ru.rpg.wikia.com/wiki/Великаны
class Giants(BaseType):
    """Тип Великаны (Гиганты)"""

    def __init__(self):
        super().__init__()

        self.name_type = "Великаны"
        self.desc = ("Существа, подобные крупным гуманоидам, но образующие отдельную группу характерных "
                     "видов: огры, эттины, настоящие великаны разных видов.")


class Fey(BaseType):
    """Тип Феи"""

    def __init__(self):
        super().__init__()

        self.name_type = "Феи"
        self.desc = "Тесно связанные с силами природы существа, имеющие обычно магические способности."


class Oozes(BaseType):
    """Тип Слизи"""

    def __init__(self):
        super().__init__()

        self.name_type = "Слизи"
        self.desc = "Желеобразные и текучие существа без чёткой формы."


class Constructs(BaseType):
    """Тип Конструкторы"""

    def __init__(self):
        super().__init__()

        self.name_type = "Конструкторы"
        self.desc = "Механизмы, големы и иные создания, создаваемые искусственно из неодушевлённой материи."


class Aberrations(BaseType):
    """Тип Отродья"""

    def __init__(self):
        super().__init__()

        self.name_type = "Отродья"
        self.desc = ("Чуждые миру существа, обладающие крайне нечеловеческим разумом и неестественным "
                     "с точки зрения природы телом.")


# http://ru.rpg.wikia.com/wiki/Нежить
class Undead(BaseType):
    """Тип Нежить"""

    def __init__(self):
        super().__init__()

        self.name_type = "Нежить"
        self.desc = "Оживлённые останки существ или неупокоенные духи"
        self.race = "Нежить"


# http://ru.rpg.wikia.com/wiki/Драконы
class Dragons(BaseType):
    """Тип Драконы"""

    def __init__(self):
        super().__init__()

        self.name_type = "Драконы"
        self.desc = "Все разновидности одного из характернейших монстров игры и связанных с ними существ."


class Celestials(BaseType):
    """Тип Небожители"""

    def __init__(self):
        super().__init__()

        self.name_type = "Небожители"
        self.desc = "Существа, характерные для Верхних планов, ангельские создания."


class Fiends(BaseType):
    """Тип Демоны"""

    def __init__(self):
        super().__init__()

        self.name_type = "Демоны"
        self.desc = "Их аналог для Нижних планов, всевозможные создания зла."


# http://ru.rpg.wikia.com/wiki/Элементали
class Elementals(BaseType):
    """Тип Элементали"""

    def __init__(self):
        super().__init__()

        self.name_type = "Элементали"
        self.desc = "Стихийные создания."


class Monstrosities(BaseType):
    """Тип Чудовища"""

    def __init__(self):
        super().__init__()

        self.name_type = "Чудовища"
        self.desc = "Результаты магических экспериментов, уникальные монстры, жертвы проклятий и пр."