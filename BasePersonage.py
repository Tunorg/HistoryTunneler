"""BasePersonage.py: Модуль содержит базовый класс персонажей"""

__author__ = 'ipetrash'


from math import floor
from random import randint, randrange


# Индекс -- уровень, значение -- базовое здоровье для данного уровня
# Первый индекс 0, всегда будет игнорироваться (т.к. уровень начинается с 1)
# FF9: http://finalfantasy.wikia.com/wiki/HP
HPMOD = [
    0,
    250, 314, 382, 454, 530, 610, 694, 782, 874, 970, 1062, 1150, 1234, 1314, 1390,
    1462, 1530, 1594, 1662, 1734, 1810, 1890, 1974, 2062, 2154, 2250, 2350, 2454, 2562,
    2674, 2790, 2910, 3034, 3162, 3282, 3394, 3498, 3594, 3682, 3762, 3834, 3898, 3958,
    4014, 4066, 4114, 4158, 4198, 4234, 4266, 4288, 4294, 4317, 4334, 4344, 4353, 4361,
    4368, 4374, 4379, 4383, 4386, 4388, 4389, 4390, 4391, 4392, 4393, 4394, 4395, 4396,
    4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4409, 4410,
    4411, 4412, 4413, 4414, 4415, 4416, 4417, 4418, 4419, 4420, 4421, 4422, 4423, 4424,
    4524,
]

# Таблица опыта: индекс -- уровень, значение -- нужное количество опыта для получения данного уровня
# FF5: http://finalfantasy.wikia.com/wiki/HP
# Первый индекс 0, всегда будет игнорироваться (т.к. уровень начинается с 1)
EXPS = [
    0,
    0, 10, 33, 74, 140, 241, 389, 599, 888, 1276, 1786, 2441, 3269, 4299, 5564, 7097, 8936,
    11120, 13691, 16693, 20173, 24180, 28765, 33983, 39890, 46546, 54012, 62352, 71632,
    81921, 93291, 105815, 119569, 134633, 151087, 169015, 188503, 209640, 232517, 257227,
    283867, 312534, 343330, 376357, 411722, 449533, 489900, 532937, 578759, 627485, 679235,
    734131, 792300, 853869, 918969, 987732, 1060294, 1136793, 1217368, 1302163, 1391323,
    1484995, 1583329, 1686478, 1794597, 1907843, 2026376, 2150358, 2279955, 2415333, 2556663,
    2704116, 2857867, 3018093, 3184974, 3358692, 3539432, 3727380, 3922726, 4125661, 4336381,
    4555081, 4781961, 5017223, 5261071, 5513712, 5775354, 6046210, 6326493, 6616420, 6916210,
    7226084, 7546266, 7876982, 8218461, 8570934, 8934635, 9309800, 9696668,
]

# # Таблица роста: кортеж, чей индекс это уровень, а значение -- пары значений: здоровье и опыт
# TABLE_GROWTH = tuple(zip(HPMOD, EXPS))
# for i, (hp, exps) in enumerate(TABLE_GROWTH):
#      print("Уровень {0:2d}: HP: {1:4d}, EXP: {2:}".format(i, hp, exps))


# Максимальный уровень
MAX_LEVEL = len(EXPS) - 1

DEBUG_MODE = True
DEBUG_MODE_GET_SET = True


class Evasion:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
            print("    __get__: self: {}, instance: {}, owner: {}  "
                  "value: {}".format(self, type(instance), type(owner), instance.d_evasion))

        return instance.d_evasion

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, value: {}".format(self, type(instance), value))

        if value > 100:
            value = 100
        instance.d_evasion = value


class MaxHP:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
            print("    __get__: self: {}, instance: {}, owner: {}  "
                  "value: {}".format(self, type(instance), type(owner), instance.d_max_hp))
        return instance.d_max_hp

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, value: {}".format(self, type(instance), value))

        hp_was_max = instance.hp == instance.d_max_hp
        instance.d_max_hp = value
        if hp_was_max:
            instance.hp = instance.d_max_hp


