__author__ = 'ipetrash'

from math import floor
from random import randint, randrange
import Type


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


# TODO: Хорошо бы интерфейс или абстракный сделать, чтоб нагляднее выглядел класс персонажа
# Сейчас же, класс персонажа напоминает вермишель


class BaseCharacter:
    """Общий класс для персонажей."""

    __exp = 0
    def get_exp(self):
        return self.__exp
    def set_exp(self, value):
        if value < self.exp:
            print("Опыт не может быть отрицательным!")
            return

        if DEBUG_MODE:
            print("\nДобавлен опыт: {}".format(value - self.__exp))

        self.__exp = value

        def has_level_up(level, exp):
            if level >= MAX_LEVEL:  # Уровень не может превышать максимальный
                return False
            if EXPS[level + 1] - exp <= 0:  # Если набрали достаточное количество опыта для level-up'а
                return True
            return False

        # Пока возможно получать уровень
        while has_level_up(self.level, self.__exp):
            # self.level += 1
            self.level_up()

        if DEBUG_MODE:
            if self.level == MAX_LEVEL:
                print(" Достигнут максимальный уровень: {}".format(MAX_LEVEL))
            else:
                print(" Опыта: {}, уровень: {}, до следующего "
                      "уровня осталось опыта: {}\n".format(self.exp, self.level, EXPS[self.level + 1] - self.exp))

    exp = property(get_exp, set_exp, doc="Текущий набранный опыт персонажа")

    __level = 1
    def get_level(self):
        return self.__level
    def set_level(self, value):
        if self.__level == value:
            if DEBUG_MODE:
                print("Уровень не изменился")
            return

        if self.__level > value:
            if DEBUG_MODE:
                print("\nЧто за черт? Уровень не может уменьшиться: "
                      "текущий уровень {}, устанавливаемый: {}\n".format(self.__level, value))
            return

        self.__level = value
        if self.__level > MAX_LEVEL:
            self.__level = MAX_LEVEL  # Уровень не может быть выше максимального, потому уменьшим до MAX_LEVEL
            if DEBUG_MODE:
                print(("Превышение максимального уровня {} ({} lvl{})!".format(MAX_LEVEL, self.name, self.level)))

        # Нет смысла показывать данное сообщение, если у нас начальный уровень
        if DEBUG_MODE:
            if self.__level > 1:
                print(" Уровень повысился! Уровень:", self.__level)

        if self.exp < EXPS[self.__level]:  # "подгонка" опыта под уровень
            self.exp = EXPS[self.__level]

        # Выполним пересчет статов
        # self.type.do_calc_stats(self)
        self.update_states()

        # После получения нового уровня, персонаж восстанавлиет здоровье до максимального
        self.hp = self.max_hp
    level = property(get_level, set_level)

    __type = Type.BaseType()
    def get_type(self):
        return self.__type
    def set_type(self, value):
        if self.__type == value:
            return
        self.__type = value

        # Выполним пересчет статов
        # self.type.do_calc_stats(self)
        self.update_states()
    type = property(get_type, set_type)


    def update_states(self):
        """Выполнение пересчета статов"""
        self.__type.do_calc_stats(self)


    __dead = False
    def get_dead(self):
        return self.__dead
    def set_dead(self, value):
        self.__dead = value
        if self.dead:
            if self.hp != 0:
                self.hp = 0
            if DEBUG_MODE:
                print("{} мертв!".format(self.name))
    dead = property(get_dead, set_dead)


    __max_hp = 0
    def get_max_hp(self):
        return self.__max_hp
    def set_max_hp(self, value):
        hp_was_max = self.hp == self.__max_hp
        self.__max_hp = value
        if hp_was_max:
            self.hp = self.__max_hp
    max_hp = property(get_max_hp, set_max_hp)


    __hp = 0
    def get_hp(self):
        return self.__hp
    def set_hp(self, value):
        if self.dead and value > 0:
            self.__hp = 0
            if DEBUG_MODE:
                print("Лечение {0} не принесло эффекта, потому что {0} мертв!".format(self.name))
        if value < 0:  # Здоровье не может быть меньше 0
            self.dead = True
            value = 0
        if value > self.max_hp:  # Здоровье не может быть больше максимального
            value = self.max_hp
        self.__hp = value
    hp = property(get_hp, set_hp, doc="Hit points")


    atk = 0
    strength = 0
    vitality = 0

    __evasion = 0

    def get_evasion(self):
        return self.__evasion

    def set_evasion(self, value):
        if value > 100:
            value = 100
        self.__evasion = value

    evasion = property(get_evasion, set_evasion, doc="Шанс уклонения")

    hit = 0
    luck = 0

    name = "???"
    description = "???"

    # TODO: реализовать использование ap
    # ap = 0  # очки мастерства, используемые для прокачки навыков (Ability Points)


    def level_up(self):
        self.level += 1

    def attack_to(self, other):
        """Функция атаки персонажей."""

        # Определим попали ли по противнику
        # Hit% = (Luck Атакующего / 2 + Hit Атакующего — Eva Цели — Luck Цели)
        percent = self.luck / 2 + self.hit - other.evasion - other.luck  # Подсчет шанса в процентах, %
        percent = floor(percent)  # Округление до целого
        has_hit = randrange(0, 100) < percent  # Эмитация шанса попадания

        if DEBUG_MODE:
            print("\nШанс попасть: {}%: {}".format(percent, has_hit))

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

            other.hp -= dmg * 2 if has_crit else dmg  # вычесть из текущего здоровья урон

            if DEBUG_MODE:
                if has_crit:
                    print("{}({}) нанес {}({}) критический удар: "
                          "{} урон!".format(self.name, self.level, other.name, other.level, dmg * 2), end="")
                else:
                    print("{}({}) нанес {}({})"
                          " {} урона!".format(self.name, self.level, other.name, other.level, dmg), end="")

                print(" Осталось hp: {}".format(other.hp))

        else:
            if DEBUG_MODE:
                print("{}({}) промахнулся по {}({})!".format(self.name, self.level, other.name, other.level))


    def __repr__(self):
        return ("{} lvl: {} (общий тип: {}, имя типа: {}, раса: {}), stats: hp: {}/{}, str: {}, atk: {}, "
                "vit: {}, eva: {}, hit: {}%, luck: {}".format(self.name, self.level, self.type.name_type,
                                                              self.type.name, self.type.race, self.hp, self.max_hp,
                                                              self.strength, self.atk, self.vitality, self.evasion,
                                                              self.hit, self.luck))

