__author__ = 'ipetrash'



# class States:
#     """Общий класс описывающий статы персонажей."""
#     def __init__(self):
#         pass
#
#     # Статы и формулы рассчета статов некоторых игр FF
#     # http://finalfantasy.wikia.com/wiki/Stats
#
#     # Характеристики в FF8
#     # http://squarefaction.ru/game/final-fantasy-viii/articles/10480-parametry-geroev-v-final-fantasy-viii
#
#     # Характеристики в FF7
#     # http://ffforever.info/index.cgi?section=ff7cc;p=experience
#     # http://www.ign.com/faqs/2004/final-fantasy-vii-stat-building-faq-452504
#
#     # Характеристики в FF6
#     # http://www.cavesofnarshe.com/ff6/stats.php
#
#     # Статы в FF9
#     # http://letao.is-a-geek.net/ff9stats/
#
#     # Полезные и просто интересные ссылки:
#     # http://ru.rpg.wikia.com/wiki/%D0%90%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B
#     # http://ru.rpg.wikia.com/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B8%D1%87%D0%BD%D1%8B%D0%B5_%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8
#     # http://ru.rpg.wikia.com/wiki/%D0%A5%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0
#     # Сила (ST), Ловкость (DX), Интеллект (IQ), Здоровье (HT)
#     # st = 0  # strength / сила
#     # ht = 0  # health / здоровье
#     # dx = 0  # dexterity / ловкость
#     # iq = 0  # intellect / интеллект
#     #
#     # dm = 0  # damage / повреждение
#     # critical = 0  # chance to deal critical / шанс нанести крит
#     # hp = 0  # hit point
#     # max_hp = 0
#     # # health = 0
#     # # max_health = 0
#
#     level = 0  # уровень
#     exp = 0  # текущее количество опыта
#     ap = 0  # очки мастерства, используемые для прокачки навыков (Ability Points)
#
#     # Статы взяты из:
#     # http://squarefaction.ru/game/final-fantasy-viii/articles/10480-parametry-geroev-v-final-fantasy-viii
#     hp = 0  # Hit Points (НР) - параметр, показывающий количество единиц Жизненной Силы персонажа. Если он
#               снизится до «0», то герой
#             # попадёт в нокдаун (статус КО — Knocked Out). Если все бойцы нашего отряда окажутся в нокауте, игра
#             # закончится поражением. Ещё одна важнейшая функция Жизненной Силы — активация сверх-способностей героев
#             # Limit Breaks. Принцип тут прост — чем ниже уровень НР, тем выше шансы на активацию в бою у
#             # персонажей «Лимитных Атак».
#     strength = 0  # Strength (Str) Физическая Сила персонажа. Напрямую влияет на урон, наносимый противникам в бою
#               с помощью стандартных
#              # Атак. Чем выше уровень Физической Силы, тем больше очков Жизненной Силы будет снято с врага.
#              # Трёхкратное увеличение параметра Strength даст семикратную прибавку к Урону от физических ударов.
#              # Дополнительно достаточно весомое влияние размер Физической Силы оказывает и на так называемую
#              # «Статусную Атаку».
#     vit = 0  # Vitality (Vit) Живучесть персонажа. Даёт в бою защиту от физических ударов, правда, в начале игры её
#               эффективность
#              # не столь высока, но в отдельных поединках данный параметр вполне способен склонить чашу весов в нашу
#              # сторону. По мере развития персонажей, возрастает и роль Живучести. С середины Прохождения начинает
#              # действовать правило — если величина параметра Vitality у героя равна или больше параметра Strength
#              # противника и близка к максимальному значению, то полученные физические повреждения минимальны.
#     mag = 0  # Magic (Mag) Магическая Сила персонажа. Напрямую влияет на величину Магического Урона, а также
#               эффективность
#              # действий Статусных и лечебных заклинаний. Кроме того, от величины Магической Силы во многом зависит
#              # эффективность работы Команды Draw, с помощью которой герои вытягивают из противников в бою
#              # магические заклинания.
#     spr = 0  # Spirit (Spr) Духовная Сила персонажа. Предоставляет в бою защиту от действий магических заклинаний
#               противников.
#              # В начале игры эффективность работы этого параметра не так заметна, тем не менее, в ряде сражений
#              # именно Духовная Сила может внести один из главных вкладов в общую победу. По мере развития персонажей,
#              # возрастает и роль Духовной Силы. С середины Прохождения начинает действовать правило — если величина
#              # параметра Spirit у героя равна или больше параметра Magic противника и близка к максимальному значению,
#              # то полученные магические повреждения минимальны.
#     spd = 0  # Speed (Spd) Скорость персонажа. Напрямую влияет на интенсивность действий героя в бою. Чем сильнее
#               развит
#              # этот параметр, тем чаще будет получать свой ход герой в поединках с врагами. Это преимущество, в
#              # свою очередь, даёт возможность нанести противнику первый удар, а в длительных сражениях позволяет
#              # увеличить количество произведённых действий. Поднятие параметра Speed в три с половиной раза даст
#              # герою одно дополнительное действие за тот же самый промежуток времени. Помимо этого Скорость оказывает
#              # прямое воздействие на следующий параметр — Evasion (Eva)
#     eva = 0  # Evasion (Eva) Уклонение. С помощью этого параметра персонажи имеют возможность в бою уворачиваться от
#               физических
#              # Атак противников. Одной из важнейших особенностей параметра Уклонение является тот факт, что герои не
#              # владеют ею даже на самом минимальном уровне. Эта способность исключительно приносная. Как мы уже
#              # заметили выше, на её повышение влияет другой параметр — Speed. Чем выше у нашего персонажа Скорость,
#              # тем выше у него Уклонение от вражеских Атак.(Evasion)
#     hit = 0  # Hit Percentage (Hit) Точность. Параметр, влияющий на успешность проведения физической Атаки
#               персонажа. При маленьких
#              # значениях Точности возможно большое количество промахов, а при максимальном значении в 255% физические
#              # удары будут всегда достигать цели. Параметр Нit внешний и является исключительно атрибутом оружия героев
#     luck = 0  # Удача. Один из самых многогранных и недооцениваемых параметров в арсенале персонажей. Он оказывает
#               # весьма немалое влияние на множество происходящих в бою процессов. Прежде всего от Удачи зависит
#               # вероятность нанесения двукратного критического урона во время проведения физической Атаки. Свой,
#               # пусть и не столь большой, вклад параметр Luck вносит и в общую вероятность проведения физической
#               # Атаки, а также уклонения героями от аналогичных Атак противника. Наконец, существует мнение, что
#               # благодаря высоким показателям параметра Удача, существенно повышается вероятность появления на поле
#               # боя Стражей Одина и Гильгамеша, и куда в большей степени нам достанутся в качестве победных трофеев
#               # редкие предметы.


    # # урон, который будет нанесен противнику
    # # DamageA = AttackerStr^2 / 16 + AttackerStr
    # # DamageB = DamageA * (265 - TargetVit) / 256
    # # Damage = DamageB * Power / 16
    # Power = 20
    # dmg = (((strength * strength) / 16 + strength) * (265 - other.vit) / 256) * Power / 16

