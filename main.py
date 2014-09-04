"""main.py: Запуск приложения начинается с этого модуля"""

__author__ = 'ipetrash'


# import Story
import Zoo
import Char
# import Type
# import time


# TODO: Добавить модуль теста


if __name__ == '__main__':
    # Вывод состояния персонажей и показ изменения статов при изменении уровня
    Char.DEBUG_MODE = False  # Убираем вывод в консоль
    Char.DEBUG_MODE_GET_SET = False  # Убираем вывод в консоль информацию о set и get методах дескрипторах


    h = Zoo.Hero()
    print(h)

    z = Zoo.Zombi()
    z.level = 3  # Пусть у зомби будет 3-й уровень
    print(z)

    Char.DEBUG_MODE = True
    c = 1
    while not h.dead or not z.dead:
        print()
        print("Раунд {}".format(c))
        print("{}(hp: {})  VS  {} (hp: {})".format(h.name, h.hp, z.name, z.hp), end="\n ")

        h.attack_to(z)
        if z.dead:
            break
        z.attack_to(h)

        c += 1
        # time.sleep(1)
        input()

    print("\n")
    if h.dead:
        print("Ты умер! Вот ты лах!")

    elif z.dead:
        print("Поздравляю чувак! Ты убил зомби!!")
        h.exp += z.exp

    print("Бой занял {} раундов.".format(c))

    Char.DEBUG_MODE = False