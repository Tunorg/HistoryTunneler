__author__ = 'ipetrash'

# import Story
import Zoo
import Char
# import time

# TODO: Добавить модуль теста

if __name__ == '__main__':
    # # Проверка пользовательского модуля
    # print(Story.ENTRY)
    #
    # print()
    # z = Zoo.Zombi()
    # print(z)
    # g = Zoo.Goblin()
    # print(g)
    #
    # # Эмитация боя
    # while z.hp > 0 and g.hp > 0:
    #     print("______________________")
    #     z.attack_to(g)
    #     g.attack_to(z)
    #     time.sleep(1)
    #
    # print("\n\n{} hp: {} and {} hp: {}".format(z.name, z.hp, g.name, g.hp))
    # if z.hp == 0 and g.hp == 0:
    #     print("Оба сдохли!")
    # else:
    #     print("{} победил!".format(z.name if z.hp else g.name))

    # z = Zoo.Zombi()
    # print(z)
    #
    # g = Zoo.Goblin()
    # print(g)

    # h = Zoo.Hero()
    # print(h)

    # print()
    # print("Для получения {0} уровня нужно {1} опыта.\n"
    #       "Базовое здоровье {0} уровня будет равно {2}".format(6, Char.EXPS[6], Char.HPMOD[6]))


    # Проверка добавления опыта
    # print()
    # h = Zoo.Hero()
    # print(h)
    # h.exp += 1000
    #
    # h.exp += 10
    # print(h)
    # h.exp += 10
    # h.exp += 5
    # print(h)
    # h.exp += 12
    # print(h)
    #
    # # Проверка изменения уровня
    # print()
    # h = Zoo.Hero()
    # h.level = 10
    # print(h)
    # h.level = 1
    # print(h)

    # print("\nМаксимальный уровень: {}".format(Char.MAX_LEVEL))
    #
    # # Сыграем в ситуацию, когда уровень оказался выше максимального
    # print()
    # h = Zoo.Hero()
    # h.level = Char.MAX_LEVEL + 100

    # Проверка изменения статов при изменении уровня
    Char.DEBUG_MODE = False  # Убираем вывод в консоль
    print()
    h = Zoo.Hero()
    print(h)
    h.level += 1
    print(h)
    h.level += 1
    print(h)


    import CharType
    z2 = Zoo.Zombi()
    # Тип можно динамически изменить
    z2.type = CharType.SuperZombiType()
    print()
    print(z2)
    z2.level += 1
    print(z2)
    z2.level += 1
    print(z2)


    z = Zoo.Zombi()
    print()
    print(z)
    z.level += 1
    print(z)
    z.level += 1
    print(z)


    g = Zoo.Goblin()
    print()
    print(g)
    g.level += 1
    print(g)
    g.level += 1
    print(g)


    f = Char.Character()
    f.level = 1
    f.name = "Неизвестная монстр"
    print()
    print(f)
    f.level += 1
    print(f)
    f.level += 1
    print(f)