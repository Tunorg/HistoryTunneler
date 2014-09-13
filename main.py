"""main.py: Запуск приложения начинается с этого модуля"""

__author__ = 'ipetrash'


import ClassPersonage
import BasePersonage as bp
import time


def sandbox(g1, g2):
    print("Группа 1:")
    for i, p in enumerate(g1):
        print("{}. {}".format(i + 1, "{}(lvl {}): {}".format(p.name, p.level, type(p))))

    print()
    print("Группа 2:")
    for i, p in enumerate(g2):
        print("{}. {}".format(i + 1, "{}(lvl {}): {}".format(p.name, p.level, type(p))))

    # определим у кого во второй группе наибольшая скорость
    # первый в списке будет иметь наибольшую скорость
    print("\nГруппа 2, отсортированная по скорости:")
    sorted_group2 = sorted(g2, key=lambda x: x.speed, reverse=True)
    for p in sorted_group2:
        print("Скорость: {}: {}".format(p.speed, "{}(lvl {}): {}".format(p.name, p.level, type(p))))


    commons = g1 + g2
    print()
    print("Объединенные группы:")
    for i, p in enumerate(commons):
        print("{}. {}".format(i + 1, "{}(lvl {}): {}".format(p.name, p.level, type(p))))


    # определим порядок хода:
    # первый в списке будет иметь наибольшую скорость и, соответственно, будет первым ходить, при нескольких
    # персонажах, имеющих одинаковую скорость, положение в списке будет определяться алгоритмос функции sorted.
    sorted_commons = sorted(commons, key=lambda x: x.speed, reverse=True)
    first = sorted_commons[0]
    print("\n\nПервый ходит: {}".format("{}(lvl {}): {}".format(first.name, first.level, type(first))))
    print("\nПорядок хода:")
    for p in sorted_commons:
        print("Скорость: {}: {}".format(p.speed, "{}(lvl {}): {}".format(p.name, p.level, type(p))))


if __name__ == '__main__':
    # Вывод состояния персонажей и показ изменения статов при изменении уровня
    bp.DEBUG_MODE = False  # Убираем вывод в консоль
    bp.DEBUG_MODE_GET_SET = False  # Убираем вывод в консоль информацию о set и get методах дескрипторах


    # TODO: добавить бой командами с выбором действий
    h = ClassPersonage.Hero()

    z1 = ClassPersonage.Zombi()
    z2 = ClassPersonage.Zombi()
    z3 = ClassPersonage.Goblin()
    z4 = ClassPersonage.Ork()

    g1 = [h]
    g2 = [z1, z2, z3, z4]
    sandbox(g1, g2)


    h = ClassPersonage.Hero()
    z = ClassPersonage.Zombi()
    z.level = 2  # Пусть у зомби будет 3-й уровень
    print()
    print(h)
    print(z)

    bp.DEBUG_MODE = True
    c = 1

    t = time.time()
    while not h.dead or not z.dead:
        print()
        print("Раунд {}".format(c))
        print("{}(hp: {})  VS  {} (hp: {})".format(h.name, h.hp, z.name, z.hp), end="\n ")

        h.attack_to(z)
        if z.dead:
            break

        z.attack_to(h)
        if h.dead:
            break

        c += 1
        time.sleep(1.5)  # Ждем 1.5 секунды
        # input()

    print("\n")
    if h.dead:
        print("Ты умер! Вот ты лах!")

    elif z.dead:
        print("Поздравляю чувак! Ты убил {} lvl {}!!".format(z.name, z.level))

    print("Бой занял {} раундов и {:.1f} секунд.".format(c, time.time() - t))
