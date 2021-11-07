from random import randint

def get_arr_sorted(size):
    arr = list()

    for i in range(size):
        arr.append(i)

    return arr


def get_arr_down_sorted(size):
    arr = list()

    for i in range(size):
        arr.append(size - i)

    return arr


def get_arr_random(size):
    arr = list()

    for _ in range(size):
        arr.append(randint(0, 100))

    return arr


def get_arr_by_type(option, size):

    type = "Не определено"

    if option == 1:
        arr = get_arr_sorted(size)
        type = "Отсортированный "

    elif option == 2:
        arr = get_arr_down_sorted(size)
        type = "Отсортированный в обратном порядке "

    elif option == 3:
        arr = get_arr_random(size)
        type = "Случайный "

    return arr, type
