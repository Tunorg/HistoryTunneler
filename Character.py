__author__ = 'ipetrash'

class States:
    """Общий класс описывающий статы персонажей."""
    def __init__(self):
        pass

    # Статы и формулы рассчета статов некоторых игр FF
    # http://finalfantasy.wikia.com/wiki/Stats

    # Характеристики в FF8
    # http://squarefaction.ru/game/final-fantasy-viii/articles/10480-parametry-geroev-v-final-fantasy-viii

    # Характеристики в FF7
    # http://ffforever.info/index.cgi?section=ff7cc;p=experience
    # http://www.ign.com/faqs/2004/final-fantasy-vii-stat-building-faq-452504

    # Характеристики в FF6
    # http://www.cavesofnarshe.com/ff6/stats.php

    # Статы в FF9
    # http://letao.is-a-geek.net/ff9stats/

    # Полезные и просто интересные ссылки:
    # http://ru.rpg.wikia.com/wiki/%D0%90%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B
    # http://ru.rpg.wikia.com/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B8%D1%87%D0%BD%D1%8B%D0%B5_%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8
    # http://ru.rpg.wikia.com/wiki/%D0%A5%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0
    # Сила (ST), Ловкость (DX), Интеллект (IQ), Здоровье (HT)
    # st = 0  # strength / сила
    # ht = 0  # health / здоровье
    # dx = 0  # dexterity / ловкость
    # iq = 0  # intellect / интеллект
    #
    # dm = 0  # damage / повреждение
    # critical = 0  # chance to deal critical / шанс нанести крит
    # hp = 0  # hit point
    # max_hp = 0
    # # health = 0
    # # max_health = 0

    level = 0
    exp = 0

    hp = 0  # здоровье
    strength = 0  # сила
    defense = 0  # зашита
    magic_defense = 0  # магическая защита
    accuracy = 0  # точность
    speed = 0  # скорость
    evasion = 0  # уклонение
    magic_evasion = 0  # уклонение от магии
    stamina = 0  # выносливость
    absorb = 0  # поглощение
    agility = 0  # ловкость
    luck = 0  # удача
    vitality = 0  # живучесть

    attack_power = 0  # урон

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





class Character:
    """Общий класс для персонажей."""
    def __init__(self):
        pass

    def __repr__(self):
        return "{} lvl: {}. {}".format(self.name, self.level, self.description)

    description = "???"

    name = "???"
    level = 1

    states = States()

    def attack_to(self, other):
        """Функция атаки персонажей."""
        pass


class Zombi(Character):
    """Класс Зомби."""
    def __init__(self):
        self.name = "Зомби"
        self.level = 2
        self.description = "Живой труп."


class Skeleton(Character):
    """Класс Скелет."""
    def __init__(self):
        self.name = "Скелет"
        self.level = 1
        self.description = "Когда-то это было живым существом, а теперь от него остались только кости."


class Goblin(Character):
    """Класс Гоблин."""
    def __init__(self):
        self.name = "Гоблин"
        self.level = 1
        self.description = "Маленькое, пронырливое, трусливое зеленокожее существо."
