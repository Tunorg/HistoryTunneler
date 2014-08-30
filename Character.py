__author__ = 'ipetrash'

from math import floor
from random import randint, randrange


# Index as level, value base hp
# FF9: http://finalfantasy.wikia.com/wiki/HP
HPMOD = [
    0, 250, 314, 382, 454, 530, 610, 694, 782, 874, 970, 1062, 1150, 1234, 1314, 1390,
    1462, 1530, 1594, 1662, 1734, 1810, 1890, 1974, 2062, 2154, 2250, 2350, 2454, 2562,
    2674, 2790, 2910, 3034, 3162, 3282, 3394, 3498, 3594, 3682, 3762, 3834, 3898, 3958,
    4014, 4066, 4114, 4158, 4198, 4234, 4266, 4288, 4294, 4317, 4334, 4344, 4353, 4361,
    4368, 4374, 4379, 4383, 4386, 4388, 4389, 4390, 4391, 4392, 4393, 4394, 4395, 4396,
    4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4409, 4410,
    4411, 4412, 4413, 4414, 4415, 4416, 4417, 4418, 4419, 4420, 4421, 4422, 4423, 4424,
    4524,
]

class DeadException(Exception):
    def __init__(self, character):
        self.character = character
    def __repr__(self):
        return "{} мертв!".format(self.character.name)
    def __str__(self):
        return self.__repr__()


class HealWhenDeadException(Exception):
    def __init__(self, character):
        self.character = character
    def __repr__(self):
        return "Лечение {0} не принесло эффекта, потому что {0} мертв!".format(self.character.name)
    def __str__(self):
        return self.__repr__()


class Character:
    """Общий класс для персонажей."""

    level = 0  # уровень
    exp = 0  # текущее количество опыта
    ap = 0  # очки мастерства, используемые для прокачки навыков (Ability Points)

    __dead = False
    def get_dead(self):
        return self.__dead
    def set_dead(self, value):
        self.__dead = value
        if self.dead:
            if self.hp != 0:
                self.hp = 0
            raise DeadException(self)
    dead = property(get_dead, set_dead)

    __max_hp = 0
    def get_max_hp(self):
        # FF9: http://finalfantasy.wikia.com/wiki/HP
        # [Str * HPMode(Level) / 50]
        self.__max_hp = floor(self.strength * HPMOD[self.level] / 50)
        return self.__max_hp
    def set_max_hp(self, value):
        self.hp = value
    max_hp = property(get_max_hp, set_max_hp, doc="Max hit points")

    __hp = 0
    def get_hp(self):
        return self.__hp
    def set_hp(self, value):
        if self.dead and value > 0:
            self.__hp = 0
            raise HealWhenDeadException(self)
        if value < 0:  # Здоровье не может быть меньше 0
            self.dead = True
            value = 0
        if value > self.__max_hp:  # Здоровье не может быть больше максимального
            value = self.__max_hp
        self.__hp = value
    hp = property(get_hp, set_hp, doc="Hit points")

    __strength = 0
    def get_strength(self):
        return self.__strength
    def set_strength(self, value):
        if value < 0:
            value = 0
        self.__strength = value
    strength = property(get_strength, set_strength, doc="Strength")

    vitality = 0
    # magic = 0
    # spirit = 0
    # speed = 0
    evasion = 0
    hit = 0
    luck = 0

    name = "???"
    description = "???"
    atk = 0  # урон оружия

    def __repr__(self):
        return "{} lvl: {}, hp: {}/{}, str: {}".format(self.name, self.level, self.hp, self.max_hp, self.strength)

    def attack_to(self, other):
        """Функция атаки персонажей."""

        # Определим попали ли по противнику
        # Hit% = (Luck Атакующего / 2 + Hit Атакующего — Eva Цели — Luck Цели)
        percent = self.luck / 2 + self.hit - other.evasion - other.luck
        percent = floor(percent)
        has_hit = randrange(0, 100) < percent

        print()
        print("Шанс попасть: {}%: {}".format(percent, has_hit))

        if has_hit:
            # Подсчитаем урон, который нанесем противнику
            # формула взята из (FF7): http://finalfantasy.wikia.com/wiki/Attack_(Command)
            power = self.strength
            defence = other.vitality
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

            other.hp -= dmg

            if has_crit:
                print("{}({}) нанес {}({}) критический удар: {} урон!".format(self.name, self.level, other.name,
                                                                              other.level, dmg * 2), end="")
            else:
                print("{}({}) нанес {}({}) {} урона!".format(self.name, self.level, other.name,
                                                             other.level, dmg), end="")

            print(" Осталось hp: {}".format(other.hp))

        else:
            print("{}({}) промахнулся по {}({})!".format(self.name, self.level, other.name, other.level))