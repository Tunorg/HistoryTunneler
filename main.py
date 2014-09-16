"""main.py: Запуск приложения начинается с этого модуля"""

__author__ = 'ipetrash'


import ClassPersonage
import BasePersonage as bp
import time
from collections import defaultdict


def set_num_pers_in_group(group):
    """
    Функция добавляет номер к имени персонажа, если такой
    тип персонажа уже есть в группе.
    """

    # Создаем словарь, ключем которого будет тип персонажа, а значением -- количество
    # персонажей такого типа в группе
    pers_count = defaultdict(int)

    # Перебор персонажей в группе
    for p in group:
        k = type(p)  # Ключом является имя типа персонажа
        pers_count[k] += 1  # Добавляем 1 к количеству персонажей в группе
        c = pers_count[k]  # Получение количества персонажей такого типа в группе
        if c > 1:  # Если персонажей больше 1
            p.name += " {}".format(c)  # Добавление номера к имени персонажа


# TODO: добавить выбор действий
def sandbox(g1, g2):
    """Песочница для боя между двумя группами."""

    # Добавление номера к персонажам в группе
    set_num_pers_in_group(g1)
    set_num_pers_in_group(g2)

    # Словарь, у которого ключом является персонаж, а значением номер группы,
    # в которую входит персонаж
    pers_number_group = dict()
    for p in g1:
        pers_number_group[p] = 1
    for p in g2:
        pers_number_group[p] = 2

    # Объединим группы
    commons = g1 + g2

    # Определим порядок хода:
    # первый в списке будет иметь наибольшую скорость и, соответственно, будет первым ходить, при нескольких
    # персонажах, имеющих одинаковую скорость, положение в списке будет определяться алгоритмос функции sorted.
    sorted_commons = sorted(commons, key=lambda x: x.speed, reverse=True)

    print("\nПорядок хода:")
    for p in sorted_commons:
        print("Группа: [{}]: Скорость: {}, {} (lvl {})".format(pers_number_group[p], p.speed, p.name, p.level))
    print()

    ## Бой
    c = 1  # Количество раундов
    t = time.time()
    h = g1[0]  # Первая группа -- герой

    # Пока герой жив и в вражеской группе есть персонажи
    while not h.dead and g2:
        time.sleep(1.5)

        print("Раунд {}".format(c))

        for p in commons:
            cur_is_g1 = p in g1
            enemy_group = g2 if cur_is_g1 else g1
            if not enemy_group:
                print("Из вражеской группы все мертвы!")
                break

            enemy = enemy_group[0]
            bp.DEBUG_MODE = True
            p.attack_to(enemy)
            bp.DEBUG_MODE = False
            if enemy.dead:
                commons.remove(enemy)
                enemy_group.remove(enemy)

        c += 1

    print()
    if h.dead:
        print("Ты умер! Вот ты лах!")
    else:
        print("Ты победил!")

    print("Бой занял {} раундов и {:.1f} секунд.".format(c, time.time() - t))


if __name__ == '__main__':
    # Вывод состояния персонажей и показ изменения статов при изменении уровня
    bp.DEBUG_MODE = False  # Убираем вывод в консоль
    bp.DEBUG_MODE_GET_SET = False  # Убираем вывод в консоль информацию о set и get методах дескрипторах

    # Подготовка групп к бою:
    h = ClassPersonage.Hero()
    h.level = 3

    z1 = ClassPersonage.Zombi()
    z2 = ClassPersonage.Zombi()
    z3 = ClassPersonage.Goblin()
    z4 = ClassPersonage.Zombi()
    z5 = ClassPersonage.Goblin()
    z6 = ClassPersonage.Ork()

    g1 = [h]
    g2 = [z1, z2, z3, z4, z5, z6]

    # Бой:
    sandbox(g1, g2)