class HP:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
            print("    __get__: self: {}, instance: {}, owner: {}  "
                  "value: {}".format(self, type(instance), type(owner), instance.d_hp))

        return instance.d_hp

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, "
                  "value: {}".format(self, type(instance), value))

        if instance.dead and value > 0:
            instance.d_hp = 0

            if DEBUG_MODE:
                print("Лечение {0} не принесло эффекта, потому что {0} мертв!".format(instance.name))

        if value < 0:  # Здоровье не может быть меньше 0
            instance.dead = True
            value = 0

        if value > instance.max_hp:  # Здоровье не может быть больше максимального
            value = instance.max_hp

        instance.d_hp = value


class Dead:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
            print("    __get__: self: {}, instance: {}, owner: {}  "
                  "value: {}".format(self, type(instance), type(owner), instance.d_dead))

        return instance.d_dead

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, "
                  "value: {}".format(self, type(instance), value))

        instance.d_dead = value
        if instance.d_dead:
            if instance.hp != 0:
                instance.hp = 0

            # if DEBUG_MODE:
            #     print("{} мертв!".format(instance.name))


class Exp:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
            print("    __get__: self: {}, instance: {}, owner: {} "
                  "value: {}".format(self, type(instance), type(owner), instance.d_exp))

        return instance.d_exp

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, value: {}".format(self, type(instance), value))

        if value < instance.d_exp:
            print("Опыт не может быть отрицательным!")
            return

        if DEBUG_MODE:
            print("\nДобавлен опыт: {}".format(value - instance.d_exp))

        instance.d_exp = value

        def has_level_up(level, exp):
            if level >= MAX_LEVEL:  # Уровень не может превышать максимальный
                return False
            if EXPS[level + 1] - exp <= 0:  # Если набрали достаточное количество опыта для level-up'а
                return True
            return False

        # Пока возможно получать уровень
        while has_level_up(instance.level, instance.d_exp):
            instance.level_up()

        if DEBUG_MODE:
            if instance.level == MAX_LEVEL:
                print(" Достигнут максимальный уровень: {}".format(MAX_LEVEL))
            else:
                print(" Опыта: {}, уровень: {}, до следующего "
                      "уровня осталось опыта: {}\n".format(instance.d_exp, instance.level, instance.need_exp()))


class Level:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
            print("    __get__: self: {}, instance: {}, owner: {}  "
                  "value: {}".format(self, type(instance), type(owner), instance.d_level))

        return instance.d_level

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, "
                  "value: {}".format(self, type(instance), value))

        if instance.d_level == value:
            if DEBUG_MODE:
                print("Уровень не изменился")
            return

        instance.d_level = value
        if instance.d_level > MAX_LEVEL:
            instance.d_level = MAX_LEVEL  # Уровень не может быть выше максимального, потому уменьшим до MAX_LEVEL

            if DEBUG_MODE:
                print(("Превышение максимального уровня {} ({} lvl{})!".format(MAX_LEVEL, instance.name, instance.d_level)))

        # Нет смысла показывать данное сообщение, если у нас начальный уровень
        if DEBUG_MODE:
            if instance.d_level > 1:
                print(" Уровень повысился! Уровень:", instance.d_level)

        if instance.exp < EXPS[instance.d_level]:  # "подгонка" опыта под уровень
            instance.exp = EXPS[instance.d_level]

        # Выполним пересчет статов
        # Пересчет статов также восстановит здоровье до максимального
        instance.update_states()


class DType:
    def __get__(self, instance, owner):
        if DEBUG_MODE_GET_SET:
                print("    __get__: self: {}, instance: {}, owner: {} "
                      "value: {}".format(self, type(instance), type(owner), instance.d_type))

        return instance.d_type

    def __set__(self, instance, value):
        if DEBUG_MODE_GET_SET:
            print("  __set__: self: {}, instance: {}, value: {}".format(self, type(instance), value))

        if instance.d_type != value:
            instance.d_type = value

            # Выполним пересчет статов
            instance.update_states()


from BaseType import BaseType


