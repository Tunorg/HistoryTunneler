__author__ = 'ipetrash'

import Character

if __name__ == '__main__':
    # Проверка пользовательского модуля
    import Story
    print(Story.ENTRY)

    print()
    z = Character.Zombi()
    print(z)
    s = Character.Skeleton()
    print(s)
    g = Character.Goblin()
    print(g)