__author__ = 'ipetrash'

from math import floor
from random import randint, randrange


MAX_HIT_POINTS = 9999


class Character:
    """Общий класс для персонажей."""

    level = 0  # уровень
    exp = 0  # текущее количество опыта
    ap = 0  # очки мастерства, используемые для прокачки навыков (Ability Points)

    __max_hp = 0
    def get_max_hp(self):
        return self.__max_hp
    def set_max_hp(self, value):
        if value < 0:
            value = 0
        if value > MAX_HIT_POINTS:  # Максимальное здоровье не может быть больше MAX_HIT_POINTS
            value = MAX_HIT_POINTS
        self.__max_hp = value
        self.hp = value
    max_hp = property(get_max_hp, set_max_hp, doc="Max hit points")

    __hp = 0
    def get_hp(self):
        return self.__hp
    def set_hp(self, value):
        if value < 0:  # Здоровье не может быть меньше 0
            value = 0
        if value > self.__max_hp:  # Здоровье не может быть больше максимального
            value = self.__max_hp
        self.__hp = value
    hp = property(get_hp, set_hp, doc="Hit points")

    strength = 0
    vit = 0
    mag = 0
    spr = 0
    spd = 0
    eva = 0
    hit = 0
    luck = 0

    name = "???"
    description = "???"
    atk = 0  # урон оружия

    def __repr__(self):
        return "{} lvl: {} hp: {} / {}".format(self.name, self.level, self.hp, self.max_hp)

    def attack_to(self, other):
        """Функция атаки персонажей."""

        # Определим попали ли по противнику
        # Hit% = (Luck Атакующего / 2 + Hit Атакующего — Eva Цели — Luck Цели)
        percent = self.luck / 2 + self.hit - other.eva - other.luck
        percent = floor(percent)
        has_hit = randrange(0, 100) < percent

        print()
        print("Шанс попасть: {}%: {}".format(percent, has_hit))

        if has_hit:
            # Подсчитаем урон, который нанесем противнику
            # формула взята из (FF7): http://finalfantasy.wikia.com/wiki/Attack_(Command)
            power = self.strength
            defence = other.vit
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