class Personage:
    """Общий класс для персонажей."""

    def __init__(self, ptype=BaseType()):
        self.name = None
        self.desc = None

        self.d_evasion = 0
        self.d_max_hp = 0
        self.d_hp = 0
        self.d_dead = False
        self.d_exp = 0
        self.d_level = 1
        self.d_type = ptype
        self.update_states()

        # TODO: добавление опыта при убийстве противника
        # TODO: может замутить формулу, в которой будут завязаны статы и уровень противника и наш текущий уровень?
        self.gives_exp = 0  # содержит количество опыта, которая даст персонаж, когда его убьют

    atk = 0
    strength = 0
    vitality = 0
    evasion = Evasion()
    speed = 0
    hit = 0
    luck = 0

    max_hp = MaxHP()
    hp = HP()
    dead = Dead()
    exp = Exp()
    level = Level()
    type = DType()

    def update_states(self):
        """Выполнение пересчета статов"""
        self.d_type.do_calc_stats(self)

    def level_up(self):
        self.level += 1

    # TODO: добавление опыта при убийстве противника
    def attack_to(self, other):
        """Функция атаки персонажей."""

        # Определим попали ли по противнику
        # Hit% = (Luck Атакующего / 2 + Hit Атакующего — Eva Цели — Luck Цели)
        percent = self.luck / 2 + self.hit - other.evasion - other.luck  # Подсчет шанса в процентах, %
        percent = floor(percent)  # Округление до целого
        has_hit = randrange(0, 100) < percent  # Эмитация шанса попадания

        if DEBUG_MODE:
            print("{}({}) хочет ударить {}({}) "
                  "(шанс попасть: {}%).".format(self.name, self.level,
                                                other.name, other.level,
                                                percent))

        if has_hit:
            # Подсчитаем урон, который нанесем противнику
            # формула взята из (FF7): http://finalfantasy.wikia.com/wiki/Attack_(Command)
            power = self.strength
            defence = other.vitality  # живучесть -- по сути защита
            base_dmg = self.atk + ((self.atk + self.level) / 32) * ((self.atk * self.level) / 32)
            max_dmg = ((power * (512 - defence)) * base_dmg) / (16 * 512)
            dmg = max_dmg * (3841 + randint(0, 255)) / 4096
            dmg = floor(dmg)

            # Подсчитаем шанс нанести критический удар
            # FF7: http://finalfantasy.wikia.com/wiki/Critical_Hit
            has_crit = (self.luck + self.level - other.level) / 4
            rnd = (randint(0, 65535) * 99 / 65535) + 1
            has_crit = floor(has_crit)
            has_crit = has_crit >= rnd

            dmg = dmg * 2 if has_crit else dmg
            other.hp -= dmg  # вычесть из текущего здоровья урон

            if DEBUG_MODE:
                print(" {}({}) нанес {}({}){}: "
                      "{} урон!".format(self.name, self.level, other.name, other.level,
                                        " критический удар" if has_crit else "",
                                        dmg))
                if other.dead:
                    print(" {} мертв!".format(other.name))
                else:
                    print(" Осталось hp: {}".format(other.hp))
        else:
            if DEBUG_MODE:
                print(" {}({}) промахнулся по {}({})!".format(self.name, self.level, other.name, other.level))

    def exp_next_level(self):
        """Функция возвращает предел опыта следующего уровня"""
        if self.level != MAX_LEVEL:  # Если текущий уровень не максимальный
            # возвращаем предел количества опыта для получения следующего уровня
            return EXPS[self.level + 1]
        else:
            # персонаж достиг максимального уровня, потому получение опыта через
            # таблицу опыта не имеет смысла, т.к. текущий набранный опыт и будет равен
            # значению таблицы для последнего уровеня
            return self.exp

    def need_exp(self):
        """Функция возвращает количество опыта, оставшееся до следующего уровня."""
        # Предел опыта для следующего уровня - текущий набранный опыт:
        return self.exp_next_level() - self.exp

    def __repr__(self):
        levels = "lvl: {} ({}/{}{})".format(self.level, self.exp, self.exp_next_level(),
                                            ", до следующего: {}".format(self.need_exp())
                                            if self.level < MAX_LEVEL else "")
        heredity = "(общий тип: {}, имя типа: {}, раса: {})".format(self.type.name_type, self.type.name,
                                                                    self.type.race)
        stats = ("\n\t\tСтаты: hp: {}/{}, str: {}, atk: {}, vit: {}, spd: {}. eva: {}%, "
                 "hit: {}%, luck: {}".format(self.hp, self.max_hp, self.strength, self.atk, self.vitality,
                                             self.speed, self.evasion, self.hit, self.luck))
        return "{} {} {} {}".format(self.name, levels, heredity, stats)