## source: http://squarefaction.ru/game/final-fantasy-viii/articles/10480-parametry-geroev-v-final-fantasy-viii
#     Расчёт базового Урона физической атаки:
#     a) Урон (I) = Str2 Атакующего / 16 + Str Атакующего
#     b) Урон (II) = Урон (I) * (265 — Vit Цели) / 256
#     c) Базовый Урон = Урон (II) * Сила Атаки / 16
#     Сила Атаки — параметр постоянный и равен 20 единицам,

# Этап №2. Расчёт модификаций Урона:
# а) Итоговый Урон = Урон * ([0..32] + 240) / 256
# С помощью этой формулы высчитывается воздействие на Итоговый урон переменной составляющей Random Mod. Как видно из
# формулы мы можем получить как прибавку к силе Урона, так и его уменьшение, правда размах этих изменений, прямо
# скажем, не велик, максимум — плюс или минус ~6,5%.

# b) Атака сзади = Урон * 2
# Тут всё прозаично — атака с тылу даст вам двукратный Урон, правда, повлиять на её появление в Final Fantasy VIII
# довольно сложно (только посредством Способности Alert). Не велика и вероятность запуская этой атаки — не
# больше ~ 7,8%.
#
# с) Berserk Mod = Урон * 1,5
# И в этой формуле нет ничего сложного — бойцы, находящиеся под действием заклинания Berserk, наносят своим врагам
# полуторный урон. Однако в этом случае мы полностью теряем контроль над персонажем, и он выбирает противников для
# проведения своих атак в случайном порядке.
#
# d) Критический Урон (Gunblade-тип) = Урон * 1,5
# В этой формуле идет расчёт Критического Урона для двух главных героев-антагонистов Final Fantasy VIII Скволла и
# Сейфера. В боях они используют свои уникальные мечи Gunblade, дополнительно стреляющие во врага патронами.
# При успешном попадании противнику будет нанесён полуторный урон. Для выстрела нужно сразу после того, как раздаётся
# свист меча в воздухе, нажать кнопку E (R1 на джойстике). С первого раза Критический выстрел, скорее всего,
# не получится, но постоянная практика даст игроку необходимую сноровку и, соответственно, в полтора раза больший
# урон главным героям игры. Тут всё зависит только от вас.
#
# e) Критический Урон (стандартный) = Урон * 2
# В этой формуле идет расчёт стандартного Критического Урона, который могут нанести все остальные персонажи игры.
# Формула показывает, что в определённых боях мы можем по существу удвоить итоговый Урон героя. Вот это круто,
# скажет новичок, но опытный геймер знает, что не всё так просто. Вероятность проведения Критического удара
# персонажами во многих играх довольна мала. Не стала исключением и Final Fantasy VIII. Расчёт вероятности запуска
# критического удара в этой игре ведётся по следующей формуле:
#
# Critical% = (Luck Атакующего + 1) / 256 * 100
# Попробуем спроецировать эту вероятность на второго персонажа игры Квисти (Quistis). С восьмого по двадцатый
# Уровень базовое значение параметра Удачи (Luck) у неё составляет 15 единиц. Таким образом, вероятность запуска
# Критического урона составит всего лишь ~6,5%. Совсем не густо…

