__author__ = 'ipetrash'

import Character

if __name__ == '__main__':
    z = Character.Zombi()
    print(z)
    print(z.attr.health)


    # Проверка пользовательского модуля
    import Story
    print(Story.ENTRY)