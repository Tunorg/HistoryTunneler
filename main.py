__author__ = 'ipetrash'

import Story
import Character

import time

if __name__ == '__main__':
    # Проверка пользовательского модуля
    print(Story.ENTRY)

    print()
    z = Character.Zombi()
    print(z)
    g = Character.Goblin()
    print(g)

    # Эмитация боя
    # TODO: воспользоваться исключениями, чтоб отлавливать, когда кто-то умрет
    while z.hp > 0 and g.hp > 0:
        print("______________________")
        z.attack_to(g)
        g.attack_to(z)
        time.sleep(1)

    print("\n\n{} hp: {} and {} hp: {}".format(z.name, z.hp, g.name, g.hp))
    if z.hp == 0 and g.hp == 0:
        print("Оба сдохли!")
    else:
        print("{} победил!".format(z.name if z.hp else g.name))