## Hit% = (Luck Атакующего / 2 + Hit Атакующего — Eva Цели — Luck Цели)
# В случае наложения на персонажей статуса Darkness (Ослепление), значение параметра Hit мгновенно упадёт на 75%.


# http://squarefaction.ru/game/final-fantasy-viii/articles/9848-boevaya-sistema-final-fantasy-viii-chast-i
# Этап №3. Расчёт Элементального (Стихийного) бонуса:
# a) Бонус к Урону = Урон * Elem-Atk * (800 — Elem-Def) / 10000
# b) Итоговый Урон = Урон + Бонус к Урону


# Наложение Статуса % = (Str Атакующего / 4 — Vit Цели / 4) — ST-Def + ST-Atk
# Наложение Статуса % = (Mag Атакующего / 4 — Spr Цели / 4) — ST-Def + 200

# http://squarefaction.ru/game/final-fantasy-viii/articles/10016-boevaya-sistema-final-fantasy-viii-chast-ii
# Этап №1. Расчёт базового Урона Магической атаки:
# a) Урон (I) = Mag Атакующего + Сила Заклинания
# b) Урон (II) = Урон (I) * (265 — Spr Цели) / 4
# c) Базовый Урон = Урон (II) * Сила Заклинания / 256
#
# Этап №2. На этом этапе в дело вступает переменная составляющая Random Mod:
# Итоговый Урон = Базовый Урон * ([0..32] + 240) / 256


# 1. Начнём с лечебных заклинаний. Расчёт Силы лечебных заклинаний ведётся следующим образом:
# Целительная Сила = (Сила Заклинания + Mag Кастующего) * Сила Заклинания / 2

# 2. Следующее нестандартное и чрезвычайно интересное заклинание — Demi. Расчёт его Магического урона
# ведётся по следующей формуле:
# Магический Урон = HP Цели / 4


    # strength = 0  # сила
    # intellect = 0  # интеллект
    # agility = 0  # ловкость
    # luck = 0  # удача
    # vitality = 0  # живучесть
    # stamina = 0  # выносливость
    #
    #
    # magic_defense = 0  # магическая защита
    # accuracy = 0  # точность
    # speed = 0  # скорость
    # evasion = 0  # уклонение
    # magic_evasion = 0  # уклонение от магии
    # absorb = 0  # поглощение
    #
    #
    # attack_power = 0  # урон
    # critical = 0  # шанс нанести крит
    # hp = 0  # текущее здоровье
    # max_hp = 0  # максимальное здоровье
    # defense = 0  # зашита

### Types of Stats (source: http://finalfantasy.wikia.com/wiki/Stats)
# Level :   A unit's level is the character's defining point; it denotes how much it has in the other stats.
#           For example, a unit with a low level is considerably weaker than a high level unit. Levels are usually
#           measured one at a time, unless a considerable amount of experience /Ability Points are gained at one time.
#           Level also affects how much damage the user deals along with the other stats in most Final Fantasy games.
#           As the unit gains levels, the unit will gain more power in the stats outlined below. Final Fantasy II is an
#           exception to this rule.
#
# HP (Hit Points) : Hit Points are used to determine if a character is able to fight. When attacked, the total
#           damage dealt is subtracted from the current HP. When the character's current HP is 0, the character
#           faints and is unable to fight. Some items like Potions and most White Mage skills restore HP.
#           Phoenix Downs can revive a fainted unit, usually with a very small portion of their max HP.
#
# MP (Magic/Mana/Mist Points) : Magic or Mana Points are used when a character uses magic, or special skills.
#           Black, White, Blue, Red, and Time Mages usually use MP to utilize their skills. In some games,
#           MP is restored periodically, but sometimes items or rest stops are required.
#
# EXP (Experience Points) : Experience points are gained to raise the character's level. To level a character by one,
#           a certain amount of EXP is needed. This amount is rarely constant, as it grows each time the character
#           levels, usually twice the previous amount. Final Fantasy VIII is an exception, with the required EXP
#           staying constant throughout the game. Enemies grant EXP to the party when defeated, and generally,
#           Bosses may either give a huge amount, or none. The EXP received after a battle is usually shared by
#           the whole party, which is why if a character fights a monster alone, he would receive the same
#           experience as all of the characters together.
#
# AP (Ability Points) : Ability Points are gained when a battle is complete and won. In most games, AP is used and
#           gained to allow characters to master abilities. Generally, the stronger an opponent/group is, both in
#           level and class (eg: Minions VS. Bosses), the more AP the character gains. In some games, AP is used as
#           an alternative to Experience Points: when they reach a certain point, the character levels up by one.
#           Also in some games, like Final Fantasy X, a character is required to attack or otherwise uses an
#           Action to gain AP.
#
# Attack Power : Also known as ATK, Vigor, Attack, or Strength, Attack Power is used to indicate how strong a
#           character's Attack is. It is compared to the opponent's Defense to determine how much damage is
#           dealt, if any.
#
# Defense Power : also known as DEF or Defense, Defense Power is used to indicate how well defended the
#           character is against physical attacks. The higher Defense Power a character has, the less
#           damage he/she takes.
#
# Magic Power : Also known as MAG or Magic, Magic Power is used to indicate how strong a character's
#           magic skills are. It is compared to the opponent Magic Resistance to determine how much damage
#           is dealt, if any. For White Mages, it determines how much HP is restored.
#
# Magic Defense : Also known as Spirit or Magic Resistance, Magic Defense is used to determine how well
#           protected a character is against magic-based attacks. The stronger it is, the less damage the
#           character will take. In some games, Defense and Resistance are combined as one stat.
#
# Speed : Also known as SPD or Agility, Speed determines how fast a character's turn will come up in battle,
#           and how often. Time Mages can be used to alter Speed for one battle, with skills such as Stop,
#           Slow, Haste, and Quick (sometimes 'Quicken').
#
# Hit Rate : Also known as ACC or Accuracy, this stat will determine how often a units attacks will connect
#           with the target. Status ailments like Blind can reduce this stat.
#
# Magic Accuracy : Magic Accuracy, in the games where it is present, determines the likelihood that a unit will
#           successfully inflict damage or effect an enemy with a negative Status Effect .
#
# Evasion : This stat will indicate how often a unit can avoid an attack from an opponent. The higher an
#           evade stat is, the less a unit will be hit. Final Fantasy XII actually has more than one type
#           of evasion: shield evasion and weapon evasion, although the in-game menu combines them into one stat.
#
# Magic Evasion : Also known as MBlock, this stat will indicate how often a unit can avoid a magic attack.
#           In some games, Magic Evasion and Evasion are combined as one stat.
#
# Stamina : Stamina stat's purpose varies between the different Final Fantasy games.
#
# Absorb : A stat, which affects how much damage a character will take when hit by an enemy.
#
# Agility (Agl.) : A stat, which affects the stat Evade%. It is affected by the heaviness of the character's armor.
#
# Luck : Can affect many things, such as when a Critical Hit will land, steal success rate, evasion and accuracy.
#
# Vitality : Vitality stat's purpose varies between different Final Fantasy games: resistance to attacks (like the
#           defense stat), how much HP is gained during a level up, or resistance to status effects.


from math import floor
from random import randint, randrange

MAX_HIT_POINTS = 9999

class Character:
    """Общий класс для персонажей."""
    # def __init__(self):
    #     pass

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
    max_hp = property(get_max_hp, set_max_hp)


    __hp = 0
    def get_hp(self):
        return self.__hp
    def set_hp(self, value):
        if value < 0:  # Здоровье не может быть меньше 0
            value = 0

        if value > self.__max_hp:  # Здоровье не может быть больше максимального
            value = self.__max_hp
        self.__hp = value
    hp = property(get_hp, set_hp)


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
    atk = 0

    def __repr__(self):
        return "{} lvl: {}. {}".format(self.name, self.level, self.description)

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


class Zombi(Character):
    """Класс Зомби."""
    def __init__(self):
        self.name = "Зомби"
        self.description = "Когда-то это было живым существом."

        self.atk = 40

        self.level = 7
        self.max_hp, self.hp = 468, 468
        self.strength = 30
        self.vit = 10
        self.mag = 6
        self.spr = 5
        self.spd = 21
        self.eva = 0
        self.hit = 100
        self.luck = 10


class Goblin(Character):
    """Класс Гоблин."""
    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."

        self.atk = 30

        self.level = 17
        self.max_hp, self.hp = 482, 482
        self.strength = 18
        self.vit = 5
        self.mag = 10
        self.spr = 4
        self.spd = 17
        self.eva = 10
        self.hit = 100
        self.luck = 15