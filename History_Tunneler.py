__author__ = 'ipetrash'

class Attributes:
    """Общий класс описывающий аттрибуты персонажей и монстров."""
    def __init__(self):
        pass

    # Полезные и просто интересные ссылки:
    # http://ru.rpg.wikia.com/wiki/%D0%90%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B
    # http://ru.rpg.wikia.com/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B8%D1%87%D0%BD%D1%8B%D0%B5_%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8
    # http://ru.rpg.wikia.com/wiki/%D0%A5%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0
    # Сила (ST), Ловкость (DX), Интеллект (IQ), Здоровье (HT)
    st = 0  # strength / сила
    ht = 0  # health / здоровье
    dx = 0  # dexterity / ловкость
    iq = 0  # intellect / интеллект

    health = 0
    max_health = 0


class Character:
    """Общий класс для персонажей и монстров."""
    def __init__(self):
        pass

    def __repr__(self):
        return "{} lvl: {}".format(self.name, self.level)

    # name = CharacterName()
    name = "???"
    level = 1

    attr = Attributes()


class Zombi(Character):
    """Класс Зомби."""
    def __init__(self):
        self.name = "Зомби"
        self.level = 2


z = Zombi()
print(z)
print(z.attr.health)


# Проверка пользовательского модуля
import Story
print(Story.ENTRY)