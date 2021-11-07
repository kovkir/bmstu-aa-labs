import matplotlib.pyplot as plt 
import numpy as np
from color import base_color, red, yellow


MSG = "\n\t\t%sМеню\n\n"\
      "\t1. Построить граф зависимости времени от кол-ва потоков \n"\
      "\t2. Построить граф зависмости времени от размера матрицы \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s"\
      %(yellow, base_color)


def build_graph_different_threads():

    threads = [1, 2, 4, 8, 16, 32]

    time_one_thread   = [0.008690, 0.008690, 0.008690, 0.008690, 0.008690, 0.008690]
    time_many_threads = [0.008690, 0.004595, 0.002507, 0.002071, 0.002152, 0.002262]

    fig1 = plt.figure(figsize = (9, 6))
    plot = fig1.add_subplot()
    plot.plot(threads, time_one_thread,   label = "Однопоточная реализация")
    plot.plot(threads, time_many_threads, label = "Многопоточная реализация")

    plt.legend()
    plt.grid()
    plt.title("Зависимость времени работы алгоритмов от кол-ва потоков\n "
              "(размер матрицы 200х200)")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Кол-во потоков (шт)")
    plt.xticks(np.arange(0, 33, 4))
    
    plt.show()


def build_graph_different_sizes():
    sizes = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    time_one_thread   = [0.001472, 0.001822, 0.002237, 0.002762, 0.003358, 0.004008, 
                         0.004776, 0.005545, 0.006478, 0.007525, 0.008690]

    time_many_threads = [0.000445, 0.000552, 0.000755, 0.000937, 0.001029, 0.001324,
                         0.001319, 0.001393, 0.001912, 0.001833, 0.002071]

    fig1 = plt.figure(figsize = (9, 6))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_one_thread,   label = "Однопоточная реализация")
    plot.plot(sizes, time_many_threads, label = "Многопоточная реализация")

    plt.legend()
    plt.grid()
    plt.title("Зависимость времени работы алгоритмов от размера матрицы\n "
              "(в многопоточной реализации используется 8 потоков)")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Кол-во потоков (шт)")
    plt.xticks(np.arange(100, 201, 10))
    
    plt.show()


def input_option():
    try:
        option = int(input(MSG))
    except:
        option = -1
    
    if option < 0 or option > 2:
        print("%s\nОжидался ввод целого чилово числа от 0 до 2 %s"
            %(red, base_color))

    return option


def main():
    option = -1

    while option != 0:
        option = input_option()

        if option == 1:
            build_graph_different_threads()

        elif option == 2:
            build_graph_different_sizes()


if __name__ == "__main__":
    main()
