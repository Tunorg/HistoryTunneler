"""main.py: Запуск приложения начинается с этого модуля"""

__author__ = 'ipetrash'


# import Story
import Zoo
import Personage
# import Type
import time


if __name__ == '__main__':
    # Вывод состояния персонажей и показ изменения статов при изменении уровня
    Personage.DEBUG_MODE = False  # Убираем вывод в консоль
    Personage.DEBUG_MODE_GET_SET = False  # Убираем вывод в консоль информацию о set и get методах дескрипторах

    gua_badan = Zoo.Ork()
    gua_badan.name = "Большой Гуа-бадан"
    gua_badan.desc = "Моя большая и сильная!"
    print(gua_badan)
    print("{}: '{}'".format(gua_badan.name, gua_badan.desc))

    # h = Zoo.Hero()
    # print(h)
    #
    # z = Zoo.Zombi()
    # z.level = 3  # Пусть у зомби будет 3-й уровень
    # print(z)
    #
    # Char.DEBUG_MODE = True
    # c = 1
    #
    # t = time.time()
    # while not h.dead or not z.dead:
    #     print()
    #     print("Раунд {}".format(c))
    #     print("{}(hp: {})  VS  {} (hp: {})".format(h.name, h.hp, z.name, z.hp), end="\n ")
    #
    #     h.attack_to(z)
    #     if z.dead:
    #         break
    #
    #     z.attack_to(h)
    #     if h.dead:
    #         break
    #
    #     c += 1
    #     time.sleep(1.5)  # Ждем 1.5 секунды
    #     # input()
    #
    # print("\n")
    # if h.dead:
    #     print("Ты умер! Вот ты лах!")
    #
    # elif z.dead:
    #     print("Поздравляю чувак! Ты убил зомби!!")
    #     h.exp += z.exp
    #
    # print("Бой занял {} раундов и {:.1f} секунд.".format(c, time.time() - t))
    #
    # Char.DEBUG_MODE = False