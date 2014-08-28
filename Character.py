__author__ = 'ipetrash'

# TODO: Переименовать в статы
class Attributes:
    """Общий класс описывающий аттрибуты персонажей и монстров."""
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
    st = 0  # strength / сила
    ht = 0  # health / здоровье
    dx = 0  # dexterity / ловкость
    iq = 0  # intellect / интеллект

    dm = 0  # damage / повреждение
    critical = 0  # chance to deal critical / шанс нанести крит
    hp = 0  # hit point
    max_hp = 0
    # health = 0
    # max_health = 0


class Character:
    """Общий класс для персонажей."""
    def __init__(self):
        pass

    def __repr__(self):
        return "{} lvl: {}".format(self.name, self.level)

    name = "???"
    level = 1

    attr = Attributes()

    def attack_to(self, other):
        """Функция атаки персонажей."""
        pass


class Zombi(Character):
    """Класс Зомби."""
    def __init__(self):
        self.name = "Зомби"
        self.level = 2
