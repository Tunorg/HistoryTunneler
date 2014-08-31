__author__ = 'ipetrash'

# import Story
import Zoo
import Character

# import time

if __name__ == '__main__':
    try:
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
        # # TODO: воспользоваться исключениями, чтоб отлавливать, когда кто-то умрет
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

        z = Zoo.Zombi()
        print(z)

        g = Zoo.Goblin()
        print(g)

        h = Zoo.Hero()
        print(h)

        print()
        print("Для получения {0} уровня нужно {1} опыта.\n"
              "Базовое здоровье {0} уровня будет равно {2}".format(6, Character.EXPS[6], Character.HPMOD[6]))

    except Character.DeadException as err:
        print("Сообщение: {} --> {}".format(err, err.character))

    except Character.HealWhenDeadException as err:
        print("Сообщение: {} --> {}".format(err, err.character))