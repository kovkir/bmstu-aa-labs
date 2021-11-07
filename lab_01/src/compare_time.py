from time import process_time
import matplotlib.pyplot as plt 

from algorithms import lev_table, dam_lev_table, lev_recursion, dam_lev_recursion
from color import set_color, base_color, purple


def generate_strings(string_length = 5):
    s1 = ''
    s2 = ''

    for _ in range(string_length):
        s1 += 'a'
        s2 += 'b'

    return s1, s2
    

def time_analysis(function, iterations, length):
    string_1, string_2 = generate_strings(length)

    time_start = process_time()

    for i in range(iterations):
        function(string_1, string_2, False)

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def print_measurement_res(sizes, time_lev_table, time_dam_lev_table, 
                          time_lev_recursion, time_dam_lev_recursion):

    print("\n%s%s  Длина  | Левенштейн (м) | Дамерау-Левенштейн (м) | Левенштейн (р) | Дамерау-Левенштейн (р) \n" 
                 "-------------------------------------------------------------------------------------------%s%s"
        %(set_color, purple, set_color, base_color))

    ind = 0

    for num in sizes:
        print("%5d    %s%s|%s%s%13.2e   %s%s|%s%s%17.2e       %s%s|%s%s%13.2e   %s%s|%s%s%17.2e       " \
            %(num,                     set_color, purple, set_color, base_color, 
              time_lev_table[ind],     set_color, purple, set_color, base_color,
              time_dam_lev_table[ind], set_color, purple, set_color, base_color,
              time_lev_recursion[ind], set_color, purple, set_color, base_color,
              time_dam_lev_recursion[ind]))

        ind += 1


def build_graph(sizes, time_lev_table, time_dam_lev_table, 
                time_lev_recursion, time_dam_lev_recursion):

    fig1 = plt.figure(figsize = (10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_lev_table,         label = "Левенштейн (матричная)")
    plot.plot(sizes, time_dam_lev_table,     label = "Дамерау-Левенштейн (матричная)")
    plot.plot(sizes, time_lev_recursion,     label = "Левенштейн (рекурсивная)")
    plot.plot(sizes, time_dam_lev_recursion, label = "Дамерау-Левенштейн (рекурсивная)")

    plt.legend()
    plt.grid()
    plt.title("Сравнение алгоритмом по времени")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина (кол-во букв)")
    plt.yscale("log")
    
    plt.show()


def compare_time():

    time_lev_table         = []
    time_dam_lev_table     = []
    time_lev_recursion     = []
    time_dam_lev_recursion = []

    sizes = [1, 2, 3, 4, 5, 6, 7, 8]

    for n in sizes:
        time_lev_table.append(time_analysis(lev_table, 2000, n))
        time_dam_lev_table.append(time_analysis(dam_lev_table, 2000, n))
        time_lev_recursion.append(time_analysis(lev_recursion, 10, n))
        time_dam_lev_recursion.append(time_analysis(dam_lev_recursion, 10, n))

    print_measurement_res(sizes, time_lev_table, time_dam_lev_table, 
                          time_lev_recursion, time_dam_lev_recursion)

    build_graph(sizes, time_lev_table, time_dam_lev_table, 
                time_lev_recursion, time_dam_lev_recursion)
