from time import process_time
import matplotlib.pyplot as plt 
from copy import deepcopy

from get_array import get_arr_by_type
from color import set_color, base_color, red, blue, green, purple
from sorts import bubble_sort, select_sort, insertion_sort

TIMES = 10


def get_process_time(func, arr):
    time_res = 0

    for _ in range(TIMES):
        copy_arr = deepcopy(arr)

        time_start = process_time()
        func(copy_arr, len(copy_arr))
        time_end = process_time()

        time_res += time_end - time_start

    return time_res / TIMES


def build_graph(sizes, time_bubble, time_select, time_insertion, type):

    fig1 = plt.figure(figsize = (10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_bubble,    label = "Сортировка пузырьком")
    plot.plot(sizes, time_select,    label = "Сортировка выбором")
    plot.plot(sizes, time_insertion, label = "Сортировка вставками")

    plt.legend()
    plt.grid()
    plt.title(type + "массив")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина (эл)")
    
    plt.show()
    

def array_type_input():
    try:
        option = int(input("%s%s\n\t\tВведите тип массива \n\n"
                            "\t1 - отсортированный\n"
                            "\t2 - отсортированный в обратном порядке\n"
                            "\t3 - случайный\n\n"
                            "\tВыбор: %s%s"\
                            %(set_color, blue, set_color, base_color)))
        if option > 3 or option < 1:
            print("%s%s\nОжидался ввод целого чилово числа от 0 до 2 %s%s"
                %(set_color, red, set_color, base_color))
            option = 0

    except:
        print("%s%s\nОжидался ввод целого чилово числа от 0 до 2 %s%s"
            %(set_color, red, set_color, base_color))
        option = 0

    return option


def print_measurement_res(sizes, time_bubble, time_select, time_insertion, type):

    print("%s%s\n\n" %(set_color, green) + type + \
          "массив: \n%s%s" %(set_color, base_color))

    print("%s%s  Размер |  пузырьком  |   выбором   |   вставками\n" 
              "-----------------------------------------------------%s%s"
        %(set_color, purple, set_color, base_color))

    ind = 0

    for num in sizes:
        print("%6d   %s%s|%s%s%12.4e %s%s|%s%s%12.4e %s%s|%s%s%12.4e" \
            %(num,              set_color, purple, set_color, base_color, 
              time_bubble[ind], set_color, purple, set_color, base_color,
              time_select[ind], set_color, purple, set_color, base_color,
              time_insertion[ind]))

        ind += 1


def compare_time():
    time_bubble    = []
    time_select    = []
    time_insertion = []

    option = array_type_input()

    if option == 0:
        return

    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    for num in sizes:
        arr, type = get_arr_by_type(option, num)

        time_bubble.append(get_process_time(bubble_sort, deepcopy(arr)))
        time_select.append(get_process_time(select_sort, deepcopy(arr)))
        time_insertion.append(get_process_time(insertion_sort, deepcopy(arr)))

    print_measurement_res(sizes, time_bubble, time_select, time_insertion, type)
    build_graph(sizes, time_bubble, time_select, time_insertion, type)
