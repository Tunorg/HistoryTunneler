__author__ = 'ipetrash'

# import Story
import Zoo
import Char
# import time
import Type


# TODO: Добавить модуль теста

if __name__ == '__main__':
    # Проверка изменения статов при изменении уровня
    Char.DEBUG_MODE = False  # Убираем вывод в консоль

    def print_test_char(char):
        print()
        print(char)
        # print("id: {}".format(hex(id(char))))  # hex-значение объекта
        char.level_up()
        print(char)
        char.level_up()
        print(char)
        char.level = 99
        print(char)


    h = Zoo.Hero()
    print_test_char(h)

    z = Zoo.Zombi()
    print_test_char(z)

    z2 = Zoo.Zombi()
    z2.type = Type.SuperZombi()  # Тип персонажа можно динамически менять
    print_test_char(z2)

    g = Zoo.Goblin()
    print_test_char(g)


    # Проверка уворота зомби, при нулевой удаче и шанса уклонения и при 100% точности противника
    # z = Zoo.Zombi()
    # z.type.b_luck = 0
    # z.level = Char.MAX_LEVEL
    # z.update_states()
    # print(z)
    #
    # g = Zoo.Goblin()
    # g.type.b_hit = 100
    # g.update_states()
    #
    # Char.DEBUG_MODE = True
    #
    # for i in range(100):
    # g.attack_to(z)
    #     if z.dead:
    #         break