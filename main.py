"""main.py: Запуск приложения начинается с этого модуля"""

__author__ = 'ipetrash'


import ClassPersonage
import Personage
import time


def sandbox(g1, g2):
    print("Group1: {}".format(g1))
    print("Group2: {}".format(g2))


if __name__ == '__main__':
    # Вывод состояния персонажей и показ изменения статов при изменении уровня
    Personage.DEBUG_MODE = False  # Убираем вывод в консоль
    Personage.DEBUG_MODE_GET_SET = False  # Убираем вывод в консоль информацию о set и get методах дескрипторах

    # TODO: добавить бой командами с выбором действий
    #
    h = ClassPersonage.Hero()
    z1 = ClassPersonage.Zombi()
    z2 = ClassPersonage.Zombi()

    g1 = [h]
    g2 = [z1, z2]
    sandbox(g1, g2)


    # h = ClassPersonage.Hero()
    # print(h)
    #
    # z = ClassPersonage.Zombi()
    # z.level = 3  # Пусть у зомби будет 3-й уровень
    # print(z)
    #
    # Personage.DEBUG_MODE = True
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
    #     print("Поздравляю чувак! Ты убил {} lvl {}!!".format(z.name, z.level))
    #     h.exp += z.gives_exp
    #
    # print("Бой занял {} раундов и {:.1f} секунд.".format(c, time.time() - t))
    #
    # Personage.DEBUG_MODE